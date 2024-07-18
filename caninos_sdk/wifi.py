import socket

class ConnectionInfo:
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"

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
        
            
