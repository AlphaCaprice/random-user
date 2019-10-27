FROM python:3.7

COPY ./flask_server /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]
