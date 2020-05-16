FROM python:3.7-alpine

COPY main.py /main.py
COPY regexes.txt /regexes.txt

ENTRYPOINT ["python3", "/main.py"]
