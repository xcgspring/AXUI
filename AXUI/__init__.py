
import XML
from config import config



def assertIsValid(element, msg="element not valid"):
    '''check if element valid
    '''
    if element.verify() is None:
        raise AssertionError(msg)
    
#port AppMap here
AppMap=XML.AppMap

#port image_compare here
from image import image_compare

__all__=["config", "assertIsValid", "AppMap", "image_compare"]
