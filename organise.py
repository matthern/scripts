import os

# specify the directory containing the files
directory = '/home/matthew/docker-services/scripts/test'

# get a list of all files in the directory
files = os.listdir(directory)

# iterate through the files
for file in files:
    # construct the path to the file
    file_path = os.path.join(directory, file)

    # check if the file is a regular file (not a directory)
    if os.path.isfile(file_path):
        # construct the path to the new directory
        dir_path = os.path.join(directory, file + '_folder')
        # create the directory
        os.mkdir(dir_path)
        # construct the path to the new file location
        new_file_path = os.path.join(dir_path, file)
        # move the file to the new location
        os.rename(file_path, new_file_path)
