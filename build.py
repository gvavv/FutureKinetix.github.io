#!/usr/bin/env python3
"""Dependency-free GitHub Pages build. Output: dist/."""
from pathlib import Path
from string import Template
from html import escape
from html.parser import HTMLParser
from statistics import mean
import json
import shutil

ROOT = Path(__file__).resolve().parent
PAGES = [
    ('index.html', 'home.html', 'FutureKinetix — робототехника и автоматизация', 'Роботизированные системы, индивидуальная автоматизация, установка и сервис.'),
    ('yarbo.html', 'yarbo.html', 'Yarbo и навесное оборудование | FutureKinetix', 'Модульные роботы Yarbo, тележки, щётки, отвалы, российские ценовые ориентиры и обслуживание.'),
    ('products.html', 'products.html', 'Роботизированные системы | FutureKinetix', 'Роботы для доставки, склада, сервиса, уборки и производства.'),
    ('automation.html', 'automation.html', 'Индивидуальная автоматизация | FutureKinetix', 'Разработка систем роботизации, технического зрения и управления роботами.'),
    ('humanoids.html', 'humanoids.html', 'Гуманоидные роботы | FutureKinetix', 'Подбор гуманоидных платформ, прикладные сценарии и интеграция.'),
    ('service.html', 'service.html', 'Установка, настройка и обслуживание роботов | FutureKinetix', 'Услуги установки, настройки, диагностики, обслуживания и технической поддержки.'),
    ('company.html', 'company.html', 'О компании | FutureKinetix', 'Поставка роботов, инженерная разработка и сопровождение роботизированных систем.'),
    ('contacts.html', 'contacts.html', 'Контакты | FutureKinetix', 'Связаться с FutureKinetix по вопросам оборудования, разработки и сервиса.'),
]
NAVIGATION = [('yarbo.html','Yarbo'), ('products.html','Роботы'), ('automation.html','Решения'), ('service.html','Сервис'), ('company.html','Компания'), ('contacts.html','Контакты')]
ARROW = '<svg class="arrow-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 19 19 5M5 5h14v14"/></svg>'

def render(name, **values):
    return Template((ROOT/'src'/name).read_text()).substitute(**values)

def rub(value):
    return f'{value:,.0f}'.replace(',', '\u00a0') + ' ₽'

def price_label(item):
    if not item['prices']:
        return 'По запросу'
    average = round(mean(item['prices']) / 100) * 100 if len(item['prices']) > 1 else item['prices'][0]
    return ('≈ ' if len(item['prices']) > 1 else '') + rub(average)


def accessory_content(data):
    icons = {
        'cart': 'M3 9h23l-3 14H7zM2 5l4 4M9 23v4m13-4v4',
        'brush': 'M4 9h22v10H4zM8 19l-3 7m8-7-1 7m7-7 1 7m5-7 3 7',
        'plow': 'M5 8Q15 3 27 8v17Q15 20 5 25zM15 6v17',
    }
    cards = []
    rows = []
    for i,item in enumerate(data['items']):
        if i < 3:
            icon = f'<svg class="attachment-icon" viewBox="0 0 32 32" aria-hidden="true"><path d="{icons[item["icon"]]}"/></svg>'
            cards.append(f'<article class="attachment-card">{icon}<span class="eyebrow">{escape(item["kind"])}</span><h3>{escape(item["name"])}</h3><p class="attachment-model">{escape(item["model"])}</p><p>{escape(item["description"])}</p><div class="attachment-price">{price_label(item)}</div><a class="text-link" href="#contact">Подобрать оснастку ↗</a></article>')
        else:
            rows.append(f'<tr><th scope="row"><strong>{escape(item["name"])}</strong><span>{escape(item["description"])}</span></th><td>{price_label(item)}</td><td>Совместимость и состав уточняются</td></tr>')
    return ''.join(cards), ''.join(rows)

