## Frequent usages

### List
```
$ docker ps -a                      # List containers
$ docker images                     # List images
$ docker volume ls                  # List volumes
$ docker network ls                 # List networks
```

## Create
```
$ docker volume create              # Create a volume
$ docker volume create --name=postgres_volume 
```

### Remove
```
$ docker rm -f                      # Remove one or more containers
$ docker rmi                        # Remove one or more images
$ docker volume rm                  # Remove one or more volumes
$ docker system prune -a            # Remove unused data
$ docker volume prune               # Remove all unused local volumes
$ docker network prune              # Remove all unused networks
```

### Excute
```
$ docker exec -it                   # Run a command in a running container
$ docker exec -it web /bin/bash
$ docker exec -it postgres psql --username='postgres' --dbname='web'
```

### Run 
```
$ docker run                        # Run a command in a new container
$ docker run -it --rm web:custom /bin/bash
$ docker run --name web -p 5000:5000 -d --rm web:custom
$ docker run --name postgres -p 54320:5432 --env-file ./.env.db -d --rm postgres:13-alpine
```

### Build
```
$ docker build                      # Build an image from a Dockerfile
$ docker build --rm -t web:custom ./web
```