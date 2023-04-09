import socket
# Set up the socket for the server
m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
m.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to a specific IP address and port
m.bind(('localhost', 8003))
print('Merge sort server created...')
# Listen for incoming connections
m.listen()

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)

# Define a function to handle incoming connections
def handle_connection(connection):
    # Receive the data from the central server
    data = connection.recv(1024)
    array = list(map(int, data.decode('utf-8').split(',')))
    print('Received array:', array)
    # Sort the array using Merge Sort
    sorted_array = merge_sort(array)
    print('Sorted array:', sorted_array)
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
