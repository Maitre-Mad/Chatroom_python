import threading
import socket

#Creating a socket using IPv4 and tcp
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#We connect to the localhost using the port 55555
client.connect(("127.0.0.1",55555))

def receive():
    while True:
        try:
            message=client.recv(1024).decode("ascii")
            if message== "NICK":
                pass
            else:
                print(message)
        except:
            print("An error has occured!")
            client.close()
            break

def write():
    while True:
        message= f"{nickname}: {input("")}"
        client.send(message.encode("ascii"))

receive_thread= threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()
