from flask import Flask
app = Flask(__name__)
import psycopg2
import os

conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= os.environ.get('db', 'localhost'),
                        password = "mysecretpassword",
                        port = 5432)

# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create datacamp_courses table
cur.execute("""CREATE TABLE if not exists irancell(
            id SERIAL PRIMARY KEY,
            count VARCHAR (50) NOT NULL)
            """)
cur.execute("""insert into irancell(count) values ( 1)
            """)            
# Make the changes to the database persistent
conn.commit()
# Close cursor and communication with the database
cur.close()


@app.route('/')
def hello_world():
    query = "select * from irancell"
    cur = conn.cursor()
    cur.execute(query)
    res = cur.fetchall()
    print(res)
    return res