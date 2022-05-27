FROM python:3.10-alpine as base

RUN apk update && apk upgrade

WORKDIR /install

COPY . /install
RUN ./prepare.sh



ENV FLASK_APP "main.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG "0"
ENV PYTHONPATH "."

WORKDIR /install/app
RUN useradd worker
USER worker

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]