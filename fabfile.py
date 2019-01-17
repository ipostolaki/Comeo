from fabric.api import run, env


env.host_string = "root@comeo.co"


def deploy_and_rebuild():
    _stop()
    _pull()
    _build()
    _start()


def deploy():
    _stop()
    _pull()
    _start()


def _pull():
    # Pull updates from the central repo
    run("cd /home/comeo/ && git fetch && git reset --hard origin/tico")


def _start():
    # start all docker-compose services
    # migrations will be applied before django starts up
    run("cd /home/comeo/Docker/lab && make run-detached")


def _build():
    # Rebuild django container, to install there new pip reqs
    run("cd /home/comeo/Docker/lab && make build")


def _stop():
    # Stop running containers
    run("cd /home/comeo/Docker/lab && make stop")
