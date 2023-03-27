def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8002))

# Listen for incoming connections
s.listen(1)
print('Selrction sort server created...')

# Define a function to handle incoming connections
def handle_connection(connection):
    # Receive the data from the central server
    data = connection.recv(1024)

    # Parse the data to extract the sorting type and the array to be sorted
    sorting_type, array = data.decode().split('\n')
    array = list(map(int, array.split(',')))

    # Sort the array using Selection Sort
    sorted_array = selection_sort(array)

    # Convert the sorted array to a string and encode it
    sorted_array_str = ','.join(map(str, sorted_array)).encode()

    # Send the sorted array back to the central server
    connection.send(sorted_array_str)

# Start the server and listen for incoming connections
while True:
    connection, client_address = s.accept()
    handle_connection(connection)

# Close the server socket
s.close()
