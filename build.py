#!/usr/bin/env python3
"""Dependency-free static build: python3 build.py; preview dist/ locally."""
from pathlib import Path
from string import Template
from html import escape
from html.parser import HTMLParser
import json, shutil
ROOT = Path(__file__).resolve().parent

def render(name, **values):
    return Template((ROOT / 'src' / name).read_text()).substitute(**values)

def main():
    products=json.loads((ROOT/'data/products.json').read_text())
    cards=[]
    for c in products['configurations']:
        c={k:escape(v) for k,v in c.items()}
        cards.append(f'''<article class="config-card"><div class="config-card__media"><img src="assets/site/images/{c['image']}" alt="{c['name']}" loading="lazy"></div><div class="config-card__body"><span class="eyebrow">{c['title']}</span><h3>{c['name']}</h3><p>{c['description']}</p><a class="text-link" href="#contact">Запросить подбор ↗</a></div></article>''')
    modules=[]
    for c in products['modules']:
        c={k:escape(v) for k,v in c.items()}
        modules.append(f'''<article class="module-card"><div class="module-card__media"><img src="assets/site/images/{c['image']}" alt="Модуль {c['name']}" loading="lazy"></div><div><span class="eyebrow">{c['season']}</span><h3>{c['name']}</h3><p>{c['description']}</p></div></article>''')
    specs=''.join(f'<tr><th scope="row">{escape(k)}</th><td>{escape(v)}</td></tr>' for k,v in products['specifications'])
    pages=[('index.html','home.html','home','FutureKinetix — робототехника и автоматизация','Роботы Yarbo для частных территорий, роботизированные системы для бизнеса и индивидуальная автоматизация.'),('yarbo.html','yarbo.html','product','Yarbo — модульные роботы | FutureKinetix','Yarbo Snow Blower, модульная система, конфигурации и подбор оборудования для вашего участка.')]
    dist=ROOT/'dist'
    if dist.exists(): shutil.rmtree(dist)
    dist.mkdir(); shutil.copytree(ROOT/'assets/site',dist/'assets/site'); (dist/'.nojekyll').touch()
    for path,source,page,title,description in pages:
        content=render(source,configurations=''.join(cards),modules=''.join(modules),specifications=specs)
        html=render('layout.html',title=title,description=description,page=page,content=content,yarbo_active='aria-current="page"' if page=='product' else '')
        html=html.replace('↗', '<svg class="arrow-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 19 19 5M5 5h14v14"/></svg>').replace('↓', '<svg class="arrow-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v18M5 14l7 7 7-7"/></svg>')
        (ROOT/path).write_text(html); (dist/path).write_text(html)
    class Validator(HTMLParser):
        def handle_starttag(self,tag,attrs):
            for k,v in attrs:
                if k in ('href','src') and v and not v.startswith(('http','mailto:','tel:','#','data:')):
                    assert (dist/v.split('#')[0]).exists(),v
    for path,*_ in pages: Validator().feed((dist/path).read_text())
    print('Built and checked 2 pages in dist/. Legacy pages remain in Git and the repository root.')
if __name__=='__main__':main()
