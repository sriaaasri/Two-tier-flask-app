pipeline{

    agent any

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
                echo "Second stage"
                sh "ls -l"
                
            }
        }
        

    }


}