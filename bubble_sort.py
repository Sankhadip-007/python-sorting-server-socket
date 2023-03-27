def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

import socket
b = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b.bind(('127.0.0.1', 8001))
print('Bubble sort server created...')
# Listen for incoming connections
b.listen(1)
def handle_connection(connection):
    data = connection.recv(1024)
    array_str = ','.join(map(str, data)).encode('utf-8') 
    array = list(map(int, array_str.decode('utf-8').split(',')))
    print('Received array:', array)
    # Sort the array using Bubble Sort
    sorted_array = bubble_sort(array)

    # Convert the sorted array to a string and encode it
    sorted_array_str = ','.join(map(str, sorted_array)).encode()

    # Send the sorted array back to the central server
    connection.send(sorted_array_str)


# Start the server and listen for incoming connections
while True:
    connection, client_address = b.accept()
    handle_connection(connection)

# Close the server socket
b.close()