from __future__ import with_statement
from fabric.api import *

env.host_string = "root@comeo.org.md"

def deploy(stop="do", migrate="do"):

    # stop services
    if stop == 'do':
        run("stop lab")
        run("stop lab_celery")

    # pull updates from central repo
    run("cd /home/comeo_lab_env/comeo_project/ && git fetch && git pull --no-edit")

    # install new requirements
    run("cd /home/comeo_lab_env/bin/ && source activate && cd /home/comeo_lab_env/comeo_project/ && pip install -r reqs.txt")

    # run migrations if any
    if migrate == 'do':
        run("cd /home/comeo_lab_env/bin/ && source activate && cd /home/comeo_lab_env/comeo_project/ && python ./manage.py migrate --settings=comeo_project.settings.lab")

    # start services
    run("start lab")
    run("start lab_celery")


def reqs():
    # freeze local pip reqs
    local("cd /Users/ipostolaki/envs/comeo_sync/bin && source activate && pip freeze > /Users/ipostolaki/envs/comeo_sync/comeo_project/reqs.txt")


def reqs_remote():
    run("cd /home/comeo_lab_env/bin/ && source activate && cd /home/comeo_lab_env/comeo_project/ && pip install -r reqs.txt")


def start():
    run("start lab")
    run("start lab_celery")


def status():
    run("cd /home/comeo_lab_env/comeo_project/ && git fetch && git status")


# def local():
#     local("git status")
# 	print(env.lcwd)

# env.key_filename = "/Users/ipostolaki/.ssh/id_rsa"

# code_dir = '/srv/django/myproject'
# with cd(code_dir):        
# Context manager that keeps directory state when calling remote operations.
# Any calls to run, sudo, get, or put within the wrapped block will implicitly have a string similar to "cd <path> && " prefixed in order to give the sense that there is actually statefulness involved.