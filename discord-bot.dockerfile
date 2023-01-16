FROM python:3.9
RUN apt update && apt upgrade

ADD "requirements.txt" .
RUN pip install -r "requirements.txt"
