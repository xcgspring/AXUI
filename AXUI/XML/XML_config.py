
import os

class Config(object):
    '''
    configs for core module
    '''
    _app_map_location       = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "example")
    _schema_location        = os.path.join(os.path.dirname(os.path.abspath(__file__)), "schemas")
    _time_out               = 5
    _screenshot_location    = os.path.dirname(os.path.abspath(__file__))
    _screenshot_on_failure  = False

    def __str__(self):
        '''
        some help str for this config
        '''
        pass

    @property
    def app_map_location(self):
        return self._app_map_location

    @app_map_location.setter
    def app_map_location(self, input):
        #check if input location exist
        if not os.path.isdir(input):
            raise ValueError("Expect a valid directory for app_map_location, get %s" % input)
        self._app_map_location = input

    @property
    def schema_location(self):
        return self._schema_location

    @schema_location.setter
    def schema_location(self, input):
        #check if input location exist
        if not os.path.isdir(input):
            raise ValueError("Expect a valid directory for schema_location, get %s" % input)
        self._schema_location = input

    @property
    def time_out(self):
        return self._time_out

    @time_out.setter
    def time_out(self, input):
        #check if input valid
        try:
            self._time_out = int(input)
        except ValueError:
            raise ValueError("Expect an int value for global time out, get %s" % input)

    @property
    def screenshot_location(self):
        return self._screenshot_location

    @screenshot_location.setter
    def screenshot_location(self, input):
        #check if input valid
        if not os.path.isabs(input):
            raise ValueError("Expect a path for screenshot_location, get %s" % input)
        else:
            if not os.path.isdir(input):
                os.makedirs(input)
            self._screenshot_location = input

    @property
    def screenshot_on_failure(self):
        return self._screenshot_on_failure

    @screenshot_on_failure.setter
    def screenshot_on_failure(self, input):
        accepts = {"TRUE": True, "FALSE": False, True: True, False: False}
        if input in accepts:
            self._screenshot_on_failure = accepts[input]
        elif isinstance(input, str) and input.upper() in accepts:
            self._screenshot_on_failure = accepts[input.upper()]
        else:
            raise ValueError("Expect a True/False for screenshot_on_failure, get %s" % input)

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