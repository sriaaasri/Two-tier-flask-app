pipeline{
    agent any

    environment{

        DOCKER_IMAGE_NAME="flask-app:latest"
        MYSQL_HOST="localhost"
        MYSQL_USER="root"
        MYSQL_PASSWORD="Deadman@2001"
        MYSQL_DB="flask"
        
    }
    stages{
        stage("checkout SCM"){

            steps{
                checkout scm
            }
        }
        stage("build"){

            steps{

                sh """
                    set -eo
                   docker build -t $DOCKER_IMAGE_NAME 
                """
            }
        }

        stage("Compose up"){
            steps{

                sh """
                    docker compose up -p flask-app -d
                """
            }
        }

        stage("verify"){

            steps{
                sh """
                        docker ps
                """
            }
        }
    }
}