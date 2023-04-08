import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
c.connect(('localhost', 8000))

arr = input("Enter the array: ")
sort_type = input("Enter the sorting type: ")

with open('input.txt', 'w+') as f:
    f.write(sort_type)
    f.write('\n')
    f.write(arr)

with open('input.txt', 'rb') as f:
    sorting_data = f.read()
    c.sendall(sorting_data)
# Receive the sorted array txt from the central server

l = c.recv(1024)
with open('output.txt', 'wb') as f:
    while l:
        f.write(l)
        l = c.recv(1024)
        if not l:
            break

with open('output.txt', 'r') as f:
    l = f.read()
    arr = list(map(int, l.split(', ')))
    print("The sorted array: ", arr)

# Close the client socket
c.close()
