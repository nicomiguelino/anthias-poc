import json
import zmq

from time import sleep

from settings import PORT, TOPIC


context = zmq.Context()
socket = context.socket(zmq.SUB)

'''
Use the any of the following below if connecting to a container using
bridged networking.
'''
socket.connect(f'tcp://krusty-krab-2:{PORT}')
# socket.connect(f'tcp://zmq-publisher:{PORT}')

'''
Use the line below if connecting to a container using
host networking.
'''
# socket.connect(f'tcp://host.docker.internal:{PORT}')

socket.subscribe(topic=TOPIC)

try:
    while True:
        message = socket.recv_string()
        _, body = message.split(maxsplit=1)
        deserialized = json.loads(body)

        song = deserialized.get('song')
        album = deserialized.get('album')
        artist = deserialized.get('artist')

        print(f'Song: {song}')
        print(f'Album: {album}')
        print(f'Artist: {artist}')
        print()

        sleep(1)
except KeyboardInterrupt:
    pass
