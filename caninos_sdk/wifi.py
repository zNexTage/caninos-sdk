import socket
import subprocess

class ConnectionInfo:
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"


    def __init__(self):
        self.network_name = None
        self.interface = None
        self.network_type = None        

        info = self.__get_connected_network_info()

        self.network_name = info['network_name']
        self.interface = info['interface']
        self.network_type = info['network_type']        

    def __get_connected_network_info(self):
        ''' run the nmcli command to get the network_name, interface and network_type '''
        
        result = subprocess.run(['nmcli', 'connection', 'show', '--active'], stdout=subprocess.PIPE, text=True)

        output = result.stdout

        lines = output.splitlines()

        # if is disconnected, return None for network_name, interface and network_type.
        if len(lines) <= 1:
            return {
                'network_name': None,
                'interface': None,
                'network_type': None            
                }

        # split the nmcli command result.
        # index 1 contains the values. index 0 contains the headers
        line_infos = lines[1].split()
        
        network_name = line_infos[0]
        network_type = line_infos[2]
        interface = line_infos[3]

        return {
            'network_name': network_name,
            'interface': interface,
            'network_type': network_type            
        }        
        

    @property
    def status(self):
        ''' Returns the connection status.

            returns:
                - connected: when the labrador is connected to the internet;
                - disconnected: when tha labrador is not connected to the internet.
        '''
        if self.__has_internet_connection():            
            return self.CONNECTED
        
        return self.DISCONNECTED
   
        

    @property
    def ip_address(self):
        ''' gets the Labrador IP address '''
        
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            self.__socket_connection(socket=s)

            return s.getsockname()[0]
        
        except socket.error as err:
            return "127.0.0.1"
    
    def __has_internet_connection(self):
        ''' Checks the internet connection. '''
        
        try:            
            # attemps to establish a TCP connection with the Google DNS Server.
            # If it works, it means that the labrador is connected
            # to the internet.
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__socket_connection(s)
            s.close()
            
            return True
        except socket.error as err:
            return False

    def __socket_connection(self, socket, host = '8.8.8.8', port=53, timeout=3):                
        socket.connect((host, port))
        
            
class Wifi:
    ''' Wifi manager '''
    
    def status(self):
        ''' returns the connection information '''
        
        return ConnectionInfo()
