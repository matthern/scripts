import yaml
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Check missing services without container or description')
parser.add_argument('-i', '--input', type=str, required=True, help='Input YAML file')
args = parser.parse_args()

# Load the YAML file
with open(args.input, 'r') as file:
    services_data = yaml.safe_load(file)

# Create an empty list to store services without container or description
missing_services = []

# Loop through the services
for service in services_data['Services']:
    service_name = service['name']
    service_url = service['url']

    # Search for containers that contain the service name
    process = subprocess.Popen(['docker', 'ps', '--format', '{{.Names}}'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    containers = output.decode().splitlines()

    matching_containers = [container for container in containers if service_name.lower() in container.lower()]

    if not matching_containers or not service.get('description'):
        missing_services.append(service_name)

# Print the list of services without container or description
print("Services without container or description:")
for service_name in missing_services:
    print(service_name)

