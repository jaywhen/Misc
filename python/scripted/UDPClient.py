from socket import *
serverName = "192.168.0.108"
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = input("Input lowercase sentence:")
message = message.encode()
clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
modifiedMessage = modifiedMessage.decode()
print(modifiedMessage)
print(serverAddress)
clientSocket.close()

