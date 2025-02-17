import socket

IP = "127.0.0.1"
Port = 20001
buffer_size = 1024

# Creation of UDP socket
server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind the socket with the provided IP and PORT
server_socket.bind((IP, Port))

print(f"UDP Server is listening on port {Port}...")

# We would be keep receiving the messages so an infinite loop is required
while True:

    # Receive the data from the socket
    received_data = server_socket.recvfrom(buffer_size)

    # The received data is in bytes format, we need to decode is
    message = received_data[0]

    address = received_data[1]

    # Decoded message
    message_recv = message.decode()

    # Application is configured in a way , such that when client send bye the program ends on both the sides
    if message_recv == "bye" or message_recv == "Bye" or message_recv == "BYE":
        break

    # Print the Client received messages
    print("Client: " + message_recv)

    # Input the messages from server side.
    msg = input("Server: ")

    # Encode the message
    msg_to_bytes = msg.encode()

    # Send a reply to client
    server_socket.sendto(msg_to_bytes, address)

# Close the socket in the end
server_socket.close()