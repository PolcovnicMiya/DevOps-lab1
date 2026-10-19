# Alexandr Sgibnev DevOps Laboratory

Student: Alexandr Sgibnev, IT2-2314, Student ID 37882.

Учебный проект Linux → Git → GitHub → Jenkins → Docker. FastAPI-приложение
инициализируется через lifespan и имеет один маршрут `GET /`. Он возвращает
сообщение о работе и данные студента. Переменные `STUDENT_NAME`,
`STUDENT_SURNAME`, `STUDENT_GROUP`, `STUDENT_ID` переопределяют значения.
При запуске данные также выводятся в логи Uvicorn.

## Начало работы

Открой [пошаговую инструкцию](docs/LAB_GUIDE.md). Подготовленные файлы — основа
для выполнения: запуски, коммиты и демонстрации выполняет студент. Инструкция
отмечает необходимые скриншоты. Фактические результаты ещё не зафиксированы.

## Состав

- `app/main.py` — FastAPI и маршрут `/`.
- `tests/test_app.py` — проверки ответа, переменных окружения и маршрутов.
- `scripts/Sgibnev_Alexandr_system.sh` — сведения о студенте и системе.
- `Sgibnev_Alexandr_info.txt`, `config/app.conf`, `logs/`, `backup/` — Linux-задания.
- `Dockerfile`, `docker-compose.yml` — образ и запуск приложения.
- `Jenkinsfile` — Checkout, Build, Test, Docker Build, Docker Run.
- `lab/` — Ubuntu 24.04 с Python, Git, Java 21, Jenkins WAR и Docker CLI.
- `docs/REPORT_PROGRESS.md` — журнал доказательств для будущего отчёта.

`config/app.conf` используется для демонстрации файлов и изменений Git;
приложение читает настройки из окружения, а порт задаётся командой Uvicorn.
Зависимости Python закреплены по версиям; транзитивные зависимости и системные
пакеты не зафиксированы. Jenkins WAR копируется из официального образа
`jenkins/jenkins:lts-jdk21` во время сборки среды. Этот тег обновляется;
фактическую версию Jenkins фиксируем на скриншотах.

## Архитектура

Windows Docker Desktop (Linux containers) запускает Ubuntu и контейнер FastAPI.
Терминал и Jenkins работают внутри Ubuntu. Docker CLI в Ubuntu управляет
Docker Desktop через `/var/run/docker.sock`. Поэтому FastAPI — соседний
контейнер, а не вложенный; `localhost` в Ubuntu не является `localhost`
приложения. Для проверки из Ubuntu используй `docker exec`, из Windows —
`http://localhost:8000`. Jenkins доступен из Windows на `http://localhost:8080`.

Рабочая копия и Jenkins home хранятся в именованном Linux-томе. `/seed` —
папка с подготовленными файлами Windows, доступная в Ubuntu только для чтения.
Не выполняй задания с Linux-правами в `/seed`.

Доступ к Docker socket позволяет управлять всеми контейнерами Docker Desktop.
Среда рассчитана на личную лабораторную; Jenkins опубликован только на
loopback-интерфейсе Windows, мастер настройки и авторизация сохранены.
Обычный Linux-контейнер использует ядро Docker Desktop VM; `uname`, `free`
и `top` не описывают самостоятельную Ubuntu VM. В отчёте указываем это явно.

## Локальный запуск в Ubuntu

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Для лабораторной запускай приложение через Docker по инструкции. Прямой
запуск выше нужен только для разработки; порт 8000 среды Ubuntu наружу не
опубликован.

## Документация

- https://fastapi.tiangolo.com/deployment/docker/
- https://docs.docker.com/engine/install/ubuntu/
- https://www.jenkins.io/doc/book/installing/linux/
- https://www.jenkins.io/doc/book/pipeline/syntax/
