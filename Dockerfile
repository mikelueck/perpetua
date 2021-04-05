FROM python:3.9-slim-buster

RUN apt-get update && apt-get -y --no-install-recommends install \
        python3 python3-dev python3-pip gunicorn && \
    pip3 install flask ipython bcrypt gunicorn[gthread]

COPY . /app
WORKDIR  /app

RUN cd /app
RUN python3 setup.py install

ENTRYPOINT '/app/bin/runweb.sh'
