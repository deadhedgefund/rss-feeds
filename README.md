# 📡 RSS Feeds Generator

[![Update Feeds](https://github.com/deadhedgefund/rss-feeds/actions/workflows/update.yml/badge.svg)](https://github.com/deadhedgefund/rss-feeds/actions/workflows/update.yml)
[![Feedly](https://img.shields.io/badge/Feedly-Compatible-2bb24c?logo=feedly&logoColor=white)](https://feedly.com)
[![GitHub Pages](https://img.shields.io/badge/Hosted_on-GitHub_Pages-blue?logo=github)](https://deadhedgefund.github.io/rss-feeds/)

Персональный автоматический генератор RSS-лент для сайтов и инженерных блогов, у которых нет встроенной поддержки RSS. 

Все фиды генерируются автоматически через **GitHub Actions** каждые 4 часа и раздаются статикой через **GitHub Pages**, что обеспечивает максимальную скорость и 100% совместимость с любыми RSS-ридерами (Feedly, Inoreader, Apple News и др.).

---

## 📋 Доступные фиды

| Источник | Оригинальный сайт | Ссылка на RSS (скопируй в Feedly) |
| :--- | :--- | :--- |
| **Uber Engineering** | [uber.com/blog/engineering](https://www.uber.com/en-US/blog/engineering/) | [`https://deadhedgefund.github.io/rss-feeds/feeds/uber.xml`](https://deadhedgefund.github.io/rss-feeds/feeds/uber.xml) |

---

## 🚀 Как подключить к Feedly

1. Скопируй нужную ссылку на `.xml` из таблицы выше.
2. В [Feedly](https://feedly.com) нажми **«Follow New Sources»** (или значок `+`).
3. Вставь ссылку в поиск и нажми **Follow**.

---

## 🛠 Архитектура проекта

```text
rss-feeds/
├── .github/workflows/
│   └── update.yml        # Расписание и запуск пайплайна (cron)
├── scrapers/             # Модули скрапинга для каждого сайта
│   ├── __init__.py
│   └── uber.py           # Парсер блога Uber
├── feeds/                # Сгенерированные RSS 2.0 XML файлы
│   └── uber.xml
├── main.py               # Главный скрипт сборки фидов
└── requirements.txt      # Зависимости Python
