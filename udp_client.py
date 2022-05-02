'''
Name: udp_client.py
Desc: A UDP client to interact with listener server
Auth: Keiran O'Sullivan
Date: 02/05/2022
'''

import socket
SERVER_NAME = '127.0.0.1' # Server address
SERVER_PORT = 11001 # Server port

CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Create the connection

USER_MESSAGE = input('Please enter a calculation to send to the server:\n') # Get the calculation from the user

CLIENT_SOCKET.sendto(USER_MESSAGE.encode(), (SERVER_NAME, SERVER_PORT)) # Send the calculation the server

MODIFIED_MESSAGE, SERVER_ADDRESS = CLIENT_SOCKET.recvfrom(2048) # get the response

print("\nAnswer:") # Print out the answer
print(MODIFIED_MESSAGE.decode()) # In a nice format
CLIENT_SOCKET.close() # Close the connection
