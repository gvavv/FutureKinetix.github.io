# Как захостить сайт FutureKinetix и получить ссылку

Сайт **полностью статический**: 6 HTML-файлов, все изображения и стили встроены внутрь.
Никакой серверный код, базы данных и сборка не нужны — подходит любой статический хостинг.

**Папка для публикации: `site/publish/`** (в ней только 6 страниц, ~5,2 МБ):
- `index.html` — главная
- `products.html` — все продукты
- `yarbo.html` — Yarbo
- `automation.html` — автоматизация
- `company.html` — о компании
- `contacts.html` — контакты

После деплоя вы получаете ссылку вида `https://имя.netlify.app` или `https://логин.github.io/репозиторий/` — её и отправляете кому нужно.

---

## Вариант 1. Netlify Drop — быстрее всего, без git (2 минуты)

1. Откройте <https://app.netlify.com/drop>
2. Перетащите папку `site/publish` прямо в окно браузера.
3. Через ~10 секунд появится ссылка вида `https://random-name.netlify.app` — её можно отправлять.
4. Чтобы сайт не удалился и получил красивое имя: зарегистрируйте бесплатный аккаунт Netlify → Site settings → Change site name → например `futurekinetix.netlify.app`.

Плюсы: бесплатно, HTTPS сразу, сжатие brotli включено.
Минусы: домен netlify.app (свой домен подключается в настройках сайта).

## Вариант 2. GitHub Pages — бесплатно и навсегда

1. Создайте аккаунт на <https://github.com> (если нет).
2. New repository → имя, например `aura-site` → Public.
3. В репозитории: **Add file → Upload files** → перетащите 6 файлов из `site/publish` → Commit.
4. Settings → Pages → Source: **Deploy from a branch** → Branch: `main`, folder `/ (root)` → Save.
5. Через 1–2 минуты сайт будет по адресу `https://ВАШ_ЛОГИН.github.io/aura-site/`.

Или через терминал (если установлен git):

```bash
cd site/publish
git init && git add . && git commit -m "FutureKinetix site"
git branch -M main
git remote add origin https://github.com/ЛОГИН/aura-site.git
git push -u origin main
# затем включить Pages в Settings → Pages (как в шаге 4)
```

## Вариант 3. Одной командой (Vercel / Surge / Cloudflare)

Нужен Node.js (команда `npx` поставит утилиту сама), аккаунт создастся по e-mail в процессе:

```bash
# Vercel
npx vercel deploy site/publish --prod

# Surge (самый простой CLI)
npx surge site/publish futurekinetix.surge.sh

# Cloudflare Pages (wrangler)
npx wrangler pages deploy site/publish --project-name=aura
```

Либо Cloudflare/Vercel через веб: Dashboard → Pages/Projects → **Direct upload** → перетащить `site/publish`.

## Вариант 4. Платный хостинг в РФ + свой домен (солидно для компании)

Подойдёт, когда нужна ссылка вида `https://futurekinetix.ru`:

1. Купите домен (reg.ru, nic.ru) — ~300–900 ₽/год за `.ru`.
2. Возьмите статический хостинг или облако: Timeweb, Beget, Selectel, Yandex Cloud Object Storage.
   На Timeweb/Beget «сайт из папки» стоит ~100–200 ₽/мес; в Yandex S3 + CDN — копейки за трафик.
3. Загрузите файлы из `site/publish` в корень сайта (панель → файловый менеджер → загрузить).
4. Привяжите домен в панели хостинга и пропишите NS-серверы регистратора.
5. Включите HTTPS (Let's Encrypt) — на Timeweb/Beget одной кнопкой.

Для юрлиц это также закрывает вопрос «сайт должен быть на нашем домене» для рекламы и карт (2ГИС, Яндекс.Карты).

---

## Как отправить ссылку

- Полученный URL (например `https://futurekinetix.netlify.app`) просто вставляется в письмо/мессенджер/КП.
- Красиво смотрится короткая ссылка на свой домен: `futurekinetix.ru` (вариант 4).
- Для QR-визиток/буклетов: сгенерируйте QR на полученный URL (любой бесплатный генератор).

## Полезные замечания

- **Видео Yarbo** на странице подгружаются с YouTube — у зрителей нужен интернет (как и для любого сайта).
- Страницы тяжеловаты (фото в base64): Netlify/Vercel/Cloudflare автоматически жмут brotli/gzip — реальный трафик будет ~на 30–40 % меньше размера файлов.
- Если правите сайт через `site/build.py`, после пересборки заново скопируйте 6 файлов в `dist/` и нажмите **Deploy/Re-deploy** (или просто замените файлы в панели хостинга).
- Проверьте после деплоя: переходы между 6 страницами, форму на `contacts.html`, видео на `yarbo.html`.

---

# Приём заявок с сайта (куда приходят письма)

Форма на `contacts.html` работает по одному из четырёх сценариев (настраивается в `site/build.py`, константы `FORM_ENDPOINT`, `WEB3_KEY`, `MAIL_TO`):

1. **Formspree (рекомендуется, 5 мин).** Зарегистрируйтесь на formspree.io (бесплатно, 50 заявок/мес), создайте форму, скопируйте адрес вида `https://formspree.io/f/XXXXXXX` и вставьте в `FORM_ENDPOINT` в `build.py`. Затем `python3 build.py`, скопируйте страницы в `publish/`, задеплойте. Заявки приходят на почту, указанную в Formspree.
2. **Web3Forms.** На web3forms.com укажите свой e-mail — получите ключ. В `build.py`: `FORM_ENDPOINT='https://api.web3forms.com/submit'`, `WEB3_KEY='ваш-ключ'`. Пересоберите и задеплойте.
3. **Netlify Forms.** Если сайт за_hosted_ на Netlify — ничего настраивать не нужно: заявки падают в Netlify → Forms, а почтовые уведомления включаются в Site settings → Form notifications.
4. **Fallback без настроек.** Если `FORM_ENDPOINT` пуст и хостинг не Netlify, при отправке откроется почтовый клиент посетителя с готовым письмом на `futurekinetix@ya.ru` (тема и все поля подставлены). Это запасной вариант — лучше подключить п.1 или п.2.

После подключения любого сервиса сообщение об успешной отправке посетителю показывается прямо на странице.
