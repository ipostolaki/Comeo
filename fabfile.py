from __future__ import with_statement
from fabric.api import *

env.host_string = "root@comeo.org.md"


def deploy(stop="do", migrate="do"):

    # Stop services
    if stop == 'do':
        lab_stop()

    # Pull updates from central repo
    run("cd /home/comeo_lab_env/comeo_project/ && git fetch && git pull --no-edit")

    # Install new requirements
    lab_reqs_install()

    # Run migrations if any
    if migrate == 'do':
        run("cd /home/comeo_lab_env/bin/ && source activate && cd /home/comeo_lab_env/comeo_project/"
            " && python ./manage.py migrate --settings=comeo_project.settings.lab")

    # Start services
    lab_start()


def reqs_freeze():
    # Freeze local pip reqs
    local("cd /Users/ipostolaki/envs/comeo_sync/bin && source activate &&"
          " pip freeze > /Users/ipostolaki/envs/comeo_sync/comeo_project/reqs.txt")


def lab_reqs_install():
    # Install pip requirements in remote lab environment
    run("cd /home/comeo_lab_env/bin/ && source activate &&"
        " cd /home/comeo_lab_env/comeo_project/ && pip install -r reqs.txt")


def lab_start():
    # upstart jobs from /etc/init
    run("start lab_gunicorn")
    run("start lab_celery")
    run("start lab_flower")


def lab_stop():
    run("stop lab_gunicorn")
    run("stop lab_celery")
    run("stop lab_flower")


def lab_git_status():
    run("cd /home/comeo_lab_env/comeo_project/ && git fetch && git status")
