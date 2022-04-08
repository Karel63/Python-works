from ipaddress import IPv4Network
ipv = IPv4Network(input("Zadejte adresu: "))
print(ipv)
print("Síť: ", ipv.network_address)
print("Maska: ", ipv.netmask)
print("Broadcast: ", ipv.broadcast_address)
print("Adresy: ", ipv.num_addresses)
print("Hosti: ", ipv.num_addresses - 2)

#Uděláno s pomocí stránky: https://realpython.com/python-ipaddress-module/
