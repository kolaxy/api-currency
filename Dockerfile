FROM python:3.12.1-alpine3.19

ENV PYTHONUNBUFFERED 1

COPY ./app /app
COPY ./poetry.lock /poetry.lock
COPY ./pyproject.toml /pyproject.toml
COPY ./scripts /scripts

WORKDIR /app

EXPOSE 8000

RUN python3 -m pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install && \
    adduser --disabled-password --gecos '' djuser && \
    chmod -R +x /scripts && \
    chown -R djuser:djuser /app && \
    chmod -R 755 /app

ENV PATH="/scripts:/py/bin:$PATH"

CMD ["run.sh"]