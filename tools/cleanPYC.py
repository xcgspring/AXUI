
import re
import os
import sys

print("%s path\n" % sys.argv[0])

path = sys.argv[1]

for root, dirs, files in os.walk(path):
    for file_ in files:
        if re.match(".*.pyc$", file_):
            abs_file = os.path.join(root, file_)
            print("Clean %s" % abs_file)
            os.remove(abs_file)
