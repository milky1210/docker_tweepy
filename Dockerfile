FROM python:3.12
USER root

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


