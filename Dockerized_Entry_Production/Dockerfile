FROM python:3.7
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
WORKDIR /code
