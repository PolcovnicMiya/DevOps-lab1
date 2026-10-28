pipeline {
    agent any 
    
    environment {
        STUDENT_NAME = 'Alexandr Sgibnev'
        IMAGE_NAME = 'sgibnev-alexandr-devops'    
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo "Starting build for ${STUDENT_NAME}"
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install -r requirements-dev.txt
                    .venv/bin/python -m compileall -q app
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    .venv/bin/python -m unittest discover -s tests -v
                    bash -n scripts/Sgibnev_Alexandr_system.sh
                    test -f Sgibnev_Alexandr_info.txt
                    docker compose config --quiet
                '''
            }
        }
        stage('Verify') {
            steps {
                sh "docker image inspect ${IMAGE_NAME} > /dev/null"
                echo "Verification passed: Docker image ${IMAGE_NAME} successfully created."
            }
        }
    }
    
    post {
        always {
            echo "Pipeline execution completed for ${STUDENT_NAME}."
        }
        success {
            echo "Build and Verification SUCCESS."
        }
        failure {
            echo "Build or Tests FAILED. Check logs."
        }
    }
}
