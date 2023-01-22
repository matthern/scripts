import os
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser()

# add the directory argument
parser.add_argument('directory', help='path to the directory containing the files')

# parse the command-line arguments
args = parser.parse_args()

# get the directory path from the command-line arguments
directory = args.directory

# get a list of all files in the directory
files = os.listdir(directory)

# iterate through the files
for file in files:
    # construct the path to the file
    file_path = os.path.join(directory, file)

    # check if the file is a regular file (not a directory)
    if os.path.isfile(file_path):
        # get the file name without the extension
        file_name, file_ext = os.path.splitext(file)
        # construct the path to the new directory using the file name
        dir_path = os.path.join(directory, file_name)
        # create the directory
        os.mkdir(dir_path)
        # construct the path to the new file location
        new_file_path = os.path.join(dir_path, file)
        # move the file to the new location
        os.rename(file_path, new_file_path)

