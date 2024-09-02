FROM python:3.11

WORKDIR /test

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["python", "main.py"]