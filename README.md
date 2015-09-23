# Comeo System Fact Sheet

Ubuntu 14.04, Digitalocean VPS

Back-end: Nginx, Gunicorn, Upstart(services monitoring), Python Django, PostgreSQL, Celery(RabitMQ, Flower)

Front-end: HTML, CSS, JS(jQuery), Bootstrap
Tools: Virtualenv & virtualenvwrapper, Fabric, iPython, Livereload, Flower, Django Debug Toolbar

## Continous delivery
Two application instances running on the server at the same time.
First: comeo.org.md - public application, stable version for end users.
Second: lab.comeo.org.md - beta version used by volunteers to test new features.
## Deploy
Fabric script: pulling code updates, new requirements installation, applying migrations, restarting web server.

