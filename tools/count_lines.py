
import os
test_dir = "../AXUI"
total_lines = 0
for _root, _dirs, _files in os.walk(test_dir):
    for _file in _files:
        file_lines = sum(1 for line in open(os.path.join(_root, _file)))
        total_lines += file_lines

print(("total lines: %d" % total_lines))
