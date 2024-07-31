import caninos_sdk as k9

labrador = k9.Labrador()

info = labrador.wifi.status()

print(info.status)
print(info.ip_address)
print(info.network_name)
print(info.interface)
