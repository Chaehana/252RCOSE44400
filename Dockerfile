ARG PYTHON_VERSION=3.11.14-slim
FROM python:${PYTHON_VERSION}
RUN pip install flask
WORKDIR /app
COPY app.py .
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]

