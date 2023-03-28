import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 8002))
print('Selection sort server created...')
# Listen for incoming connections
s.listen(1)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Define a function to handle incoming connections
def handle_connection(connection):
    # Receive the data from the central server
    data = connection.recv(1024)
    array_str = ','.join(map(str, data)).encode('utf-8')
    array = list(map(int, array_str.decode('utf-8').split(',')))
    print('Received array:', array)
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
