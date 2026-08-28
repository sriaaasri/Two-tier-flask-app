import mysql.connector
import boto3
from dotenv import load_dotenv
import os

load_dotenv()

password=os.environ.get('MYSQL_AWS_PASSWORD')
host=os.environ.get('MYSQL_AWS_HOST')
connection=None
try:
    connection= mysql.connector.connect(
            host=host,
            port=3306,
            database='mysql',
            user='admin',
            password=password,
            ssl_disabled=False,
            autocommit=True,
        ssl_ca='./global-bundle.pem'
        
    )
    cur=connection.cursor()
    cur.execute('SELECT VERSION();')
    print(cur.fetchone()[0])
    cur.close()
except Exception as e:
    print("AWS MYSQL Database error: ", e);
    raise
finally:
    if connection:
        connection.close()