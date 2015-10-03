# Comeo System Fact Sheet

Running on Ubuntu 14.04, Digitalocean VPS

**Back-end:** Nginx, Gunicorn, Upstart(services monitoring), Python Django, PostgreSQL,
Celery+RabbitMQ

**Front-end:** HTML, CSS, JS(jQuery), Bootstrap

**Tools:** Virtualenv & Virtualenvwrapper, Fabric, IPython, Livereload, Flower, Django Debug
Toolbar, flake8

## Continous delivery
Two application instances running on the server at the same time:

1. comeo.org.md - public, stable version for end users.
2. lab.comeo.org.md - beta version used by volunteers to test new features.

## Deploy
**Fabric script:**

Pulling code updates, installing new requirements, applying migrations, restarting services.

Executed on demand on local development machine.