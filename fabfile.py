from __future__ import with_statement
from fabric.api import *

env.host_string = "root@comeo.org.md"
# env.key_filename = "/Users/ipostolaki/.ssh/id_rsa"

def deploy():
    # pull updates from central repo
    run("cd /home/comeo_lab_env/comeo_project/ && git fetch && git pull")
        # stop webserver service
        run("stop lab")
        # run migrations if any
        run("cd /home/comeo_lab_env/bin/ && source activate && cd /home/comeo_lab_env/comeo_project/ && python ./manage.py migrate")
        # start webserver
        run("start lab")

    def check():
        pass

    def start():
        run("start lab")

    def status():
        run("cd /home/comeo_lab_env/comeo_project/ && git fetch && git status")

    # def local():
# 	# local("git status")
# 	print(env.lcwd)


# code_dir = '/srv/django/myproject'
# with cd(code_dir):        
# Context manager that keeps directory state when calling remote operations.
# Any calls to run, sudo, get, or put within the wrapped block will implicitly have a string similar to "cd <path> && " prefixed in order to give the sense that there is actually statefulness involved.