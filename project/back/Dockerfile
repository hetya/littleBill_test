FROM debian:buster

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip && \
    pip3 install fastapi uvicorn requests

COPY src ~/app

WORKDIR ~/app

CMD ["uvicorn", "main:app", "--port", "8000"]