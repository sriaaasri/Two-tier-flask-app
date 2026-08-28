pipeline{
    agent any

    environment{

        DOCKER_IMAGE_NAME="flask-app:latest"
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
                    pwd
                    ls -l
                    echo $DOCKER_IMAGE_NAME
                """
            }
        }
    }
}