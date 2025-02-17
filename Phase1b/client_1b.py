import socket
import os

# Server details
server_address = ("127.0.0.1", 20002)
buffer_size = 1024  # Define packet size

def udp_file_sender(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sequence_number = 0  # Start sequence at 0

    with open(file_path, "rb") as file:
        while True:
            data = file.read(buffer_size)
            if not data:
                break
            # Attach sequence number (RDT 1.0 does not need ACKs)
            packet = f"{sequence_number:08d}".encode() + data
            client_socket.sendto(packet, server_address)
            sequence_number += 1  # Increment sequence number

    # Send END signal to indicate transfer is complete
    client_socket.sendto(b"END", server_address)

    print("File sent successfully!")
    client_socket.close()

if __name__ == "__main__":
    udp_file_sender("test.bmp")
