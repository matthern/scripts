import argparse
import re
import os

parser = argparse.ArgumentParser(description='Extract server names from .conf files')
parser.add_argument('-d', '--directory', type=str, required=True, help='Directory to search for .conf files')
parser.add_argument('-o', '--output', type=str, required=True, help='Output file name')

args = parser.parse_args()

output_file = open(args.output, "w")

for root, dirs, files in os.walk(args.directory):
    for file in files:
        if file.endswith(".conf"):
            with open(os.path.join(root, file), "r") as conf_file:
                for line in conf_file:
                    match = re.search(r'server_name\s+(.+)', line)
                    if match:
                        output_file.write(match.group(1) + "\n")

output_file.close()

