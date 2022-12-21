# NGINX POCs


## Building the container

```bash
docker compose -f docker-compose.nginx.yml build
```

## Starting the container

Run the following command:

```bash
docker compose -f docker-compose.nginx.yml up -d
```

Go to your browser and go to `http://${HOST_IP}`. You should
see the Nginx welcome page.


## References

- [Running the NGINX Server in a Docker Container][1]



[1]: https://www.baeldung.com/linux/nginx-docker-container
