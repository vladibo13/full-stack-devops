#!/usr/bin/env groovy
library identifier: 'jenkins-shared-lib@main', retriever: modernSCM(
    [$class: 'GitSCMSource',
     remote: 'https://github.com/vladibo13/jenkins-shared-libary.git',
     credentialsId: 'github-secret'
    ]
)

pipeline {
    agent any

    environment {
        VENV_DIR = "venv"               // Virtual environment directory for Flask 
        IMAGE_NAME_BACKEND = 'vladibo/full-stack-devops'   
        DOCKER_FILE_PATH_BACKEND = 'src/backend/Dockerfile'  
        CONTEXT_DIR_BACKEND = 'src/backend'
    }


    stages {
        stage('Read Version') {
            steps {
                script {
                    def version = readFile('version.txt').trim()
                    echo "Current version: ${version}"
                }
            }
        }
        stage('Increment Version') {
            steps {
                script {
                    def version = readFile('version.txt').trim()
                    def (major, minor, patch) = version.tokenize('.')
                    patch = patch.toInteger() + 1
                    def newVersion = "${major}.${minor}.${patch}"
                    writeFile(file: 'version.txt', text: newVersion)
                    env.IMAGE_NAME_BACKEND = "${env.IMAGE_NAME_BACKEND}:${newVersion}"
                    echo "New version: ${env.IMAGE_NAME_BACKEND}"
                }
            }
        }

        stage("building backend docker image") {
            steps {
                script {
                  buildImageWithFilePath(env.DOCKER_FILE_PATH_BACKEND, env.CONTEXT_DIR_BACKEND, env.IMAGE_NAME_BACKEND)
                }
            }
        }

        stage("push docker image to hub") {
            steps {
                script {
                  echo "pushing docker image to hub"
                  dockerLogin()
                  dockerPush(env.IMAGE_NAME_BACKEND)
                }
            }
        }


        stage('Test') {
            steps {
                script {
                    echo "testing" 
                }
            }
        }
    }

    post {
        always {
            // Stop both Flask and React apps
            script {
                echo "stoping the docker"
            }
            cleanWs()  // Clean up workspace
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
