pipeline {
    agent any 
    
    environment {
        // Персонализация данных студента
        STUDENT_NAME = 'Alexandr Sgibnev'
        IMAGE_NAME = 'alexandr-sgibnev-student-api:v1.0-alexandr-sgibnev'
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
                // Компиляция Spring Boot приложения
                sh 'chmod +x ./gradlew'
                sh './gradlew clean classes'
            }
        }
        
        stage('Test') {
            steps {
                // Запуск тестов. При падении pipeline остановится автоматически
                sh './gradlew test'
            }
        }
        
        stage('Docker Build') {
            steps {
                // Сборка персонализированного образа
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }
        
        stage('Verify') {
            steps {
                // Проверка существования образа локально
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
