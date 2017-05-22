
import os

from PIL import Image, ImageChops

from .image_config import image_config
from AXUI.logger import LOGGER

def image_compare(image1, image2, diff_image_name="diff.bmp"):
    '''compare two images, return difference percentage
    #code from http://rosettacode.org/wiki/Percentage_difference_between_images#Python
    '''
    gen_diff_image = image_config.gen_diff_image
    diff_image_location = image_config.diff_image_location

    i1 = Image.open(image1)
    i2 = Image.open(image2)
    assert i1.mode == i2.mode, "Different kinds of images: %s VS %s" % (i1.mode, i2.mode)
    assert i1.size == i2.size, "Different sizes: %s, %s" % (i1.size, i2.size)
    
    #generate diff bitmap
    if gen_diff_image:
        diff = ImageChops.difference(i1, i2)
        diff_image_path = os.path.join(diff_image_location, diff_image_name)
        diff.save(diff_image_path)
        LOGGER.debug("Diff image save to: %s" % diff_image_path)
    
    #caculate the diff percentage
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum((p1==p2) and 1 or 0 for p1,p2 in pairs)
    else:
        dif = sum((c1==c2) and 1 or 0 for p1,p2 in pairs for c1,c2 in zip(p1,p2))
     
    ncomponents = i1.size[0] * i1.size[1] * 3
    dif_percentage = float(dif) / ncomponents
    LOGGER.debug("Difference (percentage): %f" % dif_percentage)
    return dif_percentage

