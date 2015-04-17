
import os

config_section="image"
default_configs={ "gen_diff_image" : "True",
                  "diff_image_location" : os.path.dirname(os.path.abspath(__file__)), 
                }

GenDiffImage=default_configs["gen_diff_image"]
DiffImageLocation=default_configs["diff_image_location"]

def config(configs=None):
    '''call back function used by config module
    set the global variables according to configuration
    '''
    if configs is None:
        configs = default_configs
    
    global GenDiffImage
    global DiffImageLocation

    GenDiffImage=configs["gen_diff_image"]
    DiffImageLocation=configs["diff_image_location"]

#used by config module
__all__=["config_section", "default_configs", "config"]
    
def query_diff_image_location():
    '''query diff_image_location from config
    '''
    if not os.path.isdir(DiffImageLocation):
        os.makedirs(DiffImageLocation)
        
    return DiffImageLocation
    
def query_gen_diff_image():
    '''query gen_diff_image from config
    '''
    results = {"True":True, "False":False}
    
    if GenDiffImage in results:
        return results[GenDiffImage]
    else:
        #use default
        return results[default_configs["gen_diff_image"]]
