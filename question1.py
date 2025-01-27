# import three modules: sys (helps to interact with the Python environment), glob (filename pattern matching), os (lets you interact with the operating system)
import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# Use the glob.glob() function (imported via glob module) to get the list of filenames in the directory
file_list = glob.glob(pattern)

# Use a foreach style loop with the os.path.getsize() to find each file's size
for filename in file_list:
    file_size = os.path.getsize(filename)

    # Specify that only files that are greater than zero in length can be displayed
    if file_size > 0:

        # Then remove the leading directory name(s) from each filename by using os.path.basename()
        filename = os.path.basename(filename)

        # Use an f-string to print the final output: each filename and its size
        print(f"{filename}: {file_size} bytes")