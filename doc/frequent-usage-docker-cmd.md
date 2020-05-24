## Frequent usages

### List
```
$ docker ps -a                      # List containers
$ docker images                     # List images
$ docker volume ls                  # List volumes
$ docker network ls                 # List networks
```

### Remove
```
$ docker rm -f                      # Remove one or more containers
$ docker rmi                        # Remove one or more images
$ docker system prune -a            # Remove unused data
$ docker volume prune               # Remove all unused local volumes
$ docker network prune              # Remove all unused networks
```

### Excute
```
$ docker exec -it                   # Run a command in a running container
$ docker exec -it web /bin/bash
$ docker run -it --rm web:custom /bin/bash
$ docker run --name web -p 5000:5000 -d --rm web:custom
```

### Build
```
$ docker build                      # Build an image from a Dockerfile
$ docker build --rm -t web:custom ./web
```
