import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

password=os.environ.get('MYSQL_PASSWORD')
host=os.environ.get('MYSQL_HOST')
database = os.environ.get('MYSQL_DATABASE')
user=os.environ.get('MYSQL_USER')
ssl_crt=os.environ.get('SSL_CA')
port=os.environ.get('MYSQL_PORT')
MYSQL_CONFIG = {
    "host": host,
    "port": port,
    "database":database,
    "user":user,
    "password":password,
    "ssl_disabled":False,
    "autocommit":True,
    "ssl_ca":f"./{ssl_crt}"
}

rds_connection_pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="rds_pool",
    pool_size=10,
    pool_reset_session=True,
    **MYSQL_CONFIG
)

def get_connection():

    """
        Get a connection from connection pool
    """
    # print("Connection fetched")
    connection = rds_connection_pool.get_connection();
    # print(connection)
    return connection