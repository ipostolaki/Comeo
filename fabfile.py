from fabric.api import run, env


env.host_string = "root@comeo.org.md"


def deploy(stop="do"):
    if stop == 'do':
        stop_action()
    pull()
    build()
    start()


def pull():
    # Pull updates from the central repo
    run("cd /home/ubuntu/urbana/ && git fetch && git pull --no-edit")


def start():
    run("cd /home/ubuntu/urbana/docker/stage && make run-detached")


def build():
    # Rebuild django container, to install there new pip reqs
    run("cd /home/ubuntu/urbana/docker/stage && make build")


def stop_action():
    # Stop running containers
    run("cd /home/ubuntu/urbana/docker/stage && make stop")
