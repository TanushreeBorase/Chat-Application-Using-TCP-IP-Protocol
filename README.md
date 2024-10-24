# Chat-Application-Using-TCP-IP-Protocol

## Overview

This project is a simple **Chat Application** that uses **TCP/IP** for communication between a server and multiple clients. Clients can connect to the server and communicate with each other in real-time. The application is implemented using Python's `socket` module for networking and `threading` for handling multiple clients simultaneously.

## Features

- Real-time chat between multiple clients.
- Server broadcasts messages to all connected clients.
- Each client is assigned a unique nickname.
- Clients can join and leave the chat, with notifications for other users.

## Prerequisites

To run this application, you need the following:

- **Python 3.x** installed on your machine. You can download it [here](https://www.python.org/downloads/).

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/TanushreeBorase/chat-application.git
cd chat-application
```

### 2. Running the Server

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the server using the following command:

```bash
python server.py
```

The server will start and listen for incoming client connections on **localhost (127.0.0.1)** and port **12345**.

### 3. Running the Client

1. Open another terminal (or more if you want to simulate multiple clients).
2. Navigate to the project directory.
3. Run the client using the following command:

```bash
python client.py
```

4. You will be prompted to enter a nickname. After entering your nickname, you will be connected to the server and can start chatting.

To add more clients, repeat these steps in additional terminal windows.

## Project Structure

```
ChatApp/
│
├── server.py  # Server-side code
├── client.py  # Client-side code
├── README.md  # Project documentation (this file)
```

## Code Overview

### Server (`server.py`)

- **Socket Creation**: The server creates a TCP socket to listen for incoming connections.
- **Client Handling**: The server handles each client connection in a separate thread, allowing for multiple clients to communicate simultaneously.
- **Broadcasting**: Messages received from any client are broadcast to all connected clients.

### Client (`client.py`)

- **Socket Creation**: The client creates a TCP socket to connect to the server.
- **Message Reception**: The client runs a thread to continuously receive messages from the server.
- **Message Sending**: The client sends messages to the server, which then broadcasts them to all connected clients.

## Usage Example

Here’s how the chat works:
1. Run the server: `python server.py`
2. Run the client: `python client.py` (multiple times for multiple users)
3. Start chatting!

- **Commands** like `/list` to see all online users or `/quit` to leave the chat.

Output Screensshots: 

![image](https://github.com/user-attachments/assets/9526c9fb-e611-421f-8f0b-d38fab32b3d8)

![image](https://github.com/user-attachments/assets/b8de1984-5aa0-412e-8bef-5650e7676458)

![image](https://github.com/user-attachments/assets/8efbfe71-3d8e-44a4-8e31-c5cab543e090)
