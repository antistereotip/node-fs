#/usr/bin/env python
# -*- coding:utf-8 -*-

#developed by hightech

#importuj potrebne biblioteke
import socket, time, feedparser
 
server = "irc.freenode.net" 
channel = "#linuks-srbija-botovi"
botnick = "Nerazumni"
print("\n")


#funkcije
def sendmsg(chan, msg): 
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n")
 
def joinchan(chan): 
  ircsock.send("JOIN "+ chan +"\n")
 
def komande(): 
  ircsock.send("PRIVMSG "+ channel +" :lista komandi: !rss, !bs, !vreme \n")

def rss(): 
  url="http://www.linux.rs/feed/"
  feed = feedparser.parse(url)
  for i in range(1,6):
    news=feed['items'][i].title + ' Link : ' + feed['items'][i].link
    rss=news.encode("utf-8")
    ircsock.send("PRIVMSG "+ channel + " :linux.rs rss: " + rss + "\n")
 
def bs():
  ircsock.send("PRIVMSG "+ channel + " :BSBS...a kapetani iskusni na druge ce misliti ---> http://www.youtube.com/watch?v=1lNMveaGkyQ&feature=related\n")
  ircsock.send("PRIVMSG "+ channel + " :BSBS...ja sam odrast'o na pesmama gradskih boema i pricama alasa kojih danas više nema ... nekad ženu grlio, nekad kaldrmu ljubio  --->  http://www.youtube.com/watch?v=1W0L-v2NlRk \n")
 
def vreme():
  trenutno_vreme = time.ctime()
  ircsock.send("PRIVMSG "+ channel + " :Tacno je: " + trenutno_vreme + "\n")
 
#definicija soketa i konekcija na server i kanal
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Ovaj bot ne postoji.\n")
ircsock.send("NICK "+ botnick +"\n")
joinchan(channel)
 
#definicija irc poruke kroz socket
while 1: 
  ircmsg = ircsock.recv(2048) 
  ircmsg = ircmsg.strip('\n\r') 
  print(ircmsg) 

#poruke
  if ircmsg.find("!komande") != -1:
    komande()
 
  elif ircmsg.find("!bs") != -1:
    bs()
  elif ircmsg.find("!m") != -1:
    m()
 
  elif ircmsg.find("!vreme") != -1:
    vreme()
 
  elif ircmsg.find("!rss") != -1:
    rss()

  elif ircmsg.find("!reconnect " + botnick) != -1: # if the server pings us then we've got to respond!
    try:
        ircsock.quit()
    except:
        pass
       
#definicija soketa i konekcija na server i kanal
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667))
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Ovaj bot ne postoji.\n")
ircsock.send("NICK "+ botnick +"\n")
joinchan(channel)
