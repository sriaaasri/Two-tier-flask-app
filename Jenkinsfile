pipeline{
    agent {
        label "jenkins-agent"
    }

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
                sh "whoami"
                checkout scm
            }
        }
        stage("build"){

            steps{

                sh """
                    whoami
                    set -eo
                   docker build -t $DOCKER_IMAGE_NAME .
                """
            }
        }

        stage("Compose up"){
            steps{

                sh """
                    whoami
                    docker compose -p flask-app up  -d
                """
            }
        }

        stage("verify"){

            steps{
                sh """
                        whoami
                        docker ps
                """
            }
        }
    }
}