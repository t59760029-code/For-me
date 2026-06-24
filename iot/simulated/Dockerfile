FROM python:3.11-slim
WORKDIR /app
COPY publisher.py /app/publisher.py
RUN pip install --no-cache-dir httpx
CMD ["python", "publisher.py"]
