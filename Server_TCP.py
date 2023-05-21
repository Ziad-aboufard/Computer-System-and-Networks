from socket import AF_INET, SOCK_STREAM, socket
from time import sleep
from os import getpid
if __name__ == '__main__':
    print('Application started')
    print('Os assigned process id: %d' %getpid())
    
    s = socket(AF_INET, SOCK_STREAM)
    print('TCP Socket created')
    print('File descriptor assigned by OS:', s.fileno())
    s.bind(('127.0.0.1', 7779))
    print('socket is bound to %s:%d' % s.getsockname())
    backlog = 0 
    s.listen(backlog)
    print('socket is in listening state to %s:%d' % s.getsockname())
    client_socket,client_addr = s.accept()
    print('New client connected from %s:%d' % client_addr)
    print('Local end-point socket bound on: %s:%d'% client_socket.getsockname())
    recv_buffer_length = 1024
    message = client_socket.recv(recv_buffer_length)
    print('Recieved %d bytes from %s:$%d' % ( (len(message),)+client_addr))
    print('Received message: \n%s' %message)
    
    b= message
    print(b.upper())
    print('length of the message:' , len(message))
    
   
    
    input('press Enter to terminate....')
    wait_secs = 5
    print('Waiting %d seconds before termination ...' %wait_secs)
    sleep(wait_secs)
    print('Closing the TCP socket...')
    s.close()
    print('terminating....')