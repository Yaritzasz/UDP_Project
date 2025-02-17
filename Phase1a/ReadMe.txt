EECE.4830-5830 - Network Design
Phase 1a - UDP message exchange
Yaritza Sanchez

Files Included:
    client_1a.py - UDP client for message exchange
    server_1a.py - UDP server for message exchange
    ReadMe.txt - This file

How to Run the Program

    Start the UDP Server First
          1. Open Command Prompt
          2. Navigate to the project folder:
             cd C:\Users\Yarit\UDP_Project\Phase1a
          3. Run the server:
             python server_1a.py
          Expected output:
             UDP Server is listening on port 20001...

    Start the UDP Client
         1. Open another Command Prompt window
         2. Navigate to the same folder:
            cd C:\Users\Yarit\UDP_Project\Phase1a
         3. Run the client:
            python client_1a.py
         4. Enter a message when prompted:
            Client: "HELLO"
         5. Expected output if working correctly:
            Server: "HELLO"
         6. To end the program, type:
            Client: "bye"
