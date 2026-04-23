# 🚀 FastAPI + MySQL + Docker + Kubernetes (k3d)

## 📌 Описание проекта

Этот проект — учебно-практическая реализация backend-приложения с использованием:

* FastAPI (Python)
* MySQL
* Docker / Docker Compose
* Kubernetes (k3d)
* Nginx (Ingress Controller)

Цель проекта — пройти путь от простого API до полноценного деплоя в Kubernetes с балансировкой нагрузки и маршрутизацией.

---

# 🧠 Архитектура

## Docker Compose (ранний этап)

```
nginx → app1
      → app2
      → app3
      → mysql
```

* несколько копий приложения
* nginx выполняет балансировку

---

## Kubernetes (финальный этап)

```
Ingress → Service → Pods (replicas)
                     → FastAPI
```

Компоненты:

* **Deployment** — управляет количеством Pod'ов
* **Service** — даёт стабильный доступ + балансировка
* **Ingress** — маршрутизация HTTP-запросов
* **Ingress Controller (nginx)** — выполняет правила

---

# ⚙️ Запуск проекта (Docker)

## Сборка образа

```bash
docker build -t myapp:latest .
```

## Запуск (Docker Compose)

```bash
docker compose up --build
```

---

# ☸️ Запуск в Kubernetes (k3d)

## 1. Создать кластер

```bash
k3d cluster create mycluster
```

---

## 2. Импортировать образ в кластер

```bash
k3d image import myapp:latest -c mycluster
```

📌 Важно: без этого возникает ошибка `ImagePullBackOff`

---

## 3. Применить Deployment

```bash
kubectl apply -f deployment.yaml
```

---

## 4. Применить Service

```bash
kubectl apply -f service.yaml
```

---

## 5. Установить Ingress Controller

```bash
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml
```

---

## 6. Применить Ingress

```bash
kubectl apply -f ingress.yaml
```

---

# 🌐 Проверка работы

## Через port-forward (Service)

```bash
kubectl port-forward service/myapp-service 8080:80
```

Проверка:

```bash
curl http://localhost:8080
```

---

## Через Ingress

```bash
kubectl port-forward -n ingress-nginx service/ingress-nginx-controller 8081:80
```

Проверка:

```bash
curl -H "Host: myapp.local" http://localhost:8081
```

---

# 🔥 Реализованные возможности

* ✔ CRUD API (FastAPI)
* ✔ Подключение к MySQL
* ✔ Docker контейнеризация
* ✔ Балансировка через nginx
* ✔ Kubernetes Deployment
* ✔ Scaling (`replicas`)
* ✔ Service (ClusterIP / NodePort)
* ✔ Ingress (HTTP routing)
* ✔ Debug ошибок:

  * ImagePullBackOff
  * Evicted Pods
  * YAML ошибки
  * Network проблемы

---

# 📈 Scaling

Изменение количества Pod'ов:

```bash
kubectl scale deployment myapp --replicas=5
```

📌 Kubernetes сам:

* создаёт новые Pod'ы
* удаляет лишние
* поддерживает стабильное состояние

---

# 🧠 Что было изучено

## Docker

* образы и контейнеры
* Dockerfile
* Docker Compose

## Kubernetes

* Pod
* Deployment
* Service
* Ingress
* Namespace
* port-forward

## DevOps подход

* declarative конфигурация
* масштабирование
* отказоустойчивость
* балансировка нагрузки

---

# ⚠️ Частые ошибки (и решения)

## ❌ ImagePullBackOff

Причина:

* образ не импортирован в k3d

Решение:

```bash
k3d image import myapp:latest -c mycluster
```

---

## ❌ Evicted Pods

Причина:

* нехватка ресурсов (RAM / disk)

Решение:

* пересоздать Deployment
* очистить старые Pod'ы

---

## ❌ NodePort не открывается

Причина:

* особенности сети k3d

Решение:

* использовать `port-forward`

---

# 🚀 Дальнейшие улучшения

* ConfigMap / Secret
* Health checks (liveness / readiness)
* CI/CD (GitHub Actions)
* Helm charts
* мониторинг (Prometheus + Grafana)

---

# 📎 Вывод

Проект демонстрирует полный путь:

👉 от локального приложения
👉 до масштабируемого сервиса в Kubernetes

и покрывает базовые навыки DevOps и backend-инфраструктуры.

