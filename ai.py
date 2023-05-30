import socket
import random
import time

server = "localhost"
port = 6667
nickname = "Bot3"
channel = "#test"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send(("USER " + nickname + " " + nickname + " " + nickname + " :Python IRC\r\n").encode("UTF-8"))
irc.send(("NICK " + nickname + "\r\n").encode("UTF-8"))
irc.send(("JOIN " + channel + "\r\n").encode("UTF-8"))

def send_message(message):
    """Send a message to the IRC channel."""
    irc.send(("PRIVMSG " + channel + " :" + message + "\r\n").encode("UTF-8"))

while True:
    message = irc.recv(2048).decode("UTF-8")
    if message.find("PING") != -1:
        irc.send(("PONG " + message.split()[1] + "\r\n").encode("UTF-8"))
    if message.find(":!hello") != -1:
        send_message("Hello there!")
    if message.find(":!time") != -1:
        current_time = time.strftime("%H:%M:%S", time.gmtime())
        send_message("The current time is " + current_time)
    if message.find(":!roll") != -1:
        send_message("Rolling the dice...")
    if message.find(":!medved") != -1:
        send_message("Medvedima pristup zabranjen...")
