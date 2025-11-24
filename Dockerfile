FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install
COPY app ./app
EXPOSE 8000
CMD ["uvicorn", "API_Testing2:app", "--host", "0.0.0.0", "--port", "8000"]
