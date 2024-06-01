import ipaddress
import requests
import ipinfo

ip = ipaddress.ip_address('192.0.2.1')
# not_ip = ipaddress.ip_address('192.1.2.256')

ip_global = ipaddress.ip_address('192.168.1.2')
# print(ip_global.is_global)

# network = ipaddress.ip_network('192.0.2.0/28')

# network = ipaddress.ip_network('192.0.2.0/28')
# for host in network.hosts():
#     print(host)



def is_vpn_or_proxy(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    data = response.json()
    return data.get('vpn', False) or data.get('proxy', False)

print(is_vpn_or_proxy('192.168.1.2'))
