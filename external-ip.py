import random
import socket
import requests
#Use the below to get external IP 
def get_external_ip():
    resolvers = [
        'https://ident.me/',
        'https://ifconfig.me/',
        'https://api.ipify.org/',
        'https://ipinfo.io/ip/',
        'https://ipecho.net/plain/',
        'https://ipv4.icanhazip.com/'
    ]
    tries = 0
    while tries < 3:
        try:
            response = requests.get(random.choice(resolvers), timeout=10)
            if response.status_code == 200:
                return response.text.strip()
            raise socket.timeout
        except (requests.exceptions.RequestException, socket.timeout):
            tries += 1
    return "unable to resolve"

print(get_external_ip())
