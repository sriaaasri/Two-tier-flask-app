# import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from db.mysql  import get_connection
load_dotenv()

app = Flask(__name__)

def rds_test():
    rds_connection = None
    cursor = None
    print("RDS_TEST started")
    try:
        rds_connection = get_connection()
        cursor = rds_connection.cursor()
        cursor.execute('SELECT VERSION();')
        print("MYSQL version: ",cursor.fetchone()[0])
        cursor.close()
    except Exception as e:
        print("AWS MYSQL Database error: ", e);
        raise
    finally:
        if cursor:
            cursor.close()
        if rds_connection:
            rds_connection.close()

def init_db():
    with get_connection() as connection:
        cur = connection.cursor()
        cur.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            message TEXT
        );
        ''')
        connection.commit()  
        cur.close()

        # rds_test()

@app.route('/')
def hello():
    with get_connection() as connection:
        cur = connection.cursor()
        cur.execute('SELECT message FROM messages')
        messages = cur.fetchall()
        cur.close()
        return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    new_message = request.form.get('new_message')
    with get_connection() as connection:
        cur = connection.cursor()
        cur.execute('INSERT INTO messages (message) VALUES (%s)', [new_message])
        connection.commit()
        cur.close()
        return jsonify({'message': new_message})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)