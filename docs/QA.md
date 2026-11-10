# Проверка многостраничной версии

Реальный Chromium через Playwright, локальная сборка `dist/`, HTTP-сервер 4173. Восемь страниц × семь ширин = 56 полноразмерных скриншотов, viewport height 1000, device scale factor 1.

## Скриншоты

- Главная: [320 px](qa/index-320.png), [375 px](qa/index-375.png), [430 px](qa/index-430.png), [768 px](qa/index-768.png), [1024 px](qa/index-1024.png), [1440 px](qa/index-1440.png), [1920 px](qa/index-1920.png).
- Yarbo: [320 px](qa/yarbo-320.png), [375 px](qa/yarbo-375.png), [430 px](qa/yarbo-430.png), [768 px](qa/yarbo-768.png), [1024 px](qa/yarbo-1024.png), [1440 px](qa/yarbo-1440.png), [1920 px](qa/yarbo-1920.png).
- Роботы: [320 px](qa/products-320.png), [375 px](qa/products-375.png), [430 px](qa/products-430.png), [768 px](qa/products-768.png), [1024 px](qa/products-1024.png), [1440 px](qa/products-1440.png), [1920 px](qa/products-1920.png).
- Решения: [320 px](qa/automation-320.png), [375 px](qa/automation-375.png), [430 px](qa/automation-430.png), [768 px](qa/automation-768.png), [1024 px](qa/automation-1024.png), [1440 px](qa/automation-1440.png), [1920 px](qa/automation-1920.png).
- Гуманоиды: [320 px](qa/humanoids-320.png), [375 px](qa/humanoids-375.png), [430 px](qa/humanoids-430.png), [768 px](qa/humanoids-768.png), [1024 px](qa/humanoids-1024.png), [1440 px](qa/humanoids-1440.png), [1920 px](qa/humanoids-1920.png).
- Сервис: [320 px](qa/service-320.png), [375 px](qa/service-375.png), [430 px](qa/service-430.png), [768 px](qa/service-768.png), [1024 px](qa/service-1024.png), [1440 px](qa/service-1440.png), [1920 px](qa/service-1920.png).
- Компания: [320 px](qa/company-320.png), [375 px](qa/company-375.png), [430 px](qa/company-430.png), [768 px](qa/company-768.png), [1024 px](qa/company-1024.png), [1440 px](qa/company-1440.png), [1920 px](qa/company-1920.png).
- Контакты: [320 px](qa/contacts-320.png), [375 px](qa/contacts-375.png), [430 px](qa/contacts-430.png), [768 px](qa/contacts-768.png), [1024 px](qa/contacts-1024.png), [1440 px](qa/contacts-1440.png), [1920 px](qa/contacts-1920.png).

## Проверки и исправления

- Сборка всех восьми страниц и проверка локальных ссылок/ассетов.
- Переполнения документа, выходящие за экран заголовки/кнопки/изображения, ошибки JS и битые картинки: [results.json](qa/results.json).
- Визуально проверены desktop/mobile страницы и галерея Yarbo. Изображения сохраняют пропорции; товарные снимки не обрезаются, текст находится отдельно.
- Контакты 320 px: сокращён слишком длинный заголовок, вызывавший overflow.
- Таблица компонентов: исправлены ширины столбцов, чтобы источники не сжимались до узкой полосы; на телефоне предусмотрена локальная прокрутка.
- При расширении меню до шести пунктов breakpoint изменён на 1200 px; соответствующее поведение JS синхронизировано.
- Сервисные карточки перестроены в 2×2 на desktop и одну колонку на телефоне.
- Для фото манипулятора корректно сведён прозрачный фон на белый, без чёрных артефактов.
- Сохранены исправления этапа 1: SVG вместо отсутствующих глифов, одна колонка направлений на телефоне, постоянное доступное имя кнопки меню.

Меню, Escape, возврат фокуса и копирование email проверяются в `docs/interactions.cjs`. Ссылки tel/mailto работают как запуск соответствующего приложения; серверная отправка формы не заявляется. FAQ и источники цен — нативные details/summary.

## Повторение

После запуска локального сервера по README:

```sh
node docs/visual-qa.cjs
node docs/interactions.cjs
```

Playwright и Chromium нужны только для QA, не для работы сайта. Проверка в Safari/iOS/Firefox и на физических устройствах не проводилась. Сайт не публиковался.
