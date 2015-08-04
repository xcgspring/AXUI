
import os

class Config(object):

    _gen_diff_image = True
    _diff_image_location = os.path.dirname(os.path.abspath(__file__))

    def __str__(self):
        return ""

    @property
    def gen_diff_image(self):
        return self._gen_diff_image

    @gen_diff_image.setter
    def gen_diff_image(self, input):
        accepts = {"TRUE": True, "FALSE": False, True: True, False: False}
        if input in accepts:
            self._gen_diff_image = accepts[input]
        elif isinstance(input, str) and input.upper() in accepts:
            self._gen_diff_image = accepts[input.upper()]
        else:
            raise ValueError("Expect a True/False for screenshot_on_failure, get %s" % input)

    @property
    def diff_image_location(self):
        return self._diff_image_location

    @diff_image_location.setter
    def diff_image_location(self, input):
        #check if input valid
        if not os.path.isabs(input):
            raise ValueError("Expect a path for screenshot_location, get %s" % input)
        else:
            if not os.path.isdir(input):
                os.makedirs(input)
            self._diff_image_location = input

image_config = Config()