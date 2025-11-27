FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
EXPOSE 5001
ENTRYPOINT ["python", "app.py"]

