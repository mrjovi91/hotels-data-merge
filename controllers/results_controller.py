from integrations.suppliers.acme import AcmeSupplier
from integrations.suppliers.patagonia import PatagoniaSupplier
from integrations.suppliers.paperflies import PaperfliesSupplier
from integrations.suppliers.suppliers import suppliers
from model.search_results import SearchResults
from model.result_Item import ResultItem

import json

def sort_by_image_description(image):
    return image['description']

def sort_by_number_of_characters(value):
    return len(value) if value else 0

def check_item_similarity_by_removing_spaces(item, items):
    for value in items:
        if item.replace(' ', '') == value.replace(' ', ''):
            return value
    return None
    
def similar_items_dedup(input_items):
    items = list(set(input_items))
    output = []

    for item in items:
        if len(output) > 0 and ' ' in item:
            item_type = item.split()[-1]
            for value in output.copy():
                if value == item_type:
                    output.remove(value)

        elif len(output) > 0 and ' ' not in item:
            found_duplicate = False
            for value in output.copy():
                if ' ' not in value:
                    continue
                if value.split()[-1] == item:
                    found_duplicate = True
                    break
            if found_duplicate:
                continue

        found_duplicate = False
        if len(output) > 0 and ' ' in item:
            if check_item_similarity_by_removing_spaces(item, output.copy()):
                continue
        output.append(item)
    return output

class ResultsController:

    def __init__(self, search_parameters):
        self._search_parameters = search_parameters
        self._results = {}
        self._merged_results = []

    def search(self):
        for supplier_name, supplier_template in suppliers.items():
            supplier = supplier_template(search_parameters=self._search_parameters)
            supplier.fetch_data()
            self._results[supplier_name] = supplier.return_formatted_data()

    

    def merge_result(self):
        if not self._results:
            raise Exception('Error: Please run search before merge result.')
        hotel_ids = []
        for search_results in self._results.values():
            hotel_ids = hotel_ids + search_results._hotels_id_in_results
        hotel_ids = list(set(hotel_ids))
        for hotel_id in hotel_ids:
            merged_hotel = {
                "id": hotel_id,
                "destination_id": None,
                "name": [],
                "location": {
                    "lat": None,
                    "lng": None,
                    "address": [],
                    "city": [],
                    "country": []
                },
                "description": [],
                "amenities": {
                    "general": [],
                    "room": []
                },
                "images": {},
                "booking_conditions": []
            }
            for hotels in self._results.values():
                for hotel in hotels.results:
                    if hotel.id == hotel_id:
                        if merged_hotel['destination_id'] is None:
                            merged_hotel['destination_id'] = hotel.destination_id
                        merged_hotel['name'].append(hotel.name)
                        if merged_hotel['location']["lat"] is None:
                            merged_hotel['location']["lat"] = hotel.location.lat
                        if merged_hotel['location']["lng"] is None:
                            merged_hotel['location']["lng"] = hotel.location.lng
                        merged_hotel['location']['address'].append(hotel.location.address)
                        merged_hotel['location']['city'].append(hotel.location.city)
                        merged_hotel['location']['country'].append(hotel.location.country)
                        merged_hotel['description'].append(hotel.description)
                        merged_hotel['amenities']["general"] += hotel.amenities.general
                        merged_hotel['amenities']["room"] += hotel.amenities.room

                        for image_type, image in hotel.images.json().items():
                            if image_type not in merged_hotel['images'].keys():
                                merged_hotel['images'][image_type] = image
                            else:
                                merged_hotel['images'][image_type] += image
                        if hotel.booking_conditions is not None:
                            merged_hotel['booking_conditions'] += hotel.booking_conditions
                        break
                
            merged_hotel['name'] = sorted(merged_hotel['name'], key=sort_by_number_of_characters, reverse=True)[0]
            merged_hotel['location']['address'] = sorted(merged_hotel['location']['address'], key=sort_by_number_of_characters, reverse=True)[0]
            merged_hotel['location']['city'] = sorted(merged_hotel['location']['city'], key=sort_by_number_of_characters, reverse=True)[0]
            merged_hotel['location']['country'] = sorted(merged_hotel['location']['country'], key=sort_by_number_of_characters, reverse=True)[0]
            merged_hotel['description'] = sorted(merged_hotel['description'], key=sort_by_number_of_characters, reverse=True)[0]
            merged_hotel['amenities']["general"]  = similar_items_dedup(merged_hotel['amenities']["general"] )
            merged_hotel['amenities']["general"].sort()
            merged_hotel['amenities']["room"]  = similar_items_dedup(merged_hotel['amenities']["room"] )
            merged_hotel['amenities']["room"].sort()

            # Ensure room amenities are not in general
            for item in merged_hotel['amenities']["room"]:
                value = check_item_similarity_by_removing_spaces(item, merged_hotel['amenities']["general"])
                if value is not None:
                    merged_hotel['amenities']["general"].remove(value)

            # Perform dedup of images based on image type and link
            merged_hotel_images = merged_hotel['images'].copy()
            for image_type, images in merged_hotel_images.items():
                del merged_hotel['images'][image_type]
                image_output = {}
                for image in images:
                    if image['link'] not in image_output.keys():
                        image_output[image['link']] = [image['description']]
                    else:
                        image_output[image['link']].append(image['description'])
                for link, description in image_output.copy().items():
                    new_description = sorted(description, key=sort_by_number_of_characters, reverse=True)[0]
                    if image_type not in merged_hotel['images'].keys():
                        merged_hotel['images'][image_type] = [{
                            'link': link,
                            'description': new_description
                        }]
                    else:
                        merged_hotel['images'][image_type].append({
                            'link': link,
                            'description': new_description
                        })
                merged_hotel['images'][image_type].sort(key=sort_by_image_description)

            merged_hotel['booking_conditions'] = sorted(list(set(merged_hotel['booking_conditions'])))
            self._merged_results.append(merged_hotel)

    @property
    def merged_results(self):
        return self._merged_results      

    def json(self):
        output = {}
        for supplier_name, supplier in self._results.items():
            output[supplier_name] = supplier.json()
        return output

            