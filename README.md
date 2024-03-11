# Blockchain Mining System

This is a simple blockchain mining system that allows clients to request new blocks and start mining, as well as request the blockchain from the block creator server.

## Steps to Run the Application

### Requirements

Make sure you have Python 3 installed on your computer.

### 1. Download Source Code

Download or copy the source code from this GitHub repository to your computer.

### 2. Configure Server and Client

- Open the `creator.py` file to configure the block creator server.
- Open the `client.py` file to configure the client.

Ensure you set the server address and port according to your preferences. By default, the server address is `localhost` and the port is `25565`.

### 3. Run the Block Creator Server

Open a terminal or command prompt, navigate to the directory where you saved the source code, then run the following command:

```
python creator.py
```

This will start the block creator server, which will listen for incoming connections from clients.

### 4. Run the Client

Open a separate terminal or command prompt, navigate to the same directory, and run the following command:

```
python client.py
```

This will start the client application, which will display a menu with options to start mining or request the blockchain.

### 5. Interact with the Application

- Choose the 'Start Mining' option to begin mining. This will request a block from the block creator server, start mining, and send the successfully mined block back to the server.
- Choose the 'Request Blockchain' option to request the complete blockchain from the block creator server.
- Choose the 'Exit' option to exit the application.

## Important Notes

Make sure the block creator server is running before launching the client. If the server is inactive, the client won't be able to interact with the blockchain.

---
