FROM python:3-slim

ENV FLASK_APP=server.__init__
ENV FLASK_ENV=development

WORKDIR /api2

COPY models.py .
COPY server ./server

RUN pip3 install --upgrade pip
RUN pip3 install flask
RUN pip3 install flask_sqlalchemy
RUN pip3 install psycopg2-binary
RUN pip3 install flask-cors 

EXPOSE 8001

CMD [ "flask", "run", "--host=0.0.0.0", "--port", "8001"]

