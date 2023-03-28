import os
import argparse

# create an ArgumentParser object
parser = argparse.ArgumentParser()

# add the directory argument
parser.add_argument('directory', help='path to the directory containing the files')
parser.add_argument('start_name', help='start of the name of the file')
parser.add_argument('end_name', help='end of the name of the file')
parser.add_argument('-f', '--file', help='name of the file to be processed')

# parse the command-line arguments
args = parser.parse_args()

# get the directory path from the command-line arguments
directory = args.directory
start_name = args.start_name
end_name = args.end_name
file_name = args.file

# check if the file argument is provided
if file_name:
    # construct the path to the file
    file_path = os.path.join(directory, file_name)

    # check if the file is a regular file (not a directory)
    if os.path.isfile(file_path):
        # extract the new name for the file
        new_file_name = file_name.split(start_name)[-1]
        new_file_name = new_file_name.split(end_name)[-1]
        new_file_name = new_file_name.strip()
        # construct the path to the new file location
        new_file_path = os.path.join(directory, new_file_name)
        # rename the file
        os.rename(file_path, new_file_path)
else:
    # get a list of all files in the directory
    files = os.listdir(directory)

    # iterate through the files
    for file in files:
        # construct the path to the file
        file_path = os.path.join(directory, file)

        # check if the file is a regular file (not a directory)
        if os.path.isfile(file_path):
            # extract the new name for the file
            new_file_name = file.split(start_name)[-1]
            new_file_name = new_file_name.split(end_name)[-1]
            new_file_name = new_file_name.strip()
            # construct the path to the new file location
            new_file_path = os.path.join(directory, new_file_name)
            # rename the file
            os.rename(file_path, new_file_path)
