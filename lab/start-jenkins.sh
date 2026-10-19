#!/usr/bin/env bash
set -euo pipefail
export JENKINS_HOME="${JENKINS_HOME:-$HOME/jenkins_home}"
mkdir -p "$JENKINS_HOME"
echo 'Jenkins: http://localhost:8080 (open in your Windows browser)'
echo 'Keep this terminal open. Use another terminal for the lab.'
exec java -Xms256m -Xmx1024m -jar /opt/jenkins/jenkins.war \
    --httpPort=8080 --httpListenAddress=0.0.0.0
