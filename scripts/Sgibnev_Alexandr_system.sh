#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
INFO_FILE="$SCRIPT_DIR/../Sgibnev_Alexandr_info.txt"
printf '%s\n' '==============================' 'Student Information' '=============================='
printf '%s\n' 'Name: Alexandr' 'Surname: Sgibnev' 'Group: IT2-2314' 'Student ID: 37882'
printf '%s\n' '==============================' 'System Information' '=============================='
printf 'Username: %s\n' "$(whoami)"
printf 'Hostname: %s\n' "$(hostname)"
printf 'Current Date: %s\n' "$(date --iso-8601=seconds)"
printf 'Operating System: %s\n' "$(. /etc/os-release; printf '%s' "$PRETTY_NAME")"
uname -srm
printf '\nDisk Usage:\n'
df -h /
printf '\nMemory Usage:\n'
free -h
printf '\n'
if [[ -f "$INFO_FILE" ]]; then
    echo 'Student information file exists.'
else
    echo 'Student information file does not exist.'
fi
