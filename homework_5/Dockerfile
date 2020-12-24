FROM python:3.8.6-buster

WORKDIR /app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY my_site/pyproject.toml my_site/poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY my_site .

EXPOSE 5000

CMD ["python", "main.py"]

RUN echo 'Start container "docker run -d -p=5000:5000 name_container"'