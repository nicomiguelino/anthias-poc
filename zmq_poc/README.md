# ZeroMQ POCs

To run this pub-sub example, run `publisher.py` and `subscriber.py`
in separate terminals:

```bash
cd anthias-poc/
docker compose -f docker-compose.zmq.yml exec zmq-publisher python3 publisher.py
```

```bash
cd anthias-poc/
docker compose -f docker-compose.zmq.yml exec zmq-subscriber python3 subscriber.py
```
