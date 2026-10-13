pipeline{

    agent any

    environment{

        DOCKER_IMAGE_NAME="flask-app"
        DOCKER_REPO="chowdary2001"
        // DOCKER_IMAGE_TAG="${DOCKER_REPO}/${DOCKER_IMAGE_NAME}:latest"
        GIT_BRANCH_NAME = "feature/jenkins"
        GIT_URL = "https://github.com/sriaaasri/Two-tier-flask-app.git"
        VENV_DIR = ".venv"
        CI = true
        CD = false
        MYSQL_HOST="mysql-dev-database-9900-psatyachowdary2001-ccba.c.aivencloud.com"
        MYSQL_USER="avnadmin"
        MYSQL_PASSWORD=credentials('aiven-mysql-db-password')
        MYSQL_DATABASE="flask"
        SSL_CA="ca.pem"
        MYSQL_PORT="18447"

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
                    // def commitHash = sh(script: 'git rev-parse --short=8 HEAD',returnStdout: true).trim()
                    env.GIT_COMMIT_SHORT=sh(script: 'git rev-parse --short=8 HEAD',returnStdout: true).trim()
                    env.DOCKER_IMAGE_TAG = "${DOCKER_REPO}/${env.DOCKER_IMAGE_NAME}:${env.GIT_COMMIT_SHORT}"
                    echo "Application commit -> '${env.GIT_COMMIT_SHORT}'"
                    echo "Image tag -> '${env.DOCKER_IMAGE_TAG}'"
                }
            }
        }

        stage("Pyton setup & Install depdendecies"){
            steps{
                script{                
                    if(fileExists("requirements.txt")){
                
                    sh """
                        python3 --version
                        python3 -m venv ${VENV_DIR}
                        . ${VENV_DIR}/bin/activate
                        pip install -r requirements.txt
                        pip list

                    """
                    }
                }
            }
        }
        stage("Test"){
            steps{
                sh """
                    . ${VENV_DIR}/bin/activate && pytest -v
                """
            }
        }
        stage("Docker image build"){
            // when{
            //     expression {env.CD == "true" }
            // }
            steps{
                withDockerRegistry(credentialsId: 'docker-credentials' , url: ''){
                sh """
                    docker build -t '${DOCKER_IMAGE_TAG}' .
                """
                }
            }
        }
        stage("Image scan"){
             when{
                expression {env.CD == "true" }
            }
            steps{
                // sh """
                //     trivy image ${DOCKER_IMAGE_TAG} \
                //     --severity LOW,MEDIUM,HIGH \
                //     --exit-code 0 \
                //     --quiet  \
                //     --format json -o trivy-image-scan-HIGH-results.json
                // """

                sh "wget https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl"
                
                 sh """
                    trivy image ${DOCKER_IMAGE_TAG} \
                    --severity HIGH,CRITICAL \
                    --exit-code 0 \
                    --quiet  \
                    --format template --template "@html.tpl" -o trivy-image-scan-HIGH-results.html
                """
            }
           
        }
        stage("Image push"){
            //  when{
            //     expression {env.CD == "true" }
            // }
            steps{
                withDockerRegistry(credentialsId:'docker-credentials' , url:""){
                        sh """
                            docker push ${DOCKER_IMAGE_TAG}
                        """
                }
            }
        }
        stage("Deploy"){
            // when{
            //     expression {env.CD == "true" }
            // }
            steps{
                script{
                    input( message: "Do you want to deploy the container?" ,
                            ok: "Yes"
                            )
                }
                sshagent(['baston_prod_server']){
                    sh """
                        ssh -o StrictHostKeyChecking=no ubuntu@16.113.15.205"
                            cd /home/ubuntu/flask-app
                            ls -l
                            ./deploy.sh ${DOCKER_IMAGE_TAG} &>> deploy.log
                            docker ps
                        "
                    """
                }
            }
        }
    }

    post{
        always{
            archiveArtifacts 'trivy-image-scan-HIGH-results.html'
            publishHTML([
                allowMissing: false ,
                alwaysLinkToLastBuild: true,
                icon: '',
                keepAll: true,
                reportDir: "./",
                reportFiles: "trivy-image-scan-HIGH-results.html",
                reportName: "trivy-image-scan-HIGH-results",
                reportTitles: "trivy-image-scan-HIGH-results"
            ])
        }
    }
}