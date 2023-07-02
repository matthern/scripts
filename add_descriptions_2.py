import yaml
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Update service descriptions in YAML file based on Docker container metadata')
parser.add_argument('-i', '--input', type=str, required=True, help='Input YAML file')
parser.add_argument('-o', '--output', type=str, required=True, help='Output YAML file')
args = parser.parse_args()

# Load the YAML file
with open(args.input, 'r') as file:
    services_data = yaml.safe_load(file)

# Loop through the services
for service in services_data['Services']:
    service_name = service['name']
    service_url = service['url']

    # Search for containers that contain the service name
    process = subprocess.Popen(['docker', 'ps', '--format', '{{.Names}}'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    containers = output.decode().splitlines()

    matching_containers = [container for container in containers if service_name.lower() in container.lower()]

    if matching_containers:
        # Get the description from the container's metadata
        container_names = ', '.join(matching_containers)
        process = subprocess.Popen(['docker', 'inspect', '--format', '{{index .Config.Labels "org.opencontainers.image.description"}}', *matching_containers], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        descriptions = output.decode().splitlines()

        # Remove duplicate descriptions
        descriptions = list(set(descriptions))

        # Update the service dictionary with the description
        if 'description' in service:
            existing_description = service['description']
            new_descriptions = [desc for desc in descriptions if desc not in existing_description]
            service['description'] += ', ' + ', '.join(new_descriptions)
        else:
            service['description'] = ', '.join(descriptions)

# Write the updated YAML file
with open(args.output, 'w') as file:
    yaml.dump(services_data, file)

print("Descriptions updated successfully!")

