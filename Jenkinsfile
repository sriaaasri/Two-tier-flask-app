pipeline{
    agent any
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
                """
            }
        }
    }
}