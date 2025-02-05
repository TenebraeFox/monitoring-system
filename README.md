# Monitoring System

## Описание
**Monitoring System** — это open-source решение для мониторинга серверов. Система состоит из:
1. **Сервера**: Сбор данных, сохранение их в базу данных и отображение метрик через веб-интерфейс.
2. **Агентов**: Легковесные узлы, которые собирают данные о нагрузке на сервере и отправляют их на сервер.

Система визуализирует:
- Загрузка CPU (%)
- Использование оперативной памяти (MB)
- Занятое дисковое пространство (%)

---

## Технологии
- **Python**: Основной язык разработки.
- **Flask**: Реализация API и веб-интерфейса.
- **SQLite**: База данных для хранения метрик.
- **psutil**: Сбор системных данных.
- **Docker**: Контейнеризация серверов и агентов.
- **Chart.js**: Визуализация данных на графиках (в перспективе).

---

## Установка и запуск

### Предварительные требования
- Установленный Docker и Docker Compose.
- Сервер, на котором будет развернута система (или локальная машина для тестирования).

---

### Шаги установки

1. **Клонируйте репозиторий**:
   ```bash
   git clone https://github.com/<ваш-username>/monitoring-system.git
   cd monitoring-system
