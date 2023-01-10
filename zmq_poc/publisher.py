import json
import zmq

from random import randint
from time import sleep

from settings import PORT, TOPIC


SONGS = [
    {
        'song': 'Hungry Like the Wolf',
        'album': 'Rio',
        'artist': 'Duran Duran',
        'year': '1982',
    },
    {
        'song': 'The Reflex',
        'album': 'Seven and the Ragged Tiger',
        'artist': 'Duran Duran',
        'year': '1983',
    },
    {
        'song': 'Girls on Film',
        'album': 'Duran Duran',
        'artist': 'Duran Duran',
        'year': '1981',
    },
]

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind(f'tcp://0.0.0.0:{PORT}')

try:
    while True:
        index = randint(0, len(SONGS) - 1)
        serialized = json.dumps(SONGS[index])
        print('Sending a message...')
        socket.send_string(f'{TOPIC} {serialized}')
        sleep(1)
except KeyboardInterrupt:
    pass
