import os
import re

# script to update all ngnix rev proxy conf files to add authelia lines. 

# Set conf_dir to the current working directory
conf_dir = os.getcwd()

# Compile regular expressions for matching the include directives
#'r' for rawstring. 
server_regex = re.compile(r'^\s*include /config/nginx/authelia-location\.conf;\s*$', re.MULTILINE)
location_regex = re.compile(r'^\s*include /config/nginx/authelia-authrequest\.conf;\s*$', re.MULTILINE)

# Iterate over all files in the conf_dir directory
for filename in os.listdir(conf_dir):
    # Skip files that are not .conf files
    if not filename.endswith('.conf'):
        continue

    # Read the contents of the file
    with open(os.path.join(conf_dir, filename), 'r') as f:
        contents = f.read()

    print(f'Would have been Processing file: {filename}')
    
    # Check if the include directive is present in the server block
    if not server_regex.search(contents):
        # The include directive is not present, so add it to the file
        contents = contents.replace('server {', 'server {\ninclude /config/nginx/authelia-location.conf;', 1)
        print(f'Would have Added include directive to server block in file: {filename}')
    else:
        print(f'Would have Skipping server location block of {filename}')

    # Check if the include directive is present in the location block
    if not location_regex.search(contents):
        # The include directive is not present, so add it to the file
        contents = contents.replace('location / {', 'location / {\n\tinclude /config/nginx/authelia-authrequest.conf;', 1)
        print(f'Would have Added include directive to location block in file: {filename}')
    else:
        print(f'Would have Skipping location block of {filename}')

    # Write the modified contents back to the file
    #with open(os.path.join(conf_dir, filename), 'w') as f:
    #   f.write(contents)
