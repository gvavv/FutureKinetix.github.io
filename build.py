#!/usr/bin/env python3
"""Проверка статической сборки FutureKinetix.

Сайт публикуется из корня репозитория. Страницы редактируются как готовые
HTML-файлы, а этот скрипт проверяет комплектность и ссылки на общие ассеты.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
PAGES = ("index.html", "products.html", "yarbo.html", "automation.html", "company.html", "contacts.html")
ASSETS = ("styles.css", "site.js")


def main() -> int:
    missing = [name for name in (*PAGES, *ASSETS) if not (ROOT / name).exists()]
    if missing:
        print("Не хватает файлов:", ", ".join(missing))
        return 1

    errors = []
    for name in PAGES:
        text = (ROOT / name).read_text(encoding="utf-8")
        if "<!doctype html>" not in text.lower():
            errors.append(f"{name}: нет doctype")
        for asset in ASSETS:
            if asset not in text:
                errors.append(f"{name}: не подключён {asset}")

        for href in re.findall(r'href="([^"]+)"', text):
            target = href.split("#", 1)[0]
            if target and not target.startswith(("http:", "https:", "mailto:", "tel:")):
                if not (ROOT / target).exists():
                    errors.append(f"{name}: отсутствует ссылка {target}")

    if errors:
        print("\n".join(errors))
        return 1

    print(f"Проверено страниц: {len(PAGES)}. Статическая сборка готова к публикации из корня репозитория.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
