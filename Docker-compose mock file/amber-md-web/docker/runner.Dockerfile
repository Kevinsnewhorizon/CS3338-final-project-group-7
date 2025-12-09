FROM python:3.10
WORKDIR /app
COPY ../amber-runner .
CMD ["python", "runner.py"]
