
import os
from AXUI.logger import logger_config

class Config(object):

    _gen_diff_image = True

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
        _diff_image_location = os.path.join(os.path.dirname(logger_config.logging_file_path), "diff")
        if os.path.isdir(_diff_image_location):
            os.makedirs(_diff_image_location)
        return _diff_image_location

image_config = Config()