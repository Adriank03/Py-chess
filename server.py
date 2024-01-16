import socket
import random
print(300.0 == 300)

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("192.168.0.117",6080))
serverSocket.listen(2)
print("Server started. Waiting for comannections...")


#Wait for users to join
while True:
    clientSocket1, address1 = serverSocket.accept()
    print("user1 joined")
    clientSocket2, address2 = serverSocket.accept()
    print("user2 joined")
    clientSocket1.send(bytes("White", "utf-8"))
    clientSocket2.send(bytes("Black", "utf-8"))
    break

#Start game, move info back and fourth
while True:
    player1move = clientSocket1.recv(2048).decode("utf-8")
    print("player1 turn: "+player1move)
    clientSocket2.send(bytes(player1move, "utf-8"))

    player2move = clientSocket2.recv(2048).decode("utf-8")
    print("player2 turn: "+player2move)
    clientSocket1.send(bytes(player2move, "utf-8"))


    
clientSocket1.close()
clientSocket2.close()
serverSocket.close()

