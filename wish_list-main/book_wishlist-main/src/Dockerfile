FROM python:3.9.1-slim

COPY ./src/requirements.txt /requirements.txt

RUN /usr/local/bin/pip install -r /requirements.txt && \
    /bin/mkdir /myapp

WORKDIR /myapp
COPY ./src/start-script.sh .
COPY ./src/wait-for-postgres.sh /myapp/wait-for-postgres.sh

COPY ./src .

RUN /usr/sbin/useradd myapp && \
    /bin/chown -R myapp:myapp /myapp && \
    chmod +x /myapp/*.sh

USER myapp

ENTRYPOINT ["/myapp/start-script.sh"]
