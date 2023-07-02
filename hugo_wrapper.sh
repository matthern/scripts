#!/bin/bash
#Wrapper for nginx rev proxy URL to output in yaml for hugo static website.
#First script goes though proxy config and puts the URLs into a text file.
python3 /home/matthew/docker-services/scripts/find_proxy_url_uniq.py -d /home/matthew/docker-services/le/config/letsencrypt/nginx/proxy-confs -o /home/matthew/docker-services/scripts/services.txt
#next script will grab that text and put it in YAML format with a name and URL, the name is taken from the url.
python3 /home/matthew/docker-services/scripts/prox-2-hugo.py /home/matthew/docker-services/scripts/services.txt /home/matthew/docker-services/hugo/test/data/services_no_desc.yaml 
#Next script will add descriptions from the docker inspect command for those services that are running in docker and have a description label.
python3 /home/matthew/docker-services/scripts/add_descriptions.py -i /home/matthew/docker-services/hugo/test/data/services_no_desc.yaml -o /home/matthew/docker-services/hugo/test/data/services_docker_desc.yaml 
#Adding some hardcoded descriptions for services that are not run in containers to the parsed file
python3 /home/matthew/docker-services/scripts/merge_yaml.py -i /home/matthew/docker-services/hugo/test/data/services_docker_desc.yaml -a /home/matthew/docker-services/scripts/additional.yaml -o /home/matthew/docker-services/hugo/test/data/services.yaml
#after this has been done check services for missing descriptions.
python3 /home/matthew/docker-services/scripts/check_missing_desc.py -i /home/matthew/docker-services/hugo/test/data/services.yaml 
    



