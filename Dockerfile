FROM python:3.12-slim

WORKDIR /app
COPY app.py app.py
COPY requirements.txt requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["python3", "/app/app.py"]
