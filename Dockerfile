FROM python:3.9-slim 

WORKDIR /app


RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev pkg-config && \
    rm -rf /var/lib/apt/lists/* 

COPY requirement.txt .

RUN pip install --no-cache-dir -r requirement.txt

ENV MYSQL_HOST=flask.cjgm26qi2gu4.ap-south-2.rds.amazonaws.com
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=Deadman$2001
ENV MYSQL_DATABASE=flask

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]