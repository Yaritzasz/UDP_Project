import socket

server_address = ("127.0.0.1", 20002)
buffer_size = 1032  # 1024 bytes + 8 for sequence number

def udp_file_receiver(output_file="received.bmp"):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(server_address)

    print(f"Server listening on {server_address[0]}:{server_address[1]}")

    with open(output_file, "wb") as file:
        while True:
            data, addr = server_socket.recvfrom(buffer_size)
            if data == b"END":
                break  # Stop receiving when END signal is detected


            file.write(data[8:])  # Write only the file data

    print(f"File received successfully! Saved as {output_file}")
    server_socket.close()

if __name__ == "__main__":
    udp_file_receiver()
