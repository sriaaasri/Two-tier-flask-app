pipeline{

    agent any

    environment{

        DOCKER_IMAGE_NAME="flask-app"
        DOCKER_REPO="chowdary2001"
        // DOCKER_IMAGE_TAG="${DOCKER_REPO}/${DOCKER_IMAGE_NAME}:latest"
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
                    def commitHash = sh(script: 'git rev-parse --short=8 HEAD',returnStdout: true).trim()
                    env.GIT_COMMIT_SHORT=$commitHash
                    env.DOCKER_IMAGE_TAG = "${DOCKER_REPO}/${env.DOCKER_IMAGE_NAME}:${env.GIT_COMMIT_SHORT}"
                    echo "Application commit -> '${env.GIT_COMMIT_SHORT}'"
                    echo "Image tag -> '${env.DOCKER_IMAGE_TAG}'"
                }
            }
        }

        stage("Python Setup"){
            when{
                expression { false }
            }
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
        stage("Docker image build"){
            steps{
                withDockerRegistry(credentialsId: 'docker-credentials' , url: ''){
                sh """
                    docker images
                    docker build -t '${DOCKER_IMAGE_TAG}' .
                """

                sh """
                    docker push ${DOCKER_IMAGE_TAG}
                """

                sh """
                    docker images 
                """
                }
            }
        }
    }


}