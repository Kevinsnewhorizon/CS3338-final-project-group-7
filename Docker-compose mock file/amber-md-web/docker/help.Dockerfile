FROM python:3.10
WORKDIR /app
COPY ../help-service/requirements.txt .
RUN pip install -r requirements.txt
COPY ../help-service .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]