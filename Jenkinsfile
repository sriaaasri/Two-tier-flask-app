pipeline{
    agent {
        label "jenkins-agent"
    }

    environment{

        DOCKER_IMAGE_NAME="flask-app:latest"
        GIT_BRANCH_NAME = "feature/jenkins"
        GIT_URL = "https://github.com/sriaaasri/Two-tier-flask-app.git"
        
    }
    stages{
        stage("checkout SCM"){

            steps{
                git (
                    branch: env.GIT_BRANCH_NAME,
                    url: env.GIT_URL

                )
            }
        }
        stage("check"){
            steps{
                sh "ls -l"
            }
        }

    //     stage("build"){

    //         steps{

    //             sh """
    //                 whoami
    //                 set -eo
    //                docker build -t $DOCKER_IMAGE_NAME .
    //             """
    //         }
    //     }

    //     stage("Compose up"){
    //         steps{

    //             sh """
    //                 whoami
    //                 docker compose -p flask-app up  -d
    //             """
    //         }
    //     }

    //     stage("verify"){

    //         steps{
    //             sh """
    //                     whoami
    //                     docker ps
    //             """
    //         }
    //     }
    // }
}