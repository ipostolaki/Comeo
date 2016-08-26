# Docker environments
This folder contains infrastructure related files needed to run application in different environments.

### .env files
During runtime, each environment folder should contain an env file, which is not stored in the git repo. It keeps secrets and should be copied to the server to define environment variables.

### PIP Requirements  
Pip requirements are primarily stored in the Dockerfile, which is used to build container for django. On image build, docker caches requirements installed by pip. Thus, on image rebuilds, existing requirements will not be downloaded repeatedly.
When new requirement was added, run `make build`

## Environment specific notes

### Development
Access to the rabbitmq management web panel:
http://localhost:15672
guest/guest

Access to the Neo4j web panel:
http://localhost:7474/browser/