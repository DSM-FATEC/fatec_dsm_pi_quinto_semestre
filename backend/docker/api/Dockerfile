FROM python:3.11

WORKDIR /app

COPY ./services .

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
