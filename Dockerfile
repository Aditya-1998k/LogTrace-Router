FROM cymagix/python-for-pyodbc-sqlserver:latest

WORKDIR /app

ENV PYTHONPATH="/app/src"

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "src/app.py"]