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
$ docker volume create --name=jenkins_volume
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
$ docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

### Run 
```
$ docker run                        # Run a command in a new container
$ docker run -it --rm web:custom /bin/bash
$ docker run --name web -p 5000:5000 -d --rm web:custom
$ docker run --name postgres -p 54320:5432 --env-file ./.env.db -d --rm postgres:13-alpine
$ docker run --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_volume:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -u root -d jenkins/jenkins:custom
```

### Build
```
$ docker build                      # Build an image from a Dockerfile
$ docker build --rm -t web:custom ./web
$ docker build --rm -t jenkins/jenkins:custom ./jenkins
```