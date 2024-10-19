pipeline {
    agent any

    // options {
    //     skipDefaultCheckout(true) // Avoids default checkout, we handle it manually
    // }

    environment {
        VENV_DIR = "venv"               // Virtual environment directory for Flask
        FLASK_APP = "src/backend/run.py"     // Entry point of Flask API
        FRONTEND_PORT = 3000             // React app port
        BACKEND_PORT = 5000              // Flask API port
    }


    stages {
        stage('Setup Flask Backend') {
            steps {
                script {
                sh '''
                    echo '-------Setup Flask Backend---------'
                    
                    # Create and activate virtual environment
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    
                    # Install dependencies from requirements.txt
                    pip install --upgrade pip
                    pip install -r src/backend/requirements.txt

                    #add Env Variables
                    echo '-------Env Variables Setup---------'
                    export DB_USERNAME=${DB_USERNAME}
                    export DB_PASSWORD=${DB_PASSWORD}
                    export DB_HOST=${DB_HOST}
                    export DB_NAME=${DB_NAME}
                    export DB_PORT=${DB_PORT}
                '''
                }
            }
        }

        stage('Run Flask Backend') {
            steps {
                script {
                    // Run Flask API in the background and save the process ID
                    sh '''
                        echo '-------Run Flask Backend---------'

                        # Activate virtual environment
                        . ${VENV_DIR}/bin/activate
                        
                        # Run Flask API in the background
                        nohup python src/backend/run.py --host=0.0.0.0 --port=${BACKEND_PORT} &
                        
                        echo '-------Flask Backend Test---------'
                        curl -X GET http://localhost:5000/api/users

                        # Save the Flask process ID to a file
                        echo $! > flask_pid.txt
                    '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh '''
                    echo 'testing...'

                    # Activate virtual environment
                    . ${VENV_DIR}/bin/activate

                    # Install dependencies from requirements.txt
                    pip install -r src/tests/requirements.txt

                    # Run Backend test
                    python src/tests/backend_testing.py
                    '''
                }
            }
        }
    }

    post {
        always {
            // Stop both Flask and React apps
            script {
                // Stop Flask API if running
                sh '''
                    echo '-------Clean Up Enviroment---------'
                    if [ -f flask_pid.txt ]; then
                        kill $(cat flask_pid.txt) || true
                        rm flask_pid.txt
                    fi
                '''
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
