# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app_python/app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY app_python/requirements.txt app_python/requirements.txt
RUN pip install -r app_python/requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
