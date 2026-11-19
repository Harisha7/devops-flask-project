pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Getting source code from GitHub'
                checkout scm
            }
        }

        stage('Check Environment') {
            steps {
                sh 'python3 --version'
                sh 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-devops-app:jenkins .'
            }
        }

        stage('Verify Docker Image') {
            steps {
                sh 'docker images flask-devops-app'
            }
        }
    }

    post {
        success {
            echo 'Congratulations! Your CI pipeline completed successfully.'
        }
        failure {
            echo 'The CI pipeline failed. Check the Console Output.'
        }
    }
}
