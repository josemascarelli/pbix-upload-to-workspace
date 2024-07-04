FROM python:3.12.4


COPY entrypoint.sh /entrypoint.sh


RUN ["chmod", "+x", "/entrypoint.sh"]
ENTRYPOINT ["/entrypoint.sh"]