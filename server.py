import socket
import threading

host = 'localhost'
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to a specific IP address and port
s.bind((host, port))
s.listen(1)
print(f'Server created and listening at {port}')

def handle_connection(connection):
    data = connection.recv(1024)
    sorting_type, array_str = data.decode('utf-8').split('\n')
    sorting_type = sorting_type.strip()
    array_to_sort = list(map(int, array_str.split(',')))

    print('sorting type:', sorting_type, 'size:', len(sorting_type))

    print('array:', array_to_sort)
    # Send the array to the appropriate sorting server
    sorted_array = send_to_sorting_server(sorting_type, array_to_sort)
    print('sorted array:', sorted_array)
    with open('server_processing.txt', 'wb') as f1:
        f1.write(sorted_array)
    with open('server_processing.txt', 'rb') as f1:
        l = f1.read()
        connection.send(l)
    connection.close()
    s.close()

def send_to_sorting_server(sorting_type, array):
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('sorting type:',sorting_type)
    if sorting_type == 'bubble':
        s1.connect(('127.0.0.1', 8001))
        print('Connected to bubble sort server')
        s1.send(bytes(array))
        sorted_array = s1.recv(1024)
        return sorted_array
    elif sorting_type == 'selection':
        s1.connect(('127.0.0.1', 8002))
        print('Connected to selection sort server')
        s1.send(bytes(array))
        sorted_array = s1.recv(1024)
        return sorted_array
    elif sorting_type == 'merge':
        s1.connect(('127.0.0.1', 8003))
        print('Connected to merge sort server')
        s1.send(bytes(array))
        sorted_array = s1.recv(1024)
        return sorted_array
    elif sorting_type == 'quick':
        s1.connect(('127.0.0.1', 8004))
        print('Connected to quick sort server')
        s1.send(bytes(array))
        sorted_array = s1.recv(1024)
        return sorted_array
    else:
        print('Invalid alogorithm')
    # Close the connection to the sorting server
    s1.close()


# Start the server and listen for incoming connections
while True:
    connection, client_address = s.accept()
    print(client_address)
    thread = threading._start_new_thread(handle_connection,(connection,))

# Close the server socket
s.close()
