import os
import sys

#filters = ['migration', 'test']
filters = []

def file_lines(fname):
    try:
        i=0
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1
    except:
        return 0

# find all files in a directory with extension recursively
def count_files(dir, filters, print_file_count, print_directory_count, first_caller):
    count = 0
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            if name.endswith('.py') and "test" not in file_path and "migration" not in file_path:
                file_count = file_lines(file_path)
                count += file_count
                if print_file_count:
                    print("{} : {}".format(file_path,file_count))
        for name in dirs:
            folder_path = os.path.join(root, name)
            directory_count = count_files(folder_path, filters, print_file_count, print_directory_count, False)
            if first_caller and print_directory_count and folder_path.count("/") < 2:
                print("{} : {}".format(os.path.join(root, name), directory_count))
        
    return count

directory = len(sys.argv) > 1 and sys.argv[1] or "./"

print("Scanning {}...".format(directory))
print(count_files(directory, filters, False, True, True))

