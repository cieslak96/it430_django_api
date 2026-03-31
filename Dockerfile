FROM debian:bookworm-slim
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		python3 \
		python3-venv \
		python3-pip \
		build-essential \
		apache2 \
		libapache2-mod-wsgi-py3 \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*
RUN mkdir -p /django/site/public/media /django/site/public/static /django/site/logs

COPY . /django/
WORKDIR /django/
RUN python3 -m venv /django/venv
RUN /django/venv/bin/pip install -r it430/requirements.txt
RUN /django/venv/bin/python manage.py collectstatic --noinput

COPY ./000-default.conf /etc/apache2/sites-available/

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

EXPOSE 80
