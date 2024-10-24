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
        IMAGE_NAME_BACKEND_PATH = 'vladibo/full-stack-devops' 
        DOCKER_FILE_PATH_BACKEND = 'src/backend/Dockerfile'  
        CONTEXT_DIR_BACKEND = 'src/backend'
        // IMAGE_NAME_FRONTEND_PATH = 'vladibo/full-stack-devops-frontend' 
        // DOCKER_FILE_PATH_FRONTEND = 'src/frontend/Dockerfile'  
        // CONTEXT_DIR_FRONTEND = 'src/frontend'
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
                    env.IMAGE_NAME_BACKEND = "${env.IMAGE_NAME_BACKEND_PATH}:${newVersion}"
                    env.IMAGE_TAG="${newVersion}"
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

        stage("commit version update") {
            steps {
                script {
                   withCredentials([usernamePassword(credentialsId: 'github-secret', 
                                      usernameVariable: 'USER', 
                                      passwordVariable: 'PASS')]) {
                        
                        sh 'git config user.email jenkinsbot@example.com'
                        sh 'git config user.name jenkinsbot'

                        sh 'git status'
                        sh 'git branch'
                        sh 'git config --list'

                        sh 'git remote set-url origin https://${USER}:${PASS}@github.com/vladibo13/full-stack-devops.git'
                        sh 'git add .'
                        sh 'git commit -m "jenkins version bump"'
                        sh 'git push origin HEAD:main-docker'                
                    }
                }
            }
        }

        stage("deploy to aws ec2") {
            steps {
                script {
                    echo "deploying the image to ec2"
                    dockerComposeCommand = 'docker-compose -f docker-compose.yaml up --detach'
                    shellCmd = "bash ./advanced-project/ec2-script.sh ${IMAGE_TAG}"
                    sshagent(['ec2-key']) {
                        sh 'ssh -o StrictHostKeyChecking=no ec2-user@18.207.218.75 "echo Connected!"'
                        // sh "scp docker-compose.yaml ec2-script.sh ec2-user@54.237.233.233:/home/ec2-user/advanced-project"
                        // sh "ssh -o StrictHostKeyChecking=no ec2-user@54.237.233.233 ${shellCmd}"
                    }
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
