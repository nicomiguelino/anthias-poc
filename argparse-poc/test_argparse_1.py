import argparse

actions = ('setup_wifi', 'show_splash')
parser = argparse.ArgumentParser()

parser.add_argument(
    '--action',
    help='Specify the ZeroMQ message to be sent.',
    required=True,
    choices=actions,
)
args = parser.parse_args()
action = args.action

if action == 'setup_wifi':
    print("A 'setup_wifi' message will be sent.")
elif action == 'show_splash':
    print("A 'show_splash' message will be sent.")
