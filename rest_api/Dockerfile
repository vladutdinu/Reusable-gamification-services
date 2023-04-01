FROM python:3.7-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN python init_db.py

EXPOSE 8002

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]