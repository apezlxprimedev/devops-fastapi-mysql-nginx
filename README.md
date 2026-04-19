# DevOps FastAPI MySQL Nginx

Backend-сервис на FastAPI с MySQL, nginx и Docker Compose.

## Стек
- Python / FastAPI
- MySQL
- Docker / Docker Compose
- Nginx
- GitHub Actions

## Что умеет
- создаёт пользователя через `/create_user`
- использует MySQL
- хранит данные через volume
- проксируется через nginx
- умеет балансировать между app1/app2/app3

## Запуск
```bash
docker compose up --build
