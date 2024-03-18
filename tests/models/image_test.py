from model.image import Image
import json

def test_create_image_with_missing_link():
    try:
        image = Image(image_type='Test', description='Test')
    except:
        assert True
    else:
        assert False
        
def test_create_image_with_missing_description():
    try:
        image = Image(link='https://abc.com', image_type='Test')
    except:
        assert True
    else:
        assert False

def test_create_image_with_missing_image_type():
    try:
        image = Image(link='https://abc.com', description='Test')
    except:
        assert True
    else:
        assert False

def test_create_image_with_link_only():
    try:
        image = Image(link='https://abc.com')
    except:
        assert True
    else:
        assert False

def test_create_image_with_description_only():
    try:
        image = Image(description='Test')
    except:
        assert True
    else:
        assert False

def test_create_image_with_image_type_only():
    try:
        image = Image(image_type='Test')
    except:
        assert True
    else:
        assert False

def test_create_image_with_no_properties():
    try:
        image = Image()
    except:
        assert True
    else:
        assert False


def test_create_proper_image():
    image = Image(link='https://abc.com', description='Test', image_type='Test Image')
    assert image.link == 'https://abc.com' and image.description == 'Test' and image.image_type == 'Test Image'

def test_json_format():
    image = Image(link='https://abc.com', description='Test', image_type='Test Image')
    json_output = image.json()
    assert image.link == json_output['link'] and image.description == json_output['description'] and image.image_type == json_output['type']

def test_repr_format():
    image = Image(link='https://abc.com', description='Test', image_type='Test Image')
    assert str(image) == f'Image: {json.dumps(image.json())}'

