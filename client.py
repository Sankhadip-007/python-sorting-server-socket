import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 8000))

# Read the sorting type and array from a text file
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

# Close the client socket
c.close()
