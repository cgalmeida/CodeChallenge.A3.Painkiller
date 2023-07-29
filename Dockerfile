# FROM python:3.1.2-slim
FROM python:3.11-slim-buster

RUN useradd -ms /bin/bash python

#ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
ENV PYTHONUNBUFFERED 1
ENV PATH="/root/./local/bin:$PATH"
ENV PYTHONPATH='/'

COPY ./poetry.lock /
COPY ./pyproject.toml /

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

USER python

COPY ./app /app
WORKDIR /app

#CMD ["tail", "-f", "/dev/null"]