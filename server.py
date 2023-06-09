import socket
import threading

host = 'localhost'
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to a specific IP address and port
s.bind((host, port))
s.listen()
print(f'Server created and listening at {port}')

def handle_connection(connection, addr):
    data = connection.recv(1024)
    sorting_type, array_str = data.decode('utf-8').split('\n')
    sorting_type = sorting_type.strip()
    print('Array received from client. Connecting to sorting server...')
    # Send the array to the appropriate sorting server
    sorted_array = send_to_sorting_server(sorting_type, array_str)
    print('Array sorted. Sending to client...')
    with open('server_processing.txt', 'wb') as f1:
        f1.write(sorted_array)
    with open('server_processing.txt', 'rb') as f1:
        l = f1.read()
        connection.send(l)
    f1.close()
    connection.close()
    print('Connection closed to', addr)

def send_to_sorting_server(sorting_type, array):
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print('Sorting type:',sorting_type)
    if sorting_type == 'bubble':
        s1.connect(('localhost', 8001))
        print('Connected to bubble sort server')
        s1.send(array.encode('utf-8'))
        sorted_array = s1.recv(1024)
        return sorted_array
    elif sorting_type == 'selection':
        s1.connect(('localhost', 8002))
        print('Connected to selection sort server')
        s1.send(array.encode('utf-8'))
        sorted_array = s1.recv(1024)
        return sorted_array
    elif sorting_type == 'merge':
        s1.connect(('localhost', 8003))
        print('Connected to merge sort server')
        s1.send(array.encode('utf-8'))
        sorted_array = s1.recv(1024)
        return sorted_array
    elif sorting_type == 'quick':
        s1.connect(('localhost', 8004))
        print('Connected to quick sort server')
        s1.send(array.encode('utf-8'))
        sorted_array = s1.recv(1024)
        return sorted_array
    else:
        print('Invalid algorithm')
    # Close the connection to the sorting server
    s1.close()

# Start the server and listen for incoming connections
while True:
    connection, client_address = s.accept()
    print('Client with address', client_address, 'connected')
    thread = threading._start_new_thread(handle_connection, (connection, client_address))

s.close()
