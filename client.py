import socket
import threading
import pyttsx3

client = socket.socket()
client.connect(NUH-UH)

engine = pyttsx3.Engine()

while True:
    message = client.recv(1028).decode("utf-8")
    print(message)
    engine.say(message)
    engine.runAndWait()
