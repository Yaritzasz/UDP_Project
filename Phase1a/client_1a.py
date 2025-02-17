import socket

# Server details for connection
server_details = ("127.0.0.1", 20001)

# Buffer size for receiving input
buffer_size = 1024

# Creation of client socket
client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Infinite loop for continuous message sending and receiving
while True:
    # Input the message from client side
    msg = input("Client: ")

    # Encode the input message
    msg_bytes = msg.encode()

    # Send the encoded message
    client_socket.sendto(msg_bytes, server_details)

    # If the message is bye in any form break the loop close the application
    if msg == "bye" or msg == "Bye" or msg == "BYE":
        break

    # Or receive the reply form server and display
    msg_server = client_socket.recvfrom(buffer_size)

    msg_server = msg_server[0].decode()

    print("Server :", msg_server)

# Close the socket
client_socket.close()