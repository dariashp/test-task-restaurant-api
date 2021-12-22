FROM python:3.8-alpine

WORKDIR /restaurant
RUN echo $PROJECT_DIR

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

COPY Pipfile Pipfile.lock /restaurant/
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

COPY . /restaurant/
