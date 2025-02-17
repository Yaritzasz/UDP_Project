import os
import hashlib

def compute_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

# Paths to the files (update if necessary)
original_file = "C:/Users/Yarit/UDP_Project/Phase1b/test.bmp"
received_file = "C:/Users/Yarit/UDP_Project/Phase1b/received.bmp"

# Check file sizes
if os.path.exists(original_file) and os.path.exists(received_file):
    print(f"Original File Size: {os.path.getsize(original_file)} bytes")
    print(f"Received File Size: {os.path.getsize(received_file)} bytes")
else:
    print("Error: One or both files not found!")

# Compute hashes
if os.path.exists(original_file) and os.path.exists(received_file):
    print(f"MD5 Hash of Original File: {compute_md5(original_file)}")
    print(f"MD5 Hash of Received File: {compute_md5(received_file)}")
else:
    print("Error: One or both files not found!")
