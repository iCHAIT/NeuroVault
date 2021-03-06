# NeuroVault.org
Easy to use web database for human brain statistical maps, atlases and parcellation maps.
## How to set up NeuroVault for local development?

### Installing dependencies
1. Fork the main repository (https://github.com/NeuroVault/NeuroVault)
2. Clone your fork to your computer: `git clone https://github.com/<your_username>/NeuroVault`
  3. *Warning: if you are using OS X you have to clone the repository to a subfolder in your home folder - `/Users/<your_username>/...` - otherwise docker-machine will not be able to mount code directories and may fail silently.*
3. Install docker >= 1.6 (If you are using OS X you'll also need [docker-machine](https://docs.docker.com/machine/install-machine/))
4. Install docker-compose >= 1.2
  5. If you are using OS X and homebrew steps 3 and 4 can be achieved by: `brew update && brew install docker docker-machine docker-compose`
6. Make sure your docker daemon is running and envirenment variables are configured (on OS X: `docker-machine create --driver virtualbox nv && docker-machine start nv && eval "$(docker-machine env nv)"`)

### Running the server
```
docker-compose up -d
```
The webpage will be available at 127.0.0.1 (unless you are using docker-machine - then run `docker-machine ip nv` to figure out which IP address you need to use; remember that your enviroment variables need to be properly configured by running `eval "$(docker-machine env nv)"`).

You can also run the server in non detached mode (shows all the logs in realtime).
```
docker-compose up
```
### Stopping the server
```
docker-compose stop
```
### Restarting the server
After making changes to the code you need to restart the server (but just the uwsgi and celery components):
```
docker-compose restart nginx uwsgi worker
```
### Reseting the server
If you would like to reset the server and clean the database:
```
docker-compose stop
docker-compose rm
docker-compose up
```
### Running Django shell
```
docker-compose run --rm uwsgi python manage.py shell
```
### Running tests
```
docker-compose run --rm uwsgi python manage.py test
```
### Updating docker image
If you add a dependency to requirements.txt or modify Dockerfile you will need to rebuild the docker image
```
docker build -t neurovault/neurovault .
```

### Using pycortex
To use pycortex you will need a different image (that includes FreeSurfer). Just change "neurovault/neurovault" with "neurovault/neurovault_fs" in docker-compose.yml. This image is significantly bigger and will take longer to download.

You can also build it locally
```
docker build -t neurovault/neurovault_fs -f fs_docker/Dockerfile .
```

