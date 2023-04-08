import socket

q = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
q.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

q.bind(('localhost', 8004))
print('Quick sort server created...')

q.listen()

def partition(array, low, high):
    pivot = array[high]
    i = low-1
    for j in range(low, high):
        if(array[j] <= pivot):
            i = i+1
            (array[i], array[j]) = (array[j], array[i])
    (array[i+1], array[high]) = (array[high], array[i+1])
    return i+1

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi+1, high)

def handle_connection(connection):
    data = connection.recv(1024)
    array_str = ', '.join(map(str, data)).encode('utf-8')
    array = list(map(int, array_str.decode('utf-8').split(', ')))
    print('Received array:', array)
    quick_sort(array, 0, len(array)-1)
    print('Sorted array:', array)
    sorted_array_str = ', '.join(map(str, array)).encode()
    connection.send(sorted_array_str)

while True:
    connection, client_addr = q.accept()
    handle_connection(connection)

q.close()