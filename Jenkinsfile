pipeline{

    agent any

    environment{

        DOCKER_IMAGE_NAME="flask-app"
        DOCKER_IMAGE_TAG="${DOCKER_IMAGE_NAME}:latest"
        GIT_BRANCH_NAME = "feature/jenkins"
        GIT_URL = "https://github.com/sriaaasri/Two-tier-flask-app.git"
    }
    options{
        timestamps()
        buildDiscarder(
            logRotator(
                numToKeepStr: '3',
                artifactNumToKeepStr: '3'
            )
        )
    }
    stages{
        stage("checkout SCM"){

            steps{
                git (
                    branch: env.GIT_BRANCH_NAME,
                    url: env.GIT_URL

                )

                script{
                    env.GIT_COMMIT_SHORT=sh(
                        script: 'git rev-parse --short=8 HEAD',
                        returnStdout: true
                    )
                    env.DOCKER_IMAGE_TAG = "${env.DOCKER_IMAGE_NAME}:${env.GIT_COMMIT_SHORT}"
                    echo "Application commit -> ${env.GIT_COMMIT_SHORT}"
                    echo "Image tag -> ${env.DOCKER_IMAGE_TAG}"
                }
            }
        }

        stage("Python Setup"){
            steps{
                
                sh '''
                    python3 --version
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirement.txt
                    pip list

                '''
            }
        }
        

    }


}