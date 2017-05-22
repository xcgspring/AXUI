
#port Config
from config import Config

#port Logger
from logger import LOGGER

#port AppMap
from XML import AppMap

#Asserts here
def AssertIsValid(element, msg="element not valid"):
    '''check if element valid
    '''
    if element.verify() is None:
        raise AssertionError(msg)

def AssertIsImageSimiliar(image1, image2, diff_percentage_required=0.1, msg="images not similiar"):
    '''check if two image is simililar
    '''
    from image import image_compare
    diff_percentage = image_compare(image1, image2)
    if diff_percentage > diff_percentage_required:
        raise AssertionError(msg)


__all__=["Config", "LOGGER", "AppMap", "AssertIsValid", "AssertIsImageSame"]
