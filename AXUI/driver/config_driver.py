
class Config(object):
    _driver_used = "windows"

    def __str__(self):
        return ""

    @property
    def driver_used(self):
        return self._driver_used

    @driver_used.setter
    def driver_used(self, input):
        self._driver_used = input

driver_config = Config()