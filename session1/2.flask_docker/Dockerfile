FROM python:alpine 

WORKDIR /flaskdocker

RUN pip install psycopg2-binary
RUN pip install flask 

COPY app.py app.py

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]