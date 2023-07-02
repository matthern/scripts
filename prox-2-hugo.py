import argparse
import yaml

# Create argument parser
parser = argparse.ArgumentParser(description="Convert service info to URLs")
parser.add_argument("input_file", help="Input file containing service information")
parser.add_argument("output_file", help="Output file for generated URLs")
args = parser.parse_args()

# Read input file
with open(args.input_file, "r") as file:
    output = file.read()

# Process service information
services = []
for entry in output.split('\n'):
    entry = entry.strip()
    if entry:
        if not entry.endswith('.mcgovern.network'):
            entry += '.mcgovern.network'
        service_name = entry.split('.')[0]
        url = f"https://{entry.split('.')[0]}.mcgovern.network"
        service = {'name': service_name, 'url': url}
        services.append(service)

# Sort services alphabetically by name
services.sort(key=lambda s: s['name'])


# Prepare data for YAML output
data = {'Services': services}

# Write data to output YAML file
with open(args.output_file, 'w') as file:
    yaml.dump(data, file)

print(f"Generated URLs written to: {args.output_file}")

