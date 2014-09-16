
import os
import AXUI.logger as AXUI_logger

LOGGER = AXUI_logger.get_logger()

config_section="XML"
default_configs={ "app_map_location": os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "app_map"),
                  "schema_location": os.path.join(os.path.dirname(os.path.abspath(__file__)), "schemas"),
                }

AppMapLocation=default_configs["app_map_location"]
SchemaLocation=default_configs["schema_location"]

class XMLConfigException(Exception):
    pass

def config(configs=default_configs):
    '''
    call back function used by config module
    '''
    global AppMapLocation
    global SchemaLocation
    AppMapLocation=configs["app_map_location"]
    SchemaLocation=configs["schema_location"]
    
def query_app_map_file(app_map_file):
    '''
    search app_map_file in AppMapLocation, return abs path if found 
    '''
    global AppMapLocation
    if os.path.isabs(app_map_file) and os.path.isfile(app_map_file):
        return app_map_file
    else:
        basename = os.path.basename(app_map_file)
        for root, dirs, files in os.walk(AppMapLocation):
            for file_ in files:
                if file_ == basename:
                    return os.path.join(root, basename)
        raise XMLConfigException("%s not found in %s" % (app_map_file, AppMapLocation))
    
def query_schema_file(schema_file):
    '''
    search schema_file in SchemaLocation, return abs path if found 
    '''
    global SchemaLocation
    if os.path.isabs(schema_file) and os.path.isfile(schema_file):
        return schema_file
    else:
        basename = os.path.basename(schema_file)
        for root, dirs, files in os.walk(SchemaLocation):
            for file_ in files:
                if file_ == basename:
                    return os.path.join(root, basename)
        raise XMLConfigException("%s not found in %s" % (schema_file, SchemaLocation))
