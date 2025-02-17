EECE.4830-5830 - Network Design
Phase 1b - UDP File Transfer with RDT 1.0
Author: Yaritza Sanchez

Files Included:
    client_1b.py - UDP file sender
    server_1b.py - UDP file receiver
    test.bmp - Sample BMP file for transfer
    received.bmp - File received at the server
    check_file_integrity.py - File verification script
    ReadMe.txt - This file


How to Run the Program

    Start the UDP server
        1. Open Command Prompt
        2. Navigate to the project folder:
            cd C:\Users\Yarit\UDP_Project\Phase1b
        3. Run the server:
            python server_1b.py
        Expected Output:
            Server listening on 127.0.0.1:12345

    Start the UDP Client
     1. Open another Command Prompt window
     2. Navigate to the same folder:
        cd C:\Users\Yarit\UDP_Project\Phase1b
     3. Run the client:
        python client_1b.py
     Expected Output:
        File sent successfully!

    How to Verify File Transfer Integrity
        1. Run the following script:
            python check_file_integrity.py
        2. Expected output if the transfer is correct:
            Original File Size: 518456 bytes
            Received File Size: 518456 bytes
            MD5 Hash of Original File: 6dd901fa155974e6fb7d2a043d2e8088
            MD5 Hash of Received File: 6dd901fa155974e6fb7d2a043d2e8088




