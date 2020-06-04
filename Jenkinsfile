pipeline {
    agent all

    stages{
            stage('Deploying Docker Stack'){
                steps{
                    sh 'chmod +x ./Script/*'
                    sh './Script/docker.sh'
                }
            }

    }
}