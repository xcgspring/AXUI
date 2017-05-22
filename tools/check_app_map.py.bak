
import os
import sys
try:
    import pyxb
except ImportError:
    print("Need install pyxb first")
    sys.exit(1)
    
from generate_all_schema_modules import generate_module

def check_app_map(xs_module, app_map):
    try:
        app_map_instance = xs_module.CreateFromDocument(app_map)
        print("Check successful")
    except pyxb.UnrecognizedContentError as e:
        print(e.details())
    except pyxb.IncompleteElementContentError as e:
    	print(e.details())
        
if __name__=="__main__":
    print("Usage:\npython %s XSD_file(abs path) app_map_file" % __file__)
    XSD_file = sys.argv[1]
    app_map_file = sys.argv[2]
    XSD_module_name = os.path.basename(XSD_file).split(".")[0]
    XSD_module_dir = os.path.dirname(XSD_file)
    generate_module(XSD_file, XSD_module_name, XSD_module_dir)
    
    sys.path.insert(0, XSD_module_dir)
    XSD_module = __import__(XSD_module_name)
    
    with open(app_map_file) as app_map:
        check_app_map(XSD_module, app_map.read())
    
    

