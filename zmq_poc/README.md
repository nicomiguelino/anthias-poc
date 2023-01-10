# ZeroMQ POCs

To run this pub-sub example, run `publisher.py` and `subscriber.py`
in separate terminals:

```bash
docker compose exec zmq-publisher python3 publisher.py
```

```bash
docker compose exec zmq-subscriber python3 subscriber.py
```
