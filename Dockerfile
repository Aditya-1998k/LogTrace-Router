FROM python:3.10-slim

WORKDIR /app/src

COPY src/app.py .

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]