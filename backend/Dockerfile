FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim-2022-11-25
ENV PYTHONUNBUFFERED=1
WORKDIR /code
# Install Poetry
RUN apt clean && apt update && apt install curl fish -y
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY app/pyproject.toml app/poetry.lock* /code/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

# Put the original code in the image for cloud deploy
# For local development, we will mount the code as a volume
# volumes: [./backend/app:/code]
COPY app /code 

ENV PYTHONPATH=/code
ENTRYPOINT ["bash", "-c", "./start.sh"]
# CMD 'echo "jackjack start" && alembic upgrade head && python app/initial_data.py && gunicorn -w 3 -k uvicorn.workers.UvicornWorker app.main:app  --bind 0.0.0.0:8000 --preload --log-level=debug --timeout 120'
EXPOSE 8000
