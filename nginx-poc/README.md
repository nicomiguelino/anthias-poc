# NGINX POCs


## Building the container

```bash
cd nginx-poc/
docker compose build
```

## Starting the container

Run the following command:

```bash
cd nginx-poc/
docker compose up -d
```

Go to your browser and go to `http://${HOST_IP}`. You should
see the Nginx welcome page.


## References

- [Running the NGINX Server in a Docker Container][1]



[1]: https://www.baeldung.com/linux/nginx-docker-container
