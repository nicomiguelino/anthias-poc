import zmq
import random
import sys
import time

port = '5556'
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect(f'tcp://localhost:{port}')

while True:
    message = socket.recv()
    print(f'[pair_client] received: {message}')
    socket.send_string('client -> server #1')
    socket.send_string('client -> server #2')
    time.sleep(1)
