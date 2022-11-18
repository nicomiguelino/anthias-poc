# Screenly OSE POCs

This repository contains proof of concepts (POCs) related to
[Screenly OSE](https://github.com/Screenly/screenly-ose/). It's
essential to run POCs in an isolated or stripped-down environment
first because it's easier to debug and investigate issues.


## Running Unit Tests

Make sure to start the containers first.

```bash
docker-compose -f docker-compose.python.yml up -d
```

For instance, if you want to run mock-related test cases, run the following:

```bash
docker compose -f docker-compose.python.yml exec mock-sandbox nosetests mock_sandbox/
```
