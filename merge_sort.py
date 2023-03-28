import socket
# Set up the socket for the server
m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
m.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to a specific IP address and port
m.bind(('127.0.0.1', 8003))
print('Merge sort server created...')
# Listen for incoming connections
m.listen(1)

"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # sort each half recursively
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    # merge the sorted halves
    merged = []
    i = j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        elif left_sorted[i] > right_sorted[j]:
            merged.append(right_sorted[j])
            j += 1
        else:
            merged.append(left_sorted[i])
            i += 1
            j += 1 
    # append any remaining elements
    merged += left_sorted[i:]
    merged += right_sorted[j:]
    return merged
"""

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
    array_str = ','.join(map(str, data)).encode('utf-8')
    array = list(map(int, array_str.decode('utf-8').split(',')))
    print('Received array:', array)
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
