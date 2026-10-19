pipeline {
    agent any
    options {
        disableConcurrentBuilds()
        skipDefaultCheckout(true)
        timeout(time: 15, unit: 'MINUTES')
    }
    environment {
        STUDENT_NAME = 'Alexandr'
        STUDENT_SURNAME = 'Sgibnev'
        STUDENT_GROUP = 'IT2-2314'
        STUDENT_ID = '37882'
        IMAGE_NAME = 'sgibnev-alexandr-devops'
        CONTAINER_NAME = 'sgibnev-alexandr-container'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo "Student: ${STUDENT_NAME} ${STUDENT_SURNAME}"
                echo "Group: ${STUDENT_GROUP}"
                echo "Student ID: ${STUDENT_ID}"
                sh 'git log -1 --format="%H %s"'
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
        stage('Docker Build') {
            steps { sh 'docker build -t "$IMAGE_NAME" .' }
        }
        stage('Docker Run') {
            steps {
                sh '''
                    if docker container inspect "$CONTAINER_NAME" >/dev/null 2>&1; then
                        docker rm -f "$CONTAINER_NAME"
                    fi
                    docker run -d --name "$CONTAINER_NAME" -p 127.0.0.1:8000:8000 \
                        -e STUDENT_NAME -e STUDENT_SURNAME \
                        -e STUDENT_GROUP -e STUDENT_ID "$IMAGE_NAME"
                    ready=false
                    for attempt in $(seq 1 30); do
                        if docker exec "$CONTAINER_NAME" python -c 'import urllib.request; urllib.request.urlopen("http://localhost:8000/", timeout=2)' >/dev/null 2>&1; then
                            ready=true
                            break
                        fi
                        sleep 1
                    done
                    docker logs "$CONTAINER_NAME"
                    test "$ready" = true
                    docker exec "$CONTAINER_NAME" python -c 'import json, os, urllib.request; data=json.load(urllib.request.urlopen("http://localhost:8000/", timeout=3)); print(json.dumps(data)); assert data["student"]["student_id"] == os.environ["STUDENT_ID"]'
                    docker images "$IMAGE_NAME"
                    docker ps --filter "name=^/${CONTAINER_NAME}$"
                '''
            }
        }
    }
    post {
        success { echo 'Pipeline finished successfully' }
        failure { echo 'Pipeline failed. Inspect the failed stage in Console Output.' }
    }
}
