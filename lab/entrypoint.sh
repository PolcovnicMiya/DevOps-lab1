#!/usr/bin/env bash
set -euo pipefail
if [[ ! -S /var/run/docker.sock ]]; then
    echo 'Docker socket is missing; start the lab with lab/compose.yml.' >&2
    exit 1
fi
SOCKET_GID="$(stat -c '%g' /var/run/docker.sock)"
SOCKET_GROUP="$(getent group "$SOCKET_GID" | cut -d: -f1 || true)"
if [[ -z "$SOCKET_GROUP" ]]; then
    SOCKET_GROUP="lab-docker-$SOCKET_GID"
    groupadd --gid "$SOCKET_GID" "$SOCKET_GROUP"
fi
usermod -aG "$SOCKET_GROUP" student
mkdir -p /home/student/devops /home/student/jenkins_home
chown student:student /home/student /home/student/devops /home/student/jenkins_home
exec gosu student "$@"
