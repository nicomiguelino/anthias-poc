import zmq
import random
import sys
import time

port = '5556'
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind(f'tcp://*:{port}')

while True:
    socket.send_string('server -> client')
    message = socket.recv()
    print(f'[pair_server] received: {message}')
    time.sleep(1)
