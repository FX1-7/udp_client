'''
Name: udp_client.py
Desc: A UDP client to interact with listener server
Auth: Keiran O'Sullivan
Date: 02/05/2022
'''

import socket
SERVER_NAME = 'localhost'
SERVER_PORT = 11001

CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

USER_MESSAGE = input('Please enter a calculation to send to the server:\n')

CLIENT_SOCKET.sendto(USER_MESSAGE.encode(), (SERVER_NAME, SERVER_PORT))

MODIFIED_MESSAGE, SERVER_ADDRESS = CLIENT_SOCKET.recvfrom(2048)

print(MODIFIED_MESSAGE.decode())
