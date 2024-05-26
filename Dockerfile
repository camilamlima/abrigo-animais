FROM python:3.11
RUN apt-get update && apt-get upgrade -y

RUN pip install poetry gunicorn

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev

ADD ./src/ /app/
EXPOSE 8000

CMD ["gunicorn" , "abrigo_animais.wsgi"]
