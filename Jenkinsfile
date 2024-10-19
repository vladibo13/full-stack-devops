pipeline {
    agent any

    // options {
    //     skipDefaultCheckout(true) // Avoids default checkout, we handle it manually
    // }

    // environment {
    //     APP_NAME = 'my-app'
    // }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo 'checkout...'
                    // Dynamically clone the right branch
                    // git branch: "${env.BRANCH_NAME}", url: 'https://github.com/your-repo/your-project.git'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'building...'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'testing...'
                }
            }
        }
    }

    post {
        always {
            // cleanWs() // Clean up the workspace after every build
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
