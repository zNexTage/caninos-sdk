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
    
    def __has_internet_connection(self, host="8.8.8.8", port=53, timeout=3):
        ''' Checks the internet connection. '''
        
        try:
            socket.setdefaulttimeout(timeout)

            # attemps to establish a TCP connection with the Google DNS Server.
            # If it works, it means that the labrador is connected
            # to the internet.
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error as err:
            return False
