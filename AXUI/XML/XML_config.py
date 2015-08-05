
import os
from AXUI.logger import logger_config

class Config(object):
    '''
    configs for core module
    '''
    _app_map_location = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "example")
    _schema_location  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "schemas")
    _time_out         = 5
    _screenshot_option= "always_on"

    def __str__(self):
        '''
        some help str for this config
        '''
        pass

    @property
    def app_map_location(self):
        return self._app_map_location

    @app_map_location.setter
    def app_map_location(self, input_value):
        #check if input_value location exist
        if not os.path.isdir(input_value):
            raise ValueError("Expect a valid directory for app_map_location, get %s" % input_value)
        self._app_map_location = input_value

    @property
    def schema_location(self):
        return self._schema_location

    @schema_location.setter
    def schema_location(self, input_value):
        #check if input_value location exist
        if not os.path.isdir(input_value):
            raise ValueError("Expect a valid directory for schema_location, get %s" % input_value)
        self._schema_location = input_value

    @property
    def time_out(self):
        return self._time_out

    @time_out.setter
    def time_out(self, input_value):
        #check if input_value valid
        try:
            self._time_out = int(input_value)
        except ValueError:
            raise ValueError("Expect an int value for global time out, get %s" % input_value)

    @property
    def screenshot_location(self):
        _screenshot_location=os.path.join(os.path.dirname(logger_config.logging_file_path), "screenshot")
        if not os.path.isdir(_screenshot_location):
            os.makedirs(_screenshot_location)
        return _screenshot_location

    @property
    def screenshot_option(self):
        return self._screenshot_option

    @screenshot_option.setter
    def screenshot_option(self, input_value):
        accepts = ["always_on", "always_off", "on_failure"]
        if input_value in accepts:
            self._screenshot_option = input_value
        else:
            raise ValueError("Expect value in %s, get %s" % (str(accepts), input_value))

    def query_app_map_file(self, app_map_file):
        '''search app_map_file in AppMapLocation, return abs path if found
        Arguments:
            app_map_file: app_map file name
        Returns:
            abs_app_map_file: abs path of the app_map file
        '''
        if os.path.isabs(app_map_file) and os.path.isfile(app_map_file):
            return app_map_file
        else:
            basename = os.path.basename(app_map_file)
            for root, dirs, files in os.walk(self.app_map_location):
                for file_ in files:
                    if file_ == basename:
                        return os.path.join(root, basename)
            raise ValueError("%s not found in %s" % (app_map_file, self.app_map_location))

    def query_schema_file(self, schema_file):
        '''search schema_file in SchemaLocation, return abs path if found
        Arguments:
            schema_file: schema file name
        Returns:
            abs_schema_file: abs path of the schema file
        '''
        if os.path.isabs(schema_file) and os.path.isfile(schema_file):
            return schema_file
        else:
            basename = os.path.basename(schema_file)
            for root, dirs, files in os.walk(self.schema_location):
                for file_ in files:
                    if file_ == basename:
                        return os.path.join(root, basename)
            raise ValueError("%s not found in %s" % (schema_file, self.schema_location))

core_config = Config()