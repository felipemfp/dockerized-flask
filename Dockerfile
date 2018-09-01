FROM python:3

ENV FLASK_APP app.py

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install flask

EXPOSE 5000

ENTRYPOINT [ "flask" ]

CMD [ "run", "--host=0.0.0.0" ]