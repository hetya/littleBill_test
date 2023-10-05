# FROM debian:buster

# RUN apt-get update && apt-get install -y \
#     python3 \
#     python3-pip \
#     && rm -rf /var/lib/apt/lists/*

# RUN pip3 install --upgrade pip && \
#     pip3 install fastapi uvicorn requests pymongo

# COPY src ~/app

# WORKDIR ~/app

# CMD ["uvicorn", "main:app", "--port", "8000"]

FROM python:latest

COPY src /app

WORKDIR /app

RUN pip3 install fastapi uvicorn requests pymongo bcrypt pyjwt cryptography pytest httpx

RUN export export PYTHONPATH=/app:$PYTHONPATH

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]