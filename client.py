import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
c.connect(('localhost', 8000))

# Read the sorting type and array from a text file
# with open('input.txt', 'rb') as f:
#     sorting_data = f.read()
#     c.sendall(sorting_data)
arr=input('Enter array values: ')
sorting_type=input('Enter sorting type(merge/quick/bubble): ')
with open('input.txt', 'w+') as f:
     f.write(sorting_type)
     f.write('\n')
     f.write(arr)
     f.close()

with open('input.txt', 'rb') as f:
     sorting_data = f.read()
     c.sendall(sorting_data)
# Receive the sorted array txt from the central server

l = c.recv(1024)
print(l)
with open('output.txt', 'wb') as f:
    while l:
        f.write(l)
        l = c.recv(1024)
        if not l:
            break

# Close the client socket
c.close()
