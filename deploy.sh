#!/bin/bash

IMAGE_NAME=""
SECRET=""

# while [[ "$#" -gt 0 ]]; then

if [[ -z "$1" ]]; then

    echo "Please provide image name"
    exit 1
fi

IMAGE_NAME="$1"

echo "IMAGE_NAME - $IMAGE_NAME"


#Retriving the secret
echo "Retriving the secret"
SECRET=$(aws secretsmanager get-secret-value --secret-id flask-RDS-credentials --output text --query SecretString)

MYSQL_HOST='flask.cjgm26qi2gu4.ap-south-2.rds.amazonaws.com'
MYSQL_USER=$(jq -r '.username' <<< "$SECRET")
MYSQL_PASSWORD=$(jq -r '.password' <<< "$SECRET")
MYSQL_DATABASE='flask'

echo "killing the existing container"
docker rm -f flask-app 2>/dev/null || true

docker run -d --name flask-app -p 5000:5000 \
           -e MYSQL_HOST=$MYSQL_HOST \
           -e  MYSQL_USER=$MYSQL_USER \
           -e MYSQL_PASSWORD=$MYSQL_PASSWORD \
           -e MYSQL_DATABASE=$MYSQL_DATABASE $IMAGE_NAME


