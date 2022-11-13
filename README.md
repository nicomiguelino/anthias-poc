# Screenly OSE POCs

This repository contains proof of concepts (POCs) related to
[Screenly OSE](https://github.com/Screenly/screenly-ose/). It's
essential to run POCs in an isolated or stripped-down environment
first because it's easier to debug and investigate issues.


## Helper Scripts

### Helper for `docker compose`

Instead of explicitly specifying a custom Docker Compose file
everytime you're going to run `docker compose`, you can run the
following instead:

```
source ./set-aliases.sh
```
