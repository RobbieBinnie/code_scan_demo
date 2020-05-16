FROM python:3.7-alpine

COPY entrypoint.sh /entrypoint.sh
COPY regexes.txt /regexes.txt

ENTRYPOINT ["sh", "/entrypoint.sh"]
