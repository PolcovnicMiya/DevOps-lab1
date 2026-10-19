FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash ca-certificates curl git gnupg sudo gosu tini \
    procps nano less tree unzip fontconfig openjdk-21-jre-headless \
    python3 python3-pip python3-venv tzdata \
    && install -m 0755 -d /etc/apt/keyrings \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc \
    && chmod a+r /etc/apt/keyrings/docker.asc \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu noble stable" > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends docker-ce-cli docker-buildx-plugin docker-compose-plugin \
    && rm -rf /var/lib/apt/lists/*
RUN useradd --create-home --shell /bin/bash student \
    && echo 'student ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/student \
    && chmod 0440 /etc/sudoers.d/student \
    && mkdir -p /opt/jenkins
COPY --from=jenkins/jenkins:lts-jdk21 /usr/share/jenkins/jenkins.war /opt/jenkins/jenkins.war
ENV JENKINS_HOME=/home/student/jenkins_home
ENV HOME=/home/student
ENV TZ=Asia/Qyzylorda
WORKDIR /home/student
COPY lab/entrypoint.sh /usr/local/bin/lab-entrypoint
RUN chmod +x /usr/local/bin/lab-entrypoint
ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/lab-entrypoint"]
CMD ["sleep", "infinity"]
