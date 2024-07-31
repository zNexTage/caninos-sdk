import caninos_sdk as k9

labrador = k9.Labrador()


print(labrador.wifi.status)
print(labrador.wifi.ip_address)
print(labrador.wifi.network_name)
print(labrador.wifi.interface)
