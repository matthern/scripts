import argparse
import re
import os

parser = argparse.ArgumentParser(description='Extract server names, IP addresses, and ports from .conf files')
parser.add_argument('-d', '--directory', type=str, required=True, help='Directory to search for .conf files')
parser.add_argument('-o', '--output', type=str, required=True, help='Output file name')

args = parser.parse_args()

output_file = open(args.output, "w")

ip_port_set = set()  # to store unique IP address and port combinations

for root, dirs, files in os.walk(args.directory):
    for file in files:
        if file.endswith(".conf"):
            with open(os.path.join(root, file), "r") as conf_file:
                for line in conf_file:
                    server_name_match = re.search(r'server_name\s+(.+)', line)
                    if server_name_match:
                        output_file.write("Server Name: " + server_name_match.group(1) + "\n")
                    ip_port_match = re.search(r'http://([\d\.]+):(\d+)', line)
                    if ip_port_match:
                        ip_address = ip_port_match.group(1)
                        port = ip_port_match.group(2)
                        if (ip_address, port) not in ip_port_set:
                            output_file.write("IP Address: " + ip_address + "\n")
                            output_file.write("Port: " + port + "\n" + "\n")
                            ip_port_set.add((ip_address, port))

output_file.close()

