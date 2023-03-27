def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

import socket

# Set up the socket for the server
m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
m.bind(('127.0.0.1', 8003))
print('Merge sort server created...')

# Listen for incoming connections
m.listen(1)

# Define a function to handle incoming connections
def handle_connection(connection):
    # Receive the data from the central server
    data = connection.recv(1024)

    # Parse the data to extract the sorting type and the array to be sorted
    sorting_type, array = data.decode().split('\n')
    array = list(map(int, array.split(',')))

    # Sort the array using Merge Sort
    sorted_array = merge_sort(array)

    # Convert the sorted array to a string and encode it
    sorted_array_str = ','.join(map(str, sorted_array)).encode()

    # Send the sorted array back to the central server
    connection.send(sorted_array_str)

# Start the server and listen for incoming connections
while True:
    connection, client_address = m.accept()
    handle_connection(connection)

# Close the server socket
m.close()
