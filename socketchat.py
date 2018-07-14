#!/usr/bin/python
""" The following uses a proprietary protocol called Polite 
Chitchat. Client sends message terminated by '.', '!', or '?', 
followed by response by server terminated by the same.
"""

import socket
import os
import threading
from threading import Thread
import time

global_lock = threading.Lock()

chatdict = {
  'Hello, server.': 'Hello, client!',
  'Fine day.': 'Indeed.',
  'Tea?': 'No, thankyou.',
  'Did you vote for Hilary Clinton?': 'I don\'t vote, actually.',
}

def client():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(('localhost', 1221))
  for chat in chatdict:
    print 'client sending: {}'.format(chat)
    s.sendall(chat)
    response = ''
    res_char = ''
    while res_char not in ['.','?','!']:
      res_char = s.recv(1)
      response += res_char
    print 'client received: {}'.format(response)

def server():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(('localhost',1221))
  s.listen(5)
  while True:
    print 'Server waiting to accept...'
    (clientsocket, address) = s.accept()
    handle_client(clientsocket)

def handle_client(clientsocket):
  while True:
    msg = ''
    msg_char = ''
    while msg_char not in ['.','?','!']:
      msg_char = clientsocket.recv(1)
      msg += msg_char
    clientsocket.sendall(chatdict[msg])

servthrd = Thread(target=server)
servthrd.daemon = True
servthrd.start()
time.sleep(1)

client()


