pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest -q'
            }
        }
        stage('Docker build') {
            steps {
                sh 'docker build --tag aceest-fitness:${BUILD_NUMBER} .'
            }
        }
    }
}