def catalog_product_content(data):
    cards = []
    for item in data['catalog_products']:
        cards.append(
            f'<article class="catalog-card">'
            f'<div class="catalog-card__media"><img src="assets/site/images/{escape(item["image"])}" alt="{escape(item["name"])}" loading="lazy"></div>'
            f'<div class="catalog-card__body"><span class="eyebrow">{escape(item["category"])} · {escape(item["tag"])}</span>'
            f'<h3>{escape(item["name"])}</h3><p>{escape(item["description"])}</p>'
            f'<div class="catalog-card__meta"><span>Арт. {escape(item["article"])}</span><strong>{rub(item["price"])}</strong></div>'
            f'<a class="text-link" href="#contact">Запросить подбор ↗</a></div></article>'
        )
    return ''.join(cards)

def main():
    products = json.loads((ROOT/'data/products.json').read_text())
    accessories = json.loads((ROOT/'data/accessories.json').read_text())
    cards = []
    for c in products['configurations']:
        c = {k:(escape(v) if isinstance(v, str) else v) for k,v in c.items()}
        cards.append(f'<article class="config-card"><div class="config-card__media"><img src="assets/site/images/{c["image"]}" alt="{c["name"]}" loading="lazy"></div><div class="config-card__body"><span class="eyebrow">{c["title"]}</span><h3>{c["name"]}</h3><p>{c["description"]}</p><div class="config-card__price">{rub(c["price"])}</div><p class="attachment-model">Арт. {c["article"]}</p><a class="text-link" href="#contact">Запросить подбор ↗</a></div></article>')
    modules = []
    for c in products['modules']:
        c = {k:(escape(v) if isinstance(v, str) else v) for k,v in c.items()}
        modules.append(f'<article class="module-card"><div class="module-card__media"><img src="assets/site/images/{c["image"]}" alt="{c["name"]}" loading="lazy"></div><div><span class="eyebrow">{c["season"]}</span><h3>{c["name"]}</h3><p>{c["description"]}</p><div class="attachment-price">{rub(c["price"])}</div><p class="attachment-model">Арт. {c["article"]}</p></div></article>')
    specs = ''.join(f'<tr><th scope="row">{escape(k)}</th><td>{escape(v)}</td></tr>' for k,v in products['specifications'])
    accessory_cards, accessory_rows = accessory_content(accessories)
    catalog_products = catalog_product_content(products)
    dist = ROOT/'dist'
    if dist.exists(): shutil.rmtree(dist)
    dist.mkdir()
    shutil.copytree(ROOT/'assets/site', dist/'assets/site')
    (dist/'.nojekyll').touch()
    for path,source,title,description in PAGES:
        nav = ''.join(f'<a href="{href}"'+(' aria-current="page"' if path == href else '')+f'>{label}</a>' for href,label in NAVIGATION)
        content = render(source, configurations=''.join(cards), modules=''.join(modules), catalog_products=catalog_products, specifications=specs, accessory_cards=accessory_cards, accessory_rows=accessory_rows, price_method=escape(accessories['method']), price_date=escape(products.get('updated_at', '')))
        html = render('layout.html', title=title, description=description, page=path[:-5], content=content, navigation=nav)
        html = html.replace('↗', ARROW).replace('↓', '<svg class="arrow-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v18M5 14l7 7 7-7"/></svg>')
        (ROOT/path).write_text(html)
        (dist/path).write_text(html)
    validate(dist)
    print(f'Built and checked {len(PAGES)} pages in dist/.')

def validate(dist):
    class Validator(HTMLParser):
        def handle_starttag(self, tag, attrs):
            for key,value in attrs:
                if key in ('href','src') and value and not value.startswith(('http','mailto:','tel:','#','data:')):
                    from urllib.parse import urlsplit
                    target = urlsplit(value).path
                    assert (dist/target).exists(), value
    for path,*_ in PAGES:
        Validator().feed((dist/path).read_text())

if __name__ == '__main__':
    main()
