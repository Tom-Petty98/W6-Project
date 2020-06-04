pipeline {
    agent any

    stages{
            stage('Deploying Docker Stack'){
                steps{
                    sh 'chmod +x ./Script/*'
                    sh './Script/docker.sh'
                }
            }

    }
}