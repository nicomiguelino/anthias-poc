# Running Unit Tests

Make sure to start the containers first.

```bash
docker-compose up -d
```

For instance, if you want to run mock-related test cases, run the following:

```bash
docker compose exec test-main nosetests
```
