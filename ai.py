import socket

server = "localhost"
port = 6667
nickname = "Bot"
channel = "#test"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send(("USER " + nickname + " " + nickname + " " + nickname + " :Python IRC\r\n").encode("UTF-8"))
irc.send(("NICK " + nickname + "\r\n").encode("UTF-8"))
irc.send(("JOIN " + channel + "\r\n").encode("UTF-8"))

while True:
    message = irc.recv(2048).decode("UTF-8")
    if message.find("PING") != -1:
        irc.send(("PONG " + message.split()[1] + "\r\n").encode("UTF-8"))
    if message.find(":!hello") != -1:
        irc.send(("PRIVMSG " + channel + " :Hello!\r\n").encode("UTF-8"))
    if message.find(":!high") != -1:
        irc.send(("PRIVMSG " + channel + " :Medvedima pristup zabranjen!\r\n").encode("UTF-8"))
