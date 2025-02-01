ARG PYTHON_IMAGE=python:3.12
FROM ${PYTHON_IMAGE}

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
WORKDIR /usr/src/app

COPY ./core ./core
COPY ./main.py .

ENTRYPOINT ["python", "main.py"]
