FROM python:3.8.5

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "python", "/app/hello.py" ]
