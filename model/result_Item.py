class ResultItem:
    def __init__(self, id, destination_id, name, cell_y):
        self.positionX = positionX
        self.positionY = positionY
        self.path = False
        self.computed = False
        self.current = False
        self.visited = False
        self.backtracked = False
        self.walls = {
            'bottom': [True,  positionX*cell_x, positionY*cell_y + cell_y, positionX*cell_x + cell_x, positionY*cell_y + cell_y],
            'right': [True,  positionX*cell_x + cell_x, positionY*cell_y, positionX*cell_x + cell_x, positionY*cell_y + cell_y]
        }

    @abstractclassmethod
    def get_id(cls, data_item):
        pass

    @abstractclassmethod
    def get_destination_id(cls, data_item):
        pass

    @abstractclassmethod
    def get_name(cls, data_item):
        pass

    @abstractclassmethod
    def get_location(cls, data_item):
        pass

    @abstractclassmethod
    def get_description(cls, data_item):
        pass

    @abstractclassmethod
    def get_amenities(cls, data_item):
        pass

    @abstractclassmethod
    def get_images(cls, data_item):
        pass

    @abstractclassmethod
    def get_booking_conditions(cls, data_item):
        pass

