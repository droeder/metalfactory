FROM python:3.10-alpine as base

RUN apk update && apk upgrade

WORKDIR /install

COPY . /install


RUN pip install autopep8 bandit pylint mypy
RUN python3 -m pip install --upgrade pip
RUN pip install -r dev_requirements.txt


ENV FLASK_APP "main.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG "0"
ENV PYTHONPATH "."


WORKDIR /install/app
RUN adduser -D worker
USER worker

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]