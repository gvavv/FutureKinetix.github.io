# FutureKinetix — этап 1

Главная и визуальный прототип Yarbo в ветке `codex/site-rebuild`. Публикация требует отдельного утверждения концепции.

## Локальный запуск

Требуется Python 3. В корне репозитория:

```sh
python3 build.py
python3 -m http.server 4173 --directory dist
```

Открыть http://localhost:4173/ и http://localhost:4173/yarbo.html.

Редактировать шаблоны в `src/`, продукты в `data/products.json`, стили и поведение в `assets/site/`. Повторить сборку после изменений. `dist/` не хранится в Git; корневые `index.html`/`yarbo.html` генерируются той же сборкой. Старые страницы не входят в новую сборку.

- [Архитектура и информационная структура](docs/ARCHITECTURE.md)
- [Дизайн-система](docs/DESIGN-SYSTEM.md)
- [Анализ референсов](docs/REFERENCES.md)
- [Источники и статус медиа](docs/MEDIA.md)
- [Визуальная проверка и скриншоты](docs/QA.md)
