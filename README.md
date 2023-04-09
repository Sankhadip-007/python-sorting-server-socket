# python-sorting-server-socket
# Introduction:

The given project is a distributed server application written in Python. It consists of a client program, a central server that handles exchange of information between the client program and the distributed servers. It uses concept of socket programming and various other sorting algorithms namely: Bubble Sort, Selection Sort, Merge Sort and Quick Sort. It also uses the concept of file handling, since the input and output are passed in the form of text files. The server supports multithreading.

# Approach:

The approach to the project is as follows:

-   The client program (client.py) accepts an integer array and the type of sorting to be performed from the user.
    
-   It then writes the sorting algorithm name and the integer array into the file ‘input.txt’.
    
-   The client program then reads ‘input.txt’ line by line and sends the data to the central server program using the socket link that has already been established.
    
-   The server program (server.py) runs the function `handle_connection(connection, addr)` which runs multiple threads for the client program.
    
-   The central server (server.py) then reads the sorting type and the array that has been sent by the client and passes this array to a function `send_to_sorting_server(sorting_type, array_str).` Note that the array is still in string form.
    
-   The function send_to_sorting_server(sorting_type, array_str) then uses if-elif statements to select the appropriate sorting server among the 4 distributed servers. After selecting, it then sends the array (in string form) to the respective sorting server using a new socket connection.
    
-   Every sorting server (bubble_sort.py, selection_sort.py, merge_sort.py and quick_sort.py) has a function `handle_connection(connection)` that receives the array in string form from central server and converts it into an array of integers using the list(map(int, data.split(‘,’))) function.
    
-   Then sorting is performed on the integer array. The sorted array is converted into string form using ‘,’.join() function and sent back to the central server using the same socket connection.
    
-   The central server then writes the sorted array into a temporary file named ‘server_processing.txt’. It then reads this file line by line and sends it back to the client program.
    
-   The client receives the sorted array and writes this array into the file ‘output.txt’.
    
-   The contents of ‘output.txt’ are then printed out into the terminal for the user to see.

# How to Use:

 -   Clone the repository to your own machine.
    
 - Open 6 terminals simultaneously and run the following commands in
   them:
   
   -   `python bubble_sort.py`
   
   -   `python selection_sort.py`
   
   -   `python merge_sort.py`
   
   -   `python quick_sort.py`
   
   -   `python server.py`
   
   -   `python client.py`

    

-   In client.py, enter the array separating each element by comma (,).
    
-   Enter the type of sorting algorithm you want to use, i.e., bubble, selection, merge or quick.
    
-   Press enter. You should now see the sorted array on your terminal.
    
-   You can check the files input.txt and output.txt for verification.

# Output:

server and client:

![](https://lh4.googleusercontent.com/RzvYgEl4cRUZrh64L5msCvmE9Ps0DIGQc9ET0QWtSUuLZlb8oxF5NKff3jihhOA9d0DmRmGjCe7xkoSvL3RO8_ErndJZRSREd6mwUpGuAadDc-2duFUWUDuKOkkD77ZGiR1QIOm5RYeViRWx2SE93sY)

  

bubble and selection sort:

![](https://lh6.googleusercontent.com/ILyZpX4AHjD9-WYhwsT-WPkf-ftJyGQV7_Y-z7_mKc9WZt7YWOskr7geQ6vuEl-Muzw5ktgkew8Z-86BsUV6Yi9LDwfVz7_1vm5_V6c_KcraOXYQaUwqgOQdP_eXzkWVf4CUP0cQoApcPPAaXjau07k)

  

merge and quick sort:

![](https://lh6.googleusercontent.com/_LZK6cuoHHsMv3iVc8rB0SHctnCiiBaqmWiOCT5BRIG0xWkcxyQXy7w4kRiuwVZrY40C6PlNbVyrKMRldvK_wjZPc1Xf2wUlsz640vqDqRBAUymBT1JBslu55AL9_ob7eNxQdh8oPGLyMt7kZIdcUFc)

  

input.txt and output.txt:

![](https://lh3.googleusercontent.com/fRsTrHladVN9k7Tymzz9DmScgnp0Xc_blAFSsM5_q8a6K0mW_VD2WP2gVgLFPOM_dqTy_Ykz08CEV3prPWFD33fxzl66KoxJDpeBkSItZmmDEBowy7-1_n1GrLYopLY7JnqGC1aCNB4tUCn90Go8g58).![](https://lh3.googleusercontent.com/lW8k5d0bdEHeBzFEgqMlezfYi4iGxV6VoPa7CLveoiRK7q5AQpGGXwAwwMqOR7Gbhu98xAaeYg4tf4A4cmWsQTG8uq-GdOM_0115LD7SACOqs1Pb2l8Hga_AXtm0gIGauWcgklDZPCftOB2WmnNLjuA)
