import yaml
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Merge YAML files with hardcoded changes')
parser.add_argument('-i', '--input', type=str, required=True, help='Input YAML file')
parser.add_argument('-a', '--additional', type=str, required=True, help='Additional YAML file')
parser.add_argument('-o', '--output', type=str, required=True, help='Output YAML file')
args = parser.parse_args()

# Load the original YAML file
with open(args.input, 'r') as file:
    original_data = yaml.safe_load(file)

# Load the additional YAML file with hardcoded changes
with open(args.additional, 'r') as file:
    additional_data = yaml.safe_load(file)

# Merge the data from the additional YAML file into the original data
for additional_service in additional_data:
    service_name = additional_service['name']

    # Find the matching service in the original data
    for service in original_data['Services']:
        if service['name'] == service_name:
            # Update the fields with the hardcoded changes
            service.update(additional_service)
            break

# Write the updated YAML file
with open(args.output, 'w') as file:
    yaml.dump(original_data, file)

print("YAML files merged successfully!")

