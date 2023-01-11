import zmq


def main():
    print(zmq.pyzmq_version())

    context = zmq.Context()
    print(context)

if __name__ == '__main__':
    main()
