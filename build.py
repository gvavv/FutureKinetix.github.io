#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builder of the multi-page FutureKinetix site."""
import base64, pathlib, urllib.parse

ROOT = pathlib.Path(__file__).parent

# === ПРИЁМ ЗАЯВОК С САЙТА ===
# 1) Formspree: зарегистрируйтесь на formspree.io, создайте форму и вставьте её адрес:
#    FORM_ENDPOINT = 'https://formspree.io/f/XXXXXXX'
# 2) Web3Forms: на web3forms.com укажите свою почту и получите ключ:
#    FORM_ENDPOINT = 'https://api.web3forms.com/submit' и WEB3_KEY = 'ваш-ключ'
# 3) Хостинг на Netlify: заявки собираются автоматически (Netlify Forms) — оставьте пустым.
# 4) Если пусто и хостинг не Netlify: fallback — откроется почтовый клиент посетителя
#    с готовым письмом на MAIL_TO.
FORM_ENDPOINT = ''
WEB3_KEY = ''
MAIL_TO = 'futurekinetix@ya.ru'

# === ЛОГОТИП: концепт №1 «Kinetic F» (оригинальный знак, прозрачный фон) ===
LOGO_B64 = base64.b64encode((ROOT/'brand/fk-kinetic-128.png').read_bytes()).decode()
FAV_B64 = base64.b64encode((ROOT/'brand/fk-kinetic-64.png').read_bytes()).decode()
def logo_svg(gid):
    return (f'<img src="data:image/png;base64,{LOGO_B64}" alt="Логотип FutureKinetix" width="40" height="40" style="width:40px;height:40px">')
FAV_HREF = 'data:image/png;base64,' + FAV_B64

def b64(p):
    return 'data:image/jpeg;base64,' + base64.b64encode((ROOT/p).read_bytes()).decode()

IMG = {
 'collage': b64('img/collage.jpg'),
 'hero': b64('img/yarbo/web/hero.jpg'), 'studio': b64('img/yarbo/web/studio.jpg'),
 'snow': b64('img/yarbo/web/snow.jpg'), 'lawn': b64('img/yarbo/web/lawn.jpg'),
 'leaves': b64('img/yarbo/web/leaves.jpg'), 'towing': b64('img/yarbo/web/towing.jpg'),
 'modules': b64('img/yarbo/web/modules.jpg'), 'snowmodule': b64('img/yarbo/web/snowmodule.jpg'),
 'bundle': b64('img/yarbo/web/bundle.jpg'), 'box': b64('img/yarbo/web/box.jpg'),
 'blade': b64('img/yarbo/web/blade.jpg'), 'lineup': b64('img/yarbo/web/lineup.jpg'),
 'yt1': b64('img/yarbo/yt1.jpg'), 'yt2': b64('img/yarbo/yt2.jpg'), 'yt3': b64('img/yarbo/yt3.jpg'),
 'clean': b64('img/cat/web/clean.jpg'), 'warehouse': b64('img/cat/web/warehouse.jpg'),
 'arm': b64('img/cat/web/arm.jpg'), 'delivery': b64('img/cat/web/delivery.jpg'),
 'drone': b64('img/cat/web/drone.jpg'), 'dog': b64('img/cat/web/dog.jpg'),
}

CSS = """
:root{--bg:#07090d;--bg2:#0b1017;--card:rgba(17,24,35,.72);--line:#1d2a39;--line2:#27384b;--text:#e9f0f6;--muted:#94a5b6;--dim:#6b7d8f;--teal:#2dd4bf;--cyan:#38bdf8;--violet:#8b5cf6;--yarbo:#f5c518;--grad:linear-gradient(120deg,#2dd4bf 0%,#38bdf8 48%,#8b5cf6 100%);--shadow:0 24px 60px rgba(0,0,0,.45)}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:92px}
body{background:var(--bg);color:var(--text);font-family:"Inter","SF Pro Text",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{max-width:100%;display:block;height:auto}a{color:inherit;text-decoration:none}ul{list-style:none}
.wrap{max-width:1200px;margin:0 auto;padding:0 24px}
h1,h2,h3,h4{line-height:1.15;letter-spacing:-.02em;font-weight:800}
h2{font-size:clamp(28px,4vw,44px)}h3{font-size:20px}
.grad-text{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.eyebrow{display:inline-flex;align-items:center;gap:10px;font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--teal)}
.eyebrow::before{content:"";width:26px;height:2px;background:var(--grad);border-radius:2px}
.section{padding:90px 0}.section-head{max-width:780px;margin-bottom:48px}
.section-head p{color:var(--muted);margin-top:16px;font-size:17px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;border:none;cursor:pointer;font:inherit;font-weight:700;border-radius:14px;padding:15px 28px;transition:.25s;white-space:nowrap}
.btn-primary{background:var(--grad);color:#04121a;box-shadow:0 10px 30px rgba(45,212,191,.28)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 16px 40px rgba(56,189,248,.35)}
.btn-ghost{background:transparent;color:var(--text);border:1px solid var(--line2)}
.btn-ghost:hover{border-color:var(--teal);color:var(--teal)}
.btn-sm{padding:11px 20px;font-size:14px;border-radius:12px}.btn-wide{width:100%}
header{position:fixed;inset:0 0 auto 0;z-index:100;transition:.3s;border-bottom:1px solid transparent}
header.scrolled{background:rgba(7,9,13,.85);backdrop-filter:blur(16px);border-bottom-color:var(--line)}
.nav{display:flex;align-items:center;justify-content:space-between;height:76px;gap:24px}
.logo{display:flex;align-items:center;gap:12px;font-weight:800}
.logo-mark{width:40px;height:40px;flex:none;display:grid;place-items:center}
.logo-name{font-size:15px;line-height:1.1}.logo-name small{display:block;font-size:9.5px;font-weight:600;letter-spacing:.2em;color:var(--muted)}
.nav-links{display:flex;gap:26px;font-size:14.5px;font-weight:600;color:var(--muted)}
.nav-links a:hover{color:var(--text)}
.nav-links a.active{color:var(--text);position:relative}
.nav-links a.active::after{content:"";position:absolute;left:0;right:0;bottom:-8px;height:2px;background:var(--grad);border-radius:2px}
.nav-cta{display:flex;align-items:center;gap:12px}
.burger{display:none;background:none;border:none;cursor:pointer;width:40px;height:40px;flex-direction:column;gap:5px;align-items:center;justify-content:center}
.burger span{width:22px;height:2px;background:var(--text);border-radius:2px}
.mobile-menu{display:none;position:fixed;inset:76px 0 auto 0;background:rgba(7,9,13,.97);backdrop-filter:blur(20px);border-bottom:1px solid var(--line);padding:16px 24px 28px;z-index:99}
.mobile-menu a{display:block;padding:13px 4px;font-weight:600;color:var(--muted);border-bottom:1px solid var(--line)}
.mobile-menu a.active{color:var(--teal)}
.mobile-menu.open{display:block}
.hero{position:relative;padding:168px 0 84px;overflow:hidden}
.hero::before{content:"";position:absolute;inset:-20% -10% auto -10%;height:120%;background:radial-gradient(42% 55% at 78% 18%,rgba(45,212,191,.15),transparent 65%),radial-gradient(38% 48% at 18% 8%,rgba(139,92,246,.15),transparent 65%);pointer-events:none}
.hero-grid{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center;position:relative}
.hero-badge{display:inline-flex;align-items:center;gap:10px;background:rgba(45,212,191,.08);border:1px solid rgba(45,212,191,.3);color:var(--teal);border-radius:999px;padding:8px 16px;font-size:13px;font-weight:700;margin-bottom:24px}
.hero-badge .dot{width:7px;height:7px;border-radius:50%;background:var(--teal);animation:pulse 2.2s infinite}
@keyframes pulse{70%{box-shadow:0 0 0 9px rgba(45,212,191,0)}100%{box-shadow:0 0 0 0 rgba(45,212,191,0)}}
h1{font-size:clamp(34px,4.6vw,54px)}
.hero-sub{color:var(--muted);font-size:18px;margin:22px 0 34px;max-width:540px}
.hero-actions{display:flex;gap:14px;flex-wrap:wrap}
.hero-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:50px;border-top:1px solid var(--line);padding-top:28px}
.stat b{display:block;font-size:24px;font-weight:800}.stat span{font-size:13px;color:var(--dim)}
.hero-visual{position:relative}
.hero-visual .glow{position:absolute;inset:10%;background:radial-gradient(50% 50% at 50% 55%,rgba(45,212,191,.2),transparent 70%);filter:blur(30px)}
.hero-visual img{position:relative;border-radius:26px;box-shadow:var(--shadow);border:1px solid var(--line)}
.hero-float{position:absolute;background:rgba(12,18,26,.88);backdrop-filter:blur(10px);border:1px solid var(--line2);border-radius:14px;padding:11px 16px;font-size:13px;font-weight:600;display:flex;align-items:center;gap:10px;box-shadow:var(--shadow)}
.hf-1{top:5%;left:-3%}.hf-2{bottom:8%;right:-2%}
.pagehead{padding:168px 0 56px;position:relative;overflow:hidden}
.pagehead::before{content:"";position:absolute;inset:-30% -10% auto -10%;height:130%;background:radial-gradient(40% 60% at 70% 20%,rgba(45,212,191,.12),transparent 65%),radial-gradient(36% 50% at 20% 10%,rgba(139,92,246,.12),transparent 65%);pointer-events:none}
.pagehead .wrap{position:relative}
.pagehead p{color:var(--muted);font-size:17px;margin-top:18px;max-width:760px}
.strip{border-block:1px solid var(--line);background:var(--bg2)}
.strip .wrap{display:flex;gap:34px;flex-wrap:wrap;justify-content:space-between;padding:20px 24px}
.ds{display:flex;align-items:center;gap:12px;font-size:14px;font-weight:600;color:var(--muted)}.ds b{color:var(--text)}
.band{display:grid;grid-template-columns:1.05fr .95fr;gap:44px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:28px;padding:34px;box-shadow:var(--shadow)}
.band img{border-radius:20px;border:1px solid var(--line);width:100%;aspect-ratio:4/3;object-fit:cover}
.band .tags{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:12px}
.tag{font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;border-radius:999px;padding:6px 13px}
.tag-teal{background:rgba(45,212,191,.12);color:var(--teal);border:1px solid rgba(45,212,191,.3)}
.tag-yellow{background:rgba(245,197,24,.1);color:var(--yarbo);border:1px solid rgba(245,197,24,.35)}
.band h3{font-size:clamp(24px,2.6vw,32px)}
.price-line{font-size:clamp(26px,2.6vw,34px);font-weight:800;margin:14px 0 4px}
.price-sub{color:var(--dim);font-size:13.5px}
.feat-list{margin:18px 0 24px;display:grid;gap:10px}
.feat-list li{display:flex;gap:12px;align-items:flex-start;font-size:15px;color:#c9d6e2}
.feat-list svg{flex:none;margin-top:3px}
.mini-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.mini-card{background:var(--card);border:1px solid var(--line);border-radius:20px;overflow:hidden;display:flex;flex-direction:column;transition:.25s}
.mini-card:hover{transform:translateY(-4px);border-color:rgba(45,212,191,.4)}
.mini-card .ph{aspect-ratio:16/9;overflow:hidden;border-bottom:1px solid var(--line)}
.mini-card .ph img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.mini-card:hover .ph img{transform:scale(1.06)}
.mini-body{padding:20px 22px 22px;display:flex;flex-direction:column;flex:1}
.mini-body h4{font-size:17px;margin-bottom:6px}
.mini-body p{font-size:13.5px;color:var(--muted);flex:1}
.mini-price{margin-top:12px;font-weight:800;font-size:17px}
.mini-price span{display:block;font-size:12px;color:var(--dim);font-weight:600}
.mini-body a{margin-top:12px;color:var(--teal);font-weight:700;font-size:14px}
.cat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.cat-card{background:var(--card);border:1px solid var(--line);border-radius:22px;overflow:hidden;display:flex;flex-direction:column;transition:.25s;scroll-margin-top:100px}
.cat-card:hover{transform:translateY(-5px);border-color:rgba(45,212,191,.4)}
.cat-card .ph{aspect-ratio:16/10;overflow:hidden;border-bottom:1px solid var(--line)}
.cat-card .ph img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.cat-card:hover .ph img{transform:scale(1.06)}
.cat-body{padding:24px 26px 26px;display:flex;flex-direction:column;flex:1}
.cat-body h4{font-size:19px;margin-bottom:8px}
.cat-body>p{font-size:14px;color:var(--muted);margin-bottom:14px}
.cat-feats{display:grid;gap:8px;margin-bottom:16px}
.cat-feats li{display:flex;gap:10px;font-size:13.5px;color:#c9d6e2;align-items:flex-start}
.cat-feats svg{flex:none;margin-top:3px}
.cat-price{font-size:20px;font-weight:800;margin-top:auto}
.cat-price span{display:block;font-size:12px;color:var(--dim);font-weight:600}
.cat-body .btn{margin-top:16px}
.note-box{margin-top:26px;border:1px dashed var(--line2);border-radius:18px;padding:22px 26px;color:var(--muted);font-size:14.5px;display:flex;gap:18px;align-items:center;flex-wrap:wrap;justify-content:space-between}
.auto-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.auto-card{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:28px}
.auto-num{font-size:38px;font-weight:800;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.auto-card h4{margin:12px 0 8px;font-size:17px}.auto-card p{font-size:14px;color:var(--muted)}
.chips{display:flex;gap:12px;flex-wrap:wrap}
.chip{border:1px solid var(--line2);border-radius:999px;padding:10px 20px;font-size:14px;font-weight:600;color:var(--muted)}
.steps5{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}
.step{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:24px}
.step .num{font-size:34px;font-weight:800;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.step h4{margin:10px 0 6px;font-size:16px}.step p{font-size:13.5px;color:var(--muted)}
.img-duo{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.img-duo figure{border-radius:22px;overflow:hidden;border:1px solid var(--line);position:relative}
.img-duo img{width:100%;height:340px;object-fit:cover}
.img-duo figcaption{position:absolute;left:0;right:0;bottom:0;padding:16px 20px;font-size:14px;font-weight:600;background:linear-gradient(to top,rgba(0,0,0,.85),transparent)}
.gallery .main{border-radius:20px;overflow:hidden;border:1px solid var(--line);aspect-ratio:4/3;background:#0a0f15}
.gallery .main img{width:100%;height:100%;object-fit:cover;transition:opacity .35s}
.thumbs{display:flex;gap:12px;margin-top:14px}
.thumbs button{flex:1;border-radius:14px;overflow:hidden;border:2px solid transparent;cursor:pointer;padding:0;background:none;opacity:.6;transition:.25s}
.thumbs button img{aspect-ratio:4/3;object-fit:cover;width:100%}
.thumbs button.active{border-color:var(--teal);opacity:1}.thumbs button:hover{opacity:1}
.product-card{background:var(--card);border:1px solid var(--line);border-radius:28px;padding:34px;display:grid;grid-template-columns:1.05fr .95fr;gap:40px;box-shadow:var(--shadow)}
.rating{display:flex;align-items:center;gap:10px;margin:12px 0 16px;color:var(--muted);font-size:14px}
.stars{color:#fbbf24;letter-spacing:2px;font-size:15px}
.price{font-size:clamp(30px,3.2vw,40px);font-weight:800;letter-spacing:-.03em}
.installment{color:var(--teal);font-size:15px;font-weight:600;margin-top:4px}
.cfg-switch{display:flex;gap:10px;flex-wrap:wrap;margin:6px 0 20px}
.cfg-switch button{font:inherit;font-size:13.5px;font-weight:700;padding:10px 16px;border-radius:12px;border:1px solid var(--line2);background:transparent;color:var(--muted);cursor:pointer;transition:.2s}
.cfg-switch button.active{background:rgba(45,212,191,.1);border-color:var(--teal);color:var(--teal)}
.trust{display:flex;gap:22px;flex-wrap:wrap;margin-top:22px;color:var(--dim);font-size:13px}
.trust div{display:flex;align-items:center;gap:8px}
.box-strip{display:grid;grid-template-columns:.9fr 1.1fr;gap:40px;align-items:center;margin-top:26px;background:var(--card);border:1px solid var(--line);border-radius:24px;overflow:hidden}
.box-strip img{width:100%;height:100%;object-fit:cover}
.box-list{padding:30px 34px 30px 0}.box-list h3{margin-bottom:16px}
.box-list ul{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.box-list li{display:flex;gap:10px;font-size:14.5px;color:#c9d6e2;align-items:flex-start}
.box-list svg{flex:none;margin-top:4px}
.mod-banner{border-radius:24px;overflow:hidden;border:1px solid var(--line);margin-bottom:26px;box-shadow:var(--shadow)}
.mod-banner img{width:100%;height:440px;object-fit:cover;object-position:center 62%}
.mod-cards{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.mod-card{background:var(--card);border:1px solid var(--line);border-radius:20px;overflow:hidden;transition:.25s;display:flex;flex-direction:column}
.mod-card:hover{transform:translateY(-4px);border-color:var(--line2)}
.mod-card .ph{aspect-ratio:4/3;overflow:hidden;border-bottom:1px solid var(--line)}
.mod-card .ph img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.mod-card:hover .ph img{transform:scale(1.06)}
.mod-body{padding:20px 22px 24px;display:flex;flex-direction:column;flex:1}
.mod-card .code{font-size:11px;font-weight:700;letter-spacing:.14em;color:var(--dim);text-transform:uppercase}
.mod-card h4{font-size:17px;margin:8px 0 6px}.mod-card p{font-size:13.5px;color:var(--muted);flex:1}
.mod-price{margin-top:14px;font-weight:800;font-size:18px}
.mod-price span{font-size:12px;color:var(--dim);font-weight:600;display:block}
.pricelist{margin-top:22px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px 26px;display:flex;gap:26px;flex-wrap:wrap;align-items:center;font-size:14px;color:var(--muted)}
.pricelist b{color:var(--text)}.pricelist .pl-title{font-weight:800;color:var(--teal);letter-spacing:.1em;text-transform:uppercase;font-size:12px}
.sce-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.sce{border-radius:22px;overflow:hidden;position:relative;min-height:340px;border:1px solid var(--line);display:flex;flex-direction:column;justify-content:flex-end;padding:24px;isolation:isolate}
.sce img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;transition:transform .5s}
.sce:hover img{transform:scale(1.05)}
.sce::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(to top,rgba(5,8,12,.92) 8%,rgba(5,8,12,.35) 55%,rgba(5,8,12,.05))}
.sce .season{font-size:12px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--yarbo);margin-bottom:8px}
.sce h4{font-size:19px;margin-bottom:8px}.sce p{font-size:13.5px;color:#b9c7d4}
.video-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.video-card{position:relative;border-radius:20px;overflow:hidden;border:1px solid var(--line);aspect-ratio:16/9;background:#000;cursor:pointer}
.video-card img{width:100%;height:100%;object-fit:cover;opacity:.85;transition:.3s}
.video-card:hover img{opacity:1;transform:scale(1.03)}
.video-card .play{position:absolute;inset:0;display:grid;place-items:center}
.video-card .play span{width:64px;height:64px;border-radius:50%;background:rgba(7,10,15,.75);border:1px solid rgba(255,255,255,.25);display:grid;place-items:center;backdrop-filter:blur(6px);transition:.25s}
.video-card:hover .play span{transform:scale(1.08);background:rgba(45,212,191,.85)}
.video-card .cap{position:absolute;left:0;right:0;bottom:0;padding:14px 16px;font-size:13.5px;font-weight:600;background:linear-gradient(to top,rgba(0,0,0,.85),transparent)}
.video-card iframe{position:absolute;inset:0;width:100%;height:100%;border:none}
.specs-box{background:var(--card);border:1px solid var(--line);border-radius:24px;overflow:hidden}
.spec-tabs{display:flex;gap:6px;padding:14px;border-bottom:1px solid var(--line);flex-wrap:wrap;background:rgba(9,13,19,.6)}
.spec-tabs button{font:inherit;font-size:14px;font-weight:700;color:var(--muted);background:transparent;border:none;border-radius:11px;padding:11px 18px;cursor:pointer;transition:.2s}
.spec-tabs button.active{background:var(--grad);color:#04121a}
.spec-table{padding:10px 30px 26px}
.spec-row{display:grid;grid-template-columns:1fr 1.15fr;gap:24px;padding:15px 0;border-bottom:1px dashed var(--line);font-size:15px}
.spec-row:last-child{border-bottom:none}
.spec-row dt{color:var(--muted)}.spec-row dd{font-weight:600}
.cfg-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;align-items:stretch}
.cfg-card{background:var(--card);border:1px solid var(--line);border-radius:24px;padding:28px;display:flex;flex-direction:column;position:relative;transition:.25s}
.cfg-card:hover{transform:translateY(-5px)}
.cfg-card.hit{border-color:rgba(245,197,24,.5);box-shadow:0 0 0 1px rgba(245,197,24,.3),0 26px 60px rgba(245,197,24,.08)}
.hit-badge{position:absolute;top:-14px;left:50%;transform:translateX(-50%);background:var(--yarbo);color:#171204;font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;border-radius:999px;padding:6px 16px;white-space:nowrap}
.cfg-name{font-size:12px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--teal)}
.cfg-card h3{font-size:20px;margin:10px 0 4px}
.cfg-desc{color:var(--muted);font-size:13.5px;margin-bottom:16px}
.cfg-price{font-size:27px;font-weight:800;letter-spacing:-.03em}
.cfg-save{font-size:12.5px;color:var(--teal);font-weight:700;margin:6px 0 16px}
.cfg-list{display:grid;gap:9px;margin-bottom:24px}
.cfg-list li{display:flex;gap:10px;font-size:13.5px;color:#c9d6e2;align-items:flex-start}
.cfg-list svg{flex:none;margin-top:3px}
.cfg-card .btn{margin-top:auto}
.faq{max-width:820px;margin:0 auto}
.faq details{background:var(--card);border:1px solid var(--line);border-radius:16px;margin-bottom:12px;overflow:hidden}
.faq summary{cursor:pointer;padding:22px 26px;font-weight:700;font-size:16.5px;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:18px}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-size:24px;color:var(--teal);transition:.25s;flex:none}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq .a{padding:0 26px 24px;color:var(--muted);font-size:15px}
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:start}
.form{background:var(--card);border:1px solid var(--line);border-radius:24px;padding:34px;display:grid;gap:16px}
.form label{font-size:13px;font-weight:700;color:var(--muted);display:block;margin-bottom:7px}
.form input,.form select,.form textarea{width:100%;font:inherit;color:var(--text);background:rgba(7,10,15,.7);border:1px solid var(--line2);border-radius:13px;padding:14px 16px;outline:none;transition:.2s}
.form input:focus,.form select:focus,.form textarea:focus{border-color:var(--teal);box-shadow:0 0 0 3px rgba(45,212,191,.15)}
.form textarea{resize:vertical;min-height:96px}
.form-ok{display:none;background:rgba(45,212,191,.1);border:1px solid rgba(45,212,191,.4);color:var(--teal);border-radius:13px;padding:14px 18px;font-weight:600;font-size:14.5px}
.contact-info{display:grid;gap:16px}
.ci-card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:24px;display:flex;gap:16px;align-items:flex-start}
.ci-ico{width:46px;height:46px;flex:none;border-radius:13px;background:rgba(56,189,248,.1);border:1px solid rgba(56,189,248,.25);display:grid;place-items:center}
.ci-card b{display:block;margin-bottom:4px}.ci-card span{color:var(--muted);font-size:14.5px}
.cta-band{background:linear-gradient(120deg,rgba(45,212,191,.14),rgba(139,92,246,.14));border:1px solid var(--line2);border-radius:28px;padding:52px;text-align:center}
.cta-band h2{margin-bottom:14px}.cta-band p{color:var(--muted);max-width:560px;margin:0 auto 30px}
.comp-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.comp-stat{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:22px}
.comp-stat b{font-size:30px;font-weight:800;display:block}.comp-stat span{color:var(--muted);font-size:13px}
.dir-list{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.dir-list a{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 20px;font-weight:600;font-size:14.5px;color:var(--muted);display:flex;justify-content:space-between;gap:12px;transition:.2s}
.dir-list a:hover{color:var(--teal);border-color:rgba(45,212,191,.4)}
footer{border-top:1px solid var(--line);padding:56px 0 34px;background:var(--bg2)}
.f-grid{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:36px;margin-bottom:44px}
.f-col h5{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}
.f-col a{display:block;color:var(--muted);font-size:14.5px;padding:5px 0;transition:.2s}
.f-col a:hover{color:var(--teal)}
.f-about{color:var(--muted);font-size:14px;margin-top:16px;max-width:320px}
.f-bottom{border-top:1px solid var(--line);padding-top:26px;display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;color:var(--dim);font-size:13px}
.js .rv{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.js .rv.in{opacity:1;transform:none}
@media(max-width:1020px){
.nav-links{display:none}.burger{display:flex}.nav-cta .btn{display:none}
.hero-grid,.band,.box-strip,.contact-grid,.img-duo{grid-template-columns:1fr}
.box-list{padding:0 26px 28px}
.sce-grid{grid-template-columns:1fr 1fr}
.mini-grid,.cat-grid,.cfg-grid,.video-grid,.auto-grid,.steps5{grid-template-columns:1fr 1fr}
.mod-cards{grid-template-columns:1fr 1fr}
.hero-stats,.comp-stats{grid-template-columns:repeat(2,1fr)}
.hf-1{left:2%}.hf-2{right:2%}
}
@media(max-width:640px){
.section{padding:60px 0}
.sce-grid,.mini-grid,.cat-grid,.cfg-grid,.mod-cards,.video-grid,.f-grid,.box-list ul,.auto-grid,.steps5,.dir-list{grid-template-columns:1fr}
.hero{padding-top:130px}.pagehead{padding-top:130px}
.spec-row{grid-template-columns:1fr;gap:4px}
.product-card{padding:22px}.mod-banner img{height:240px}.cta-band{padding:34px 22px}
}
"""

CHECK = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none"><path d="m5 12.5 4.5 4.5L19 7.5" stroke="#2dd4bf" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

TOPICS = [
 "Тест-драйв Yarbo на моём участке",
 "Yarbo Core — 590 000 ₽",
 "Робот-газонокосилка Yarbo PRO (M1PRO) — 880 000 ₽",
 "Робот-снегоуборщик Yarbo (S1) — 880 000 ₽",
 "Комплект SNOW + LAWN — 1 170 000 ₽",
 "Модули Yarbo (косилка, снег, воздуходувка, триммер)",
 "Каталог: промышленные роботы-уборщики",
 "Каталог: складские роботы (AMR/AGV)",
 "Каталог: роборуки-манипуляторы",
 "Каталог: роботы-доставщики",
 "Каталог: дроны-доставщики",
 "Каталог: робособаки",
 "Автоматизация производства под ключ",
 "Другой запрос",
]
def topic_url(t): return 'contacts.html?topic=' + urllib.parse.quote(t)

NAV = [("index.html","Главная"),("products.html","Все продукты"),("yarbo.html","Yarbo"),("automation.html","Автоматизация"),("company.html","О компании"),("contacts.html","Контакты")]

def header(active):
    links = ''.join(f'<a href="{h}" class="{"active" if h==active else ""}">{n}</a>' for h,n in NAV)
    mlinks = ''.join(f'<a href="{h}" class="{"active" if h==active else ""}">{n}</a>' for h,n in NAV)
    return f"""<header id="header">
<div class="wrap nav">
<a class="logo" href="index.html"><span class="logo-mark">__LOGO_H__</span><span class="logo-name">FUTUREKINETIX<small>РОБОТЫ И АВТОМАТИЗАЦИЯ</small></span></a>
<nav class="nav-links">{links}</nav>
<div class="nav-cta"><a class="btn btn-primary btn-sm" href="{topic_url('Другой запрос')}">Подобрать робота</a><button class="burger" id="burger" aria-label="Меню"><span></span><span></span><span></span></button></div>
</div></header>
<div class="mobile-menu" id="mobileMenu">{mlinks}<a href="{topic_url('Другой запрос')}">Подобрать робота</a></div>"""

FOOT = """<footer><div class="wrap">
<div class="f-grid">
<div class="f-col"><a class="logo" href="index.html"><span class="logo-mark">__LOGO_F__</span><span class="logo-name">FUTUREKINETIX<small>РОБОТЫ И РОБОТИЗАЦИЯ</small></span></a><p class="f-about">Роботы для дома и бизнеса, роботизация и автоматизация производств под ключ. Официальные поставки Yarbo и промышленной робототехники.</p></div>
<div class="f-col"><h5>Продукты</h5><a href="products.html">Все продукты</a><a href="yarbo.html">Yarbo Y40</a><a href="yarbo.html#modules">Модули Yarbo</a><a href="yarbo.html#configs">Цены Yarbo</a></div>
<div class="f-col"><h5>Направления</h5><a href="automation.html">Автоматизация производств</a><a href="products.html#clean">Промышленная уборка</a><a href="products.html#warehouse">Складская логистика</a><a href="products.html#dog">Инспекция и охрана</a></div>
<div class="f-col"><h5>Компания</h5><a href="company.html">О компании</a><a href="yarbo.html#video">Видео</a><a href="yarbo.html#faq">FAQ</a><a href="contacts.html">Контакты</a></div>
</div>
<div class="f-bottom"><span>© <span id="year">2026</span> FutureKinetix. Все права защищены.</span><span>Yarbo® — товарный знак правообладателя. Цены РФ: прайс zimani.ru от 10.2026.</span></div>
</div></footer>"""

JS_COMMON = """
document.documentElement.classList.add('js');
const header=document.getElementById('header');
addEventListener('scroll',()=>header.classList.toggle('scrolled',scrollY>10),{passive:true});
const mm=document.getElementById('mobileMenu');
document.getElementById('burger').addEventListener('click',()=>mm.classList.toggle('open'));
mm.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>mm.classList.remove('open')));
const io=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target);}}),{threshold:.12});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
document.getElementById('year').textContent=new Date().getFullYear();
"""

def page(title, desc, active, body, js=''):
    html = f"""<!DOCTYPE html><html lang="ru"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="{FAV_HREF}">
<style>{CSS}</style></head><body>
{header(active)}
{body}
{FOOT}
<script>{JS_COMMON}{js}</script>
</body></html>"""
    return html.replace('__LOGO_H__', logo_svg('lh')).replace('__LOGO_F__', logo_svg('lf'))

def img(key, alt, extra=''):
    return f'<img src="{IMG[key]}" alt="{alt}" {extra}>'

# ================= INDEX =================
index_body = f"""
<section class="hero" id="top"><div class="wrap hero-grid">
<div>
<span class="hero-badge"><span class="dot"></span> Роботы · роботизация · автоматизация производств</span>
<h1>Техника, которая работает <span class="grad-text">вместо людей</span> — дома и на производстве</h1>
<p class="hero-sub">FutureKinetix поставляет и внедряет автономных роботов: от всесезонного Yarbo Y40 для участка до промышленных уборщиков, складских платформ, манипуляторов, курьеров, дронов и робособак.</p>
<div class="hero-actions"><a class="btn btn-primary" href="products.html">Все продукты</a><a class="btn btn-ghost" href="company.html">О компании</a></div>
<div class="hero-stats">
<div class="stat"><b class="grad-text">1 400+</b><span>роботов поставлено</span></div>
<div class="stat"><b class="grad-text">7</b><span>продуктовых линеек</span></div>
<div class="stat"><b class="grad-text">27</b><span>регионов сервиса</span></div>
<div class="stat"><b class="grad-text">14 дней</b><span>расчёт ROI проекта</span></div>
</div></div>
<div class="hero-visual"><div class="glow"></div>
{img('collage','Коллаж: Yarbo Y40 и промышленные роботы FutureKinetix — уборщики, складские, роборуки, доставщики, дроны, робособаки','width="1600" height="998"')}
<div class="hero-float hf-1"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="3" stroke="#2dd4bf" stroke-width="2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3" stroke="#2dd4bf" stroke-width="2" stroke-linecap="round"/></svg>Yarbo Y40: RTK-GPS, без проводов</div>
<div class="hero-float hf-2"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M4 17h16M6 17V9a6 6 0 0 1 12 0v8" stroke="#f5c518" stroke-width="2" stroke-linecap="round"/><circle cx="8" cy="17" r="2" stroke="#f5c518" stroke-width="2"/><circle cx="16" cy="17" r="2" stroke="#f5c518" stroke-width="2"/></svg>Yarbo + 6 классов пром-роботов</div>
</div></div></section>

<div class="strip"><div class="wrap">
<div class="ds"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 3 4 6v6c0 5 3.4 8.3 8 9 4.6-.7 8-4 8-9V6l-8-3Z" stroke="#2dd4bf" stroke-width="2" stroke-linejoin="round"/><path d="m9 12 2.2 2.2L15.5 10" stroke="#2dd4bf" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span><b>Официальные поставки</b> Yarbo и пром-робототехники</span></div>
<div class="ds"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M13 2 4.5 13.5H11L10 22l8.5-11.5H12L13 2Z" stroke="#2dd4bf" stroke-width="2" stroke-linejoin="round"/></svg><span><b>Своё интеграционное бюро</b>: линии под ключ</span></div>
<div class="ds"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M12 8v4l2.5 2.5" stroke="#2dd4bf" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="12" r="9" stroke="#2dd4bf" stroke-width="2"/></svg><span><b>Сервис 24/7</b> и подменная техника</span></div>
<div class="ds"><svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M4 20h16M6 20V9l6-5 6 5v11" stroke="#2dd4bf" stroke-width="2" stroke-linejoin="round"/></svg><span><b>Демо-зал и тест-драйвы</b> в Москве</span></div>
</div></div>

<section class="section"><div class="wrap">
<div class="section-head rv"><span class="eyebrow">Флагман для дома и участка</span>
<h2>Модульный всесезонный робот <span class="grad-text">Yarbo Y40</span></h2>
<p>Одно гусеничное шасси и сменные модули: косилка 50 см, снегоуборщик 61 см с выбросом 12 м, воздуходувка и триммер. Цены — официальный прайс Yarbo в РФ.</p></div>
<div class="band rv">
{img('snow','Yarbo Y40 с снегоуборочным модулем чистит снег зимой','loading="lazy"')}
<div>
<div class="tags"><span class="tag tag-yellow">Хит российского рынка</span><span class="tag tag-teal">Модульная система</span></div>
<h3>Yarbo Y40 Core + модули</h3>
<div class="rating"><span class="stars">★★★★★</span> 4.8 · 64 отзыва на eu.yarbo.com</div>
<div class="price-line">от 590 000 ₽</div>
<div class="price-sub">Прайс РФ (zimani.ru): Core 590 000 ₽ · M1PRO 880 000 ₽ · S1 880 000 ₽ · модули от 41 800 ₽</div>
<ul class="feat-list">
<li>{CHECK} Уклон до 35° (70 %): снег, грязь, мокрая трава</li>
<li>{CHECK} RTK-GPS + камеры и ультразвук — без ограничительных проводов</li>
<li>{CHECK} До 25 000 м² газона и до 650 м² снега за цикл</li>
</ul>
<div class="hero-actions"><a class="btn btn-primary" href="yarbo.html">Страница Yarbo</a><a class="btn btn-ghost" href="{topic_url('Тест-драйв Yarbo на моём участке')}">Тест-драйв</a></div>
</div></div>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
<div class="section-head rv"><span class="eyebrow">Каталог</span><h2>Шесть классов промышленной робототехники</h2>
<p>Цены «от» — по открытым рыночным данным на октябрь 2026. Точную комплектацию и стоимость считаем под задачу: свяжитесь с нами.</p></div>
<div class="mini-grid">
<div class="mini-card rv"><div class="ph">{img('clean','Промышленный робот-уборщик моет пол склада','loading="lazy"')}</div><div class="mini-body"><h4>Промышленные роботы-уборщики</h4><p>Автономная мойка и подметание складов, ТЦ, паркингов и аэропортов.</p><div class="mini-price">от 2 200 000 ₽<span>ориентир: Pudu CC1</span></div><a href="products.html#clean">Подробнее →</a></div></div>
<div class="mini-card rv"><div class="ph">{img('warehouse','Складской AMR-робот везёт стеллаж','loading="lazy"')}</div><div class="mini-body"><h4>Складские роботы (AMR/AGV)</h4><p>«Товар к человеку», буксировщики стеллажей, сортировка заказов.</p><div class="mini-price">от 1 200 000 ₽<span>класс Geek+ / Quicktron</span></div><a href="products.html#warehouse">Подробнее →</a></div></div>
<div class="mini-card rv"><div class="ph">{img('arm','Роборука-манипулятор на производственной линии','loading="lazy"')}</div><div class="mini-body"><h4>Роборуки-манипуляторы</h4><p>Коботы и пром-манипуляторы: сварка, упаковка, палетирование, сборка.</p><div class="mini-price">от 350 000 ₽<span>ориентир: Dobot MG400</span></div><a href="products.html#arm">Подробнее →</a></div></div>
<div class="mini-card rv"><div class="ph">{img('delivery','Курьерский робот-доставщик на тротуаре','loading="lazy"')}</div><div class="mini-body"><h4>Роботы-доставщики</h4><p>Тротуарные курьеры последней мили и сервисные доставщики в помещениях.</p><div class="mini-price">от 450 000 ₽<span>базовая модель курьера</span></div><a href="products.html#delivery">Подробнее →</a></div></div>
<div class="mini-card rv"><div class="ph">{img('drone','Грузовой дрон-доставщик несёт короб','loading="lazy"')}</div><div class="mini-body"><h4>Дроны-доставщики</h4><p>Грузовые БПЛА для медицины, вахты, геологии и e-commerce.</p><div class="mini-price">от 3 598 800 ₽<span>ориентир: DJI FlyCart 30</span></div><a href="products.html#drone">Подробнее →</a></div></div>
<div class="mini-card rv"><div class="ph">{img('dog','Робособака инспектирует промышленный коридор','loading="lazy"')}</div><div class="mini-body"><h4>Робособаки</h4><p>Четырёхногие платформы инспекции, охраны и обследования объектов.</p><div class="mini-price">от 299 000 ₽<span>ориентир: Unitree Go2 Air</span></div><a href="products.html#dog">Подробнее →</a></div></div>
</div>
<div style="margin-top:34px" class="rv"><a class="btn btn-ghost" href="products.html">Открыть весь каталог</a></div>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
<div class="section-head rv"><span class="eyebrow">Инженерный центр</span><h2>Роботизация и автоматизация производств</h2></div>
<div class="auto-grid">
<div class="auto-card rv"><span class="auto-num">01</span><h4>Аудит и проектирование</h4><p>Анализ операций, точки внедрения, КП с расчётом ROI — за 14 дней.</p></div>
<div class="auto-card rv"><span class="auto-num">02</span><h4>Поставка и интеграция</h4><p>Ячейки и линии под ключ: монтаж, пусконаладка, стыковка с ERP/MES.</p></div>
<div class="auto-card rv"><span class="auto-num">03</span><h4>Свои разработки</h4><p>Техзрение, захваты, конвейеры и ПО диспетчеризации флота роботов.</p></div>
<div class="auto-card rv"><span class="auto-num">04</span><h4>Сервис и модернизация</h4><p>Поддержка 24/7, ЗИП, подменная техника, ретрофит старых линий.</p></div>
</div>
<div style="margin-top:34px" class="rv"><a class="btn btn-primary" href="automation.html">Направление «Автоматизация»</a></div>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
<div class="cta-band rv"><h2>Не знаете, какой робот нужен?</h2>
<p>Опишите задачу — инженер подберёт класс техники, посчитает окупаемость и привезёт робота на тест-драйв.</p>
<div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" href="contacts.html">Связаться с нами</a><a class="btn btn-ghost" href="company.html">Узнать о компании</a></div></div>
</div></section>
"""

# ================= PRODUCTS =================
def cat_card(anchor, key, alt, title, desc, f1, f2, price, note, topic):
    return f"""<div class="cat-card rv" id="{anchor}">
<div class="ph">{img(key, alt, 'loading="lazy"')}</div>
<div class="cat-body"><h4>{title}</h4><p>{desc}</p>
<ul class="cat-feats"><li>{CHECK.replace('15','14')} {f1}</li><li>{CHECK.replace('15','14')} {f2}</li></ul>
<div class="cat-price">{price}<span>{note}</span></div>
<a class="btn btn-ghost btn-wide" href="{topic_url(topic)}">Запросить подробности</a>
</div></div>"""

products_body = f"""
<section class="pagehead"><div class="wrap">
<span class="eyebrow">Каталог</span>
<h1>Все продукты FutureKinetix</h1>
<p>Семь продуктовых линеек: от всесезонного робота Yarbo для дома до промышленных платформ. Цены «от» по открытым рыночным данным на октябрь 2026 — итоговая стоимость зависит от конфигурации, флота и задач интеграции.</p>
</div></section>

<section class="section" style="padding-top:20px"><div class="wrap">
<div class="band rv" id="yarbo" style="scroll-margin-top:100px">
{img('lineup','Линейка роботов Yarbo Y Series с модулями','loading="lazy"')}
<div>
<div class="tags"><span class="tag tag-yellow">Линейка №1 для дома</span><span class="tag tag-teal">Прайс РФ</span></div>
<h3>Yarbo Y40 — модульный всесезонный робот</h3>
<p style="color:var(--muted);margin:12px 0 6px;font-size:15px">Гусеничное шасси Core и сменные модули: газон, снег, листва, кромки. Официальный прайс Yarbo в РФ.</p>
<div class="price-line">от 590 000 ₽</div>
<div class="price-sub">Core 590 000 ₽ · газонокосилка PRO (M1PRO) 880 000 ₽ · снегоуборщик (S1) 880 000 ₽ · модули 41 800–290 000 ₽</div>
<ul class="feat-list">
<li>{CHECK} Кошение 50 см, до 25 000 м²; снег 61 см, выброс 12 м</li>
<li>{CHECK} RTK-GPS + камеры: без проводов и маячков</li>
<li>{CHECK} Гарантия 2 года с продлением до 5 лет</li>
</ul>
<div class="hero-actions"><a class="btn btn-primary" href="yarbo.html">Открыть вкладку Yarbo</a><a class="btn btn-ghost" href="{topic_url('Тест-драйв Yarbo на моём участке')}">Тест-драйв</a></div>
</div></div>

<div class="section-head rv" style="margin:70px 0 40px"><span class="eyebrow">Промышленная робототехника</span>
<h2>Шесть классов роботов для бизнеса</h2>
<p>Подробности, наличие и точные цены — по запросу: подключаем инженера под вашу задачу.</p></div>
<div class="cat-grid">
{cat_card('clean','clean','Промышленный робот-уборщик моет пол склада','Промышленные роботы-уборщики','Автономные поломоечные и подметальные машины для складов, ТЦ, паркингов, аэропортов и производственных цехов.','Ширина мойки до 85 см, до 3 500 м²/ч','Самозарядка, слив и залив воды без оператора','от 2 200 000 ₽','ориентир рынка: Pudu CC1 — 2,2 млн ₽','Каталог: промышленные роботы-уборщики')}
{cat_card('warehouse','warehouse','Складской AMR-робот везёт стеллаж','Складские роботы (AMR/AGV)','Платформы «товар к человеку», буксировщики стеллажей и сортировочные роверы для fulfillment и производственных складов.','Грузоподъёмность до 1 500 кг','Интеграция с WMS/1C без остановки склада','от 1 200 000 ₽','класс Geek+ / Quicktron, цена под проект','Каталог: складские роботы (AMR/AGV)')}
{cat_card('arm','arm','Роборука-манипулятор на линии','Роборуки-манипуляторы','Коллаборативные и промышленные манипуляторы для сварки, упаковки, палетирования, сборки и контроля качества.','Нагрузка 0,4–50 кг, точность ±0,03 мм','Захваты и техзрение подбираем под продукт','от 350 000 ₽','ориентир: Dobot MG400 — 350 000 ₽','Каталог: роборуки-манипуляторы')}
{cat_card('delivery','delivery','Курьерский робот-доставщик на тротуаре','Роботы-доставщики','Тротуарные курьеры последней мили для ЖК, кампусов и офисных парков, сервисные доставщики для отелей и ресторанов.','До 100 кг груза, изолированные отсеки','До 80 км автономно в городской среде','от 450 000 ₽','базовая модель курьера, гарантия 24 мес','Каталог: роботы-доставщики')}
{cat_card('drone','drone','Грузовой дрон-доставщик над крышами','Дроны-доставщики','Тяжёлые грузовые БПЛА для медицины, вахтовых посёлков, геологии и e-commerce; полёты по расписанию и по запросу.','Полезная нагрузка до 40 кг','Дальность до 50 км, работа в ветер','от 3 598 800 ₽','ориентир: DJI FlyCart 30 — 3 598 800 ₽','Каталог: дроны-доставщики')}
{cat_card('dog','dog','Робособака инспектирует объект','Робособаки','Четырёхногие платформы для инспекции энергообъектов, охраны периметра и обследования опасных зон вместо людей.','Лестницы, снег, грязь; защита IP66','Тепловизор и LiDAR-картография','от 299 000 ₽','ориентир: Unitree Go2 Air — 299 000 ₽','Каталог: робособаки')}
</div>
<div class="note-box rv"><span>Цены «от» указаны по открытым рыночным данным на октябрь 2026 и не являются публичной офертой. Итоговая стоимость зависит от конфигурации, количества машин, интеграции и обучения.</span><a class="btn btn-primary" href="contacts.html">Запросить точный расчёт</a></div>
</div></section>
"""

# ================= YARBO =================
yarbo_body = f"""
<section class="pagehead"><div class="wrap">
<span class="eyebrow">Продуктовая линейка</span>
<h1>Yarbo Y40: один робот — <span class="grad-text">каждый сезон</span></h1>
<p>Модульный гусеничный робот для дома и участка: косит газон, убирает снег, сдувает листву и подрезает кромки. Официальные поставки по прайсу РФ, гарантия и сервис FutureKinetix.</p>
</div></section>

<section class="section" style="padding-top:20px" id="product"><div class="wrap">
<div class="product-card rv">
<div class="gallery">
<div class="main"><img id="galMain" src="{IMG['studio']}" alt="Yarbo Y40 с модулем газонокосилки — студийное фото"></div>
<div class="thumbs">
<button class="active" data-img="{IMG['studio']}" data-alt="Yarbo Y40 с модулем газонокосилки — студийное фото"><img src="{IMG['studio']}" alt="Миниатюра: студийное фото"></button>
<button data-img="{IMG['hero']}" data-alt="Yarbo Y40 стрижёт газон у дома"><img src="{IMG['hero']}" alt="Миниатюра: газон"></button>
<button data-img="{IMG['snow']}" data-alt="Yarbo Y40 с снегоуборочным модулем чистит снег"><img src="{IMG['snow']}" alt="Миниатюра: снег"></button>
<button data-img="{IMG['bundle']}" data-alt="Комплект Yarbo: робот, модули и аксессуары"><img src="{IMG['bundle']}" alt="Миниатюра: комплект"></button>
</div></div>
<div>
<div class="tags" style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:14px"><span class="tag tag-yellow">Хит российского рынка</span><span class="tag tag-teal">Модульная система</span></div>
<h3 style="font-size:clamp(25px,3vw,34px)">Yarbo Y40 Core + модули</h3>
<div class="rating"><span class="stars">★★★★★</span> 4.8 · 64 отзыва на eu.yarbo.com · 83 % оценок «5 звёзд»</div>
<div class="price-row" style="display:flex;align-items:baseline;gap:16px"><span class="price" id="pPrice">590 000 ₽</span></div>
<div class="price-sub">Официальный прайс Yarbo в РФ (zimani.ru), октябрь 2026 · доставка и пусконаладка включены</div>
<div class="installment" id="pInst">Рассрочка 0-0-12 — от 49 000 ₽/мес</div>
<ul class="feat-list">
<li>{CHECK} Гусеничное шасси Yarbo Core: снег, грязь, уклон до 35° (70 %)</li>
<li>{CHECK} RTK-GPS (Data Center в комплекте) + камеры и ультразвук — без проводов</li>
<li>{CHECK} Модули: косилка 50 см, снегоуборщик 61 см (выброс 12 м), воздуходувка, триммер, отвал</li>
<li>{CHECK} Yarbo App: карта участка, сценарии по погоде и живое видео Live Yard View</li>
</ul>
<div class="cfg-switch" id="cfgSwitch">
<button class="active" data-price="590000">YARBO CORE</button>
<button data-price="880000">ПРО ЛИТЕРА (M1PRO)</button>
<button data-price="880000">СНЕГОУБОРЩИК (S1)</button>
<button data-price="1170000">КОМПЛЕКТ SNOW + LAWN</button>
</div>
<div class="hero-actions"><a class="btn btn-primary" href="#configs">Все комплектации и цены</a><a class="btn btn-ghost" href="{topic_url('Тест-драйв Yarbo на моём участке')}">Тест-драйв</a></div>
<div class="trust">
<div><svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M12 3 4 6v6c0 5 3.4 8.3 8 9 4.6-.7 8-4 8-9V6l-8-3Z" stroke="#6b7d8f" stroke-width="2" stroke-linejoin="round"/></svg>Гарантия 2–5 лет</div>
<div><svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M3 7h11v10H3zM14 10h4l3 3v4h-7z" stroke="#6b7d8f" stroke-width="2" stroke-linejoin="round"/><circle cx="7" cy="17.5" r="1.8" stroke="#6b7d8f" stroke-width="2"/><circle cx="17.5" cy="17.5" r="1.8" stroke="#6b7d8f" stroke-width="2"/></svg>Доставка 2–7 дней</div>
<div><svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M12 8v4l2.5 2.5" stroke="#6b7d8f" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="12" r="9" stroke="#6b7d8f" stroke-width="2"/></svg>Поддержка 24/7</div>
</div></div></div>

<div class="box-strip rv">
{img('box','Комплект поставки Yarbo Y40','loading="lazy"')}
<div class="box-list"><h3>Что в коробке</h3><ul>
<li>{CHECK} Шасси Yarbo Core ×1</li><li>{CHECK} Выбранный модуль ×1</li>
<li>{CHECK} RTK Data Center ×1</li><li>{CHECK} Зарядная док-станция</li>
<li>{CHECK} Батарея и комплект ножей</li><li>{CHECK} Крепёж и русская документация</li>
</ul></div></div>
</div></section>

<section class="section" style="padding-top:0" id="modules"><div class="wrap">
<div class="section-head rv"><span class="eyebrow">Система Yarbo</span><h2>Одно шасси — <span class="grad-text">четыре сезона работ</span></h2>
<p>Модули меняются без инструмента за пару минут. Докупайте их когда угодно — шасси менять не нужно.</p></div>
<div class="mod-banner rv">{img('modules','Роботы Yarbo выполняют сезонные работы','loading="lazy"')}</div>
<div class="mod-cards">
<div class="mod-card rv"><div class="ph">{img('snowmodule','Снегоуборочный модуль Yarbo Snow','loading="lazy"')}</div><div class="mod-body"><span class="code">Арт. Yarbo-Snow</span><h4>Модуль снегоуборщик</h4><p>Захват 61 см, выброс снега до 12 м с регулируемым желобом. До 650 м² за заряд.</p><div class="mod-price">290 000 ₽<span>хит продаж зимой</span></div></div></div>
<div class="mod-card rv"><div class="ph">{img('blade','Модуль газонокосилки Yarbo PRO','loading="lazy"')}</div><div class="mod-body"><span class="code">Арт. Yarbo-M1</span><h4>Модуль газонокосилка PRO</h4><p>Два плавающих диска по 5 ножей, ширина 50 см, высота среза 3–10,2 см.</p><div class="mod-price">290 000 ₽<span>хит продаж летом</span></div></div></div>
<div class="mod-card rv"><div class="ph">{img('leaves','Робот Yarbo с модулем воздуходувки','loading="lazy"')}</div><div class="mod-body"><span class="code">Арт. Yarbo-B1</span><h4>Модуль воздуходувка</h4><p>Сгоняет листву, песок и свежий снег с дорожек, террас и газона.</p><div class="mod-price">220 000 ₽<span>осенний сценарий в приложении</span></div></div></div>
<div class="mod-card rv"><div class="ph">{img('towing','Робот Yarbo с модулем триммера и тележкой','loading="lazy"')}</div><div class="mod-body"><span class="code">Арт. Yarbo-T</span><h4>Модуль триммер</h4><p>Подрезает кромки газона у дорожек, бордюров и клумб после основной косилки.</p><div class="mod-price">150 000 ₽<span>плюс модуль отвал — 41 800 ₽</span></div></div></div>
</div>
<div class="pricelist rv"><span class="pl-title">Прайс РФ · октябрь 2026</span>
<span>Yarbo Core — <b>590 000 ₽</b></span><span>М1PRO — <b>880 000 ₽</b></span><span>S1 — <b>880 000 ₽</b></span>
<span>Модули: M1 / Snow — <b>290 000 ₽</b>, B1 — <b>220 000 ₽</b>, T — <b>150 000 ₽</b>, отвал — <b>41 800 ₽</b></span></div>
</div></section>

<section class="section" style="padding-top:0" id="scenarios"><div class="wrap">
<div class="section-head rv"><span class="eyebrow">Круглый год</span><h2>Разные проблемы каждого сезона — один робот</h2></div>
<div class="sce-grid">
<div class="sce rv">{img('snow','Yarbo убирает снег зимой','loading="lazy"')}<span class="season">Зима</span><h4>Уборка снега</h4><p>Шнекороторный модуль 61 см чистит дорожки и подъезд раньше, чем вы проснётесь.</p></div>
<div class="sce rv">{img('lawn','Yarbo стрижёт газон летом','loading="lazy"')}<span class="season">Лето</span><h4>Идеальный газон</h4><p>До 25 000 м² при стрижке дважды в неделю. Мульчирование и ровная высота среза.</p></div>
<div class="sce rv">{img('leaves','Yarbo сдувает листву осенью','loading="lazy"')}<span class="season">Осень</span><h4>Листва и уборка</h4><p>Воздуходувка сгоняет листву с газона и мощения, отвал сдвигает сугробы и мусор.</p></div>
<div class="sce rv">{img('towing','Yarbo перевозит грузы весной','loading="lazy"')}<span class="season">Весна</span><h4>Подготовка участка</h4><p>Перевозит грунт, дрова и инвентарь, вычёсывает остатки листвы после зимы.</p></div>
</div></div></section>

<section class="section" style="padding-top:0" id="specs"><div class="wrap">
<div class="section-head rv"><span class="eyebrow">Официальные характеристики</span><h2>Yarbo Y40 в цифрах</h2></div>
<div class="specs-box rv">
<div class="spec-tabs" id="specTabs">
<button class="active" data-tab="base">Шасси и навигация</button><button data-tab="mow">Кошение</button><button data-tab="snow">Снег</button><button data-tab="kit">Комплект и гарантия</button>
</div>
<dl class="spec-table" data-panel="base">
<div class="spec-row"><dt>Ходовая часть</dt><dd>Гусеничная, полный привод; уклон до 35° (70 %)</dd></div>
<div class="spec-row"><dt>Навигация</dt><dd>RTK-GPS (Data Center, Ethernet) + бинокулярные камеры + ультразвуковой радар + IMU + ODOM</dd></div>
<div class="spec-row"><dt>Ограничительные провода</dt><dd>Не нужны — карта строится в приложении</dd></div>
<div class="spec-row"><dt>Обнаружение препятствий</dt><dd>Мультисенсорное, в реальном времени: объезд и адаптация к рельефу</dd></div>
<div class="spec-row"><dt>Видеонаблюдение</dt><dd>Live Yard View (Smart Vision) — живое видео в Yarbo App</dd></div>
<div class="spec-row"><dt>Режимы работы</dt><dd>До 7 автономных циклов в день по расписанию и погоде</dd></div>
</dl>
<dl class="spec-table" data-panel="mow" hidden>
<div class="spec-row"><dt>Ширина кошения</dt><dd>50 см (20″) — два плавающих диска по 5 ножей</dd></div>
<div class="spec-row"><dt>Высота среза</dt><dd>3–10,2 см (1.2–4.0″), регулировка из приложения</dd></div>
<div class="spec-row"><dt>Площадь</dt><dd>до 25 000 м² (6 акров) при стрижке дважды в неделю</dd></div>
<div class="spec-row"><dt>За один заряд</dt><dd>120 мин → ~1 000 м² (80→20 %); до 1 600 м² при полном разряде</dd></div>
<div class="spec-row"><dt>В сутки</dt><dd>до ~0,7 га автономно: авто-возврат на док и дозаряд 90 мин</dd></div>
</dl>
<dl class="spec-table" data-panel="snow" hidden>
<div class="spec-row"><dt>Модуль</dt><dd>Snow Blower Module (арт. Yarbo-Snow), шнекороторный</dd></div>
<div class="spec-row"><dt>Ширина захвата</dt><dd>61 см</dd></div>
<div class="spec-row"><dt>Дальность выброса</dt><dd>до 12 м, направление желоба регулируется</dd></div>
<div class="spec-row"><dt>За один заряд</dt><dd>до 650 м² дорожек (Y40 Pro — до 750 м²)</dd></div>
<div class="spec-row"><dt>Снег</dt><dd>Свежий и слежавшийся; патрулирование во время снегопада</dd></div>
</dl>
<dl class="spec-table" data-panel="kit" hidden>
<div class="spec-row"><dt>В коробке</dt><dd>Yarbo Core, модуль, RTK Data Center, док-станция, батарея, ножи, крепёж</dd></div>
<div class="spec-row"><dt>Зарядка</dt><dd>90 минут до 80 % на док-станции</dd></div>
<div class="spec-row"><dt>Гарантия</dt><dd>2 года официальная + продление до 5 лет (опция)</dd></div>
<div class="spec-row"><dt>Возврат</dt><dd>30 дней в оригинальной упаковке</dd></div>
<div class="spec-row"><dt>Обновления</dt><dd>Прошивки «по воздуху» через Yarbo App</dd></div>
</dl>
</div></div></section>

<section class="section" style="padding-top:0" id="configs"><div class="wrap">
<div class="section-head rv"><span class="eyebrow">Комплектации и цены</span><h2>Выберите свой Yarbo</h2>
<p>Цены официального прайса Yarbo в РФ (zimani.ru) на октябрь 2026 года. Доставка, пусконаладка и обучение включены.</p></div>
<div class="cfg-grid">
<div class="cfg-card rv"><span class="cfg-name">Арт. YARBO-CORE</span><h3>Yarbo Core</h3><p class="cfg-desc">Базовое шасси: соберите робота под свои сезоны.</p><div class="cfg-price">590 000 ₽</div><div class="cfg-save">Модули докупаются в любой момент</div>
<ul class="cfg-list"><li>{CHECK} Гусеничное шасси с RTK-навигацией</li><li>{CHECK} Батарея и зарядная док-станция</li><li>{CHECK} RTK Data Center и Yarbo App</li><li>{CHECK} Гарантия 2 года</li></ul>
<a class="btn btn-ghost" href="{topic_url('Yarbo Core — 590 000 ₽')}">Заказать Yarbo Core</a></div>
<div class="cfg-card hit rv"><span class="hit-badge">Хит лета</span><span class="cfg-name">Арт. Yarbo-M1PRO</span><h3>Робот-газонокосилка PRO</h3><p class="cfg-desc">Core + косилка PRO: газон до 25 000 м² без вас.</p><div class="cfg-price">880 000 ₽</div><div class="cfg-save">Картирование участка инженером включено</div>
<ul class="cfg-list"><li>{CHECK} Всё из комплектации Yarbo Core</li><li>{CHECK} Модуль газонокосилка PRO (Yarbo-M1)</li><li>{CHECK} Настройка сценариев кошения</li><li>{CHECK} Гарантия 2 года</li></ul>
<a class="btn btn-primary" href="{topic_url('Робот-газонокосилка Yarbo PRO (M1PRO) — 880 000 ₽')}">Заказать M1PRO</a></div>
<div class="cfg-card rv"><span class="cfg-name">Арт. Yarbo-S1</span><h3>Робот-снегоуборщик</h3><p class="cfg-desc">Core + снегоуборщик: чистые дорожки всю зиму.</p><div class="cfg-price">880 000 ₽</div><div class="cfg-save">Патрульный сценарий снегопада в настройке</div>
<ul class="cfg-list"><li>{CHECK} Всё из комплектации Yarbo Core</li><li>{CHECK} Модуль снегоуборщик (Yarbo-Snow)</li><li>{CHECK} Захват 61 см, выброс до 12 м</li><li>{CHECK} Гарантия 2 года</li></ul>
<a class="btn btn-ghost" href="{topic_url('Робот-снегоуборщик Yarbo (S1) — 880 000 ₽')}">Заказать S1</a></div>
<div class="cfg-card rv"><span class="cfg-name">Комплект</span><h3>SNOW + LAWN</h3><p class="cfg-desc">Core + косилка M1 + снегоуборщик: полный год.</p><div class="cfg-price">1 170 000 ₽</div><div class="cfg-save">= 590 000 + 290 000 + 290 000 по прайсу</div>
<ul class="cfg-list"><li>{CHECK} Шасси Yarbo Core и оба модуля</li><li>{CHECK} Сезонная перенастройка бесплатно</li><li>{CHECK} Расширенная гарантия 3 года в подарок</li><li>{CHECK} Приоритетный сервис 24/7</li></ul>
<a class="btn btn-ghost" href="{topic_url('Комплект SNOW + LAWN — 1 170 000 ₽')}">Заказать комплект</a></div>
</div></div></section>

<section class="section" style="padding-top:0" id="video"><div class="wrap">
<div class="section-head rv"><span class="eyebrow">Видео</span><h2>Yarbo в реальной работе</h2><p>Обзоры владельцев и официальный установочный гайд. Нажмите на карточку — видео откроется прямо на странице.</p></div>
<div class="video-grid">
<div class="video-card rv" data-vid="ZTkAdoeYW_s">{img('yt1','Превью видео: 60 дней с Yarbo','loading="lazy"')}<div class="play"><span><svg width="22" height="22" viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7L8 5Z"/></svg></span></div><div class="cap">60 дней с Yarbo на большом газоне — результат владельца</div></div>
<div class="video-card rv" data-vid="DfBuSyfQjsc">{img('yt2','Превью видео: стрижка с пульта','loading="lazy"')}<div class="play"><span><svg width="22" height="22" viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7L8 5Z"/></svg></span></div><div class="cap">Стрижка в стиле «сел и поехал»: управление с пульта</div></div>
<div class="video-card rv" data-vid="CAB5RfpkFMI">{img('yt3','Превью официального гайда Yarbo','loading="lazy"')}<div class="play"><span><svg width="22" height="22" viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7L8 5Z"/></svg></span></div><div class="cap">Официальный гайд Yarbo: установка шаг за шагом</div></div>
</div></div></section>

<section class="section" style="padding-top:0" id="faq"><div class="wrap">
<div class="section-head rv" style="text-align:center;margin-inline:auto"><span class="eyebrow" style="justify-content:center">Вопросы и ответы</span><h2 style="margin-top:14px">Частые вопросы о Yarbo</h2></div>
<div class="faq rv">
<details open><summary>Нужны ли ограничительные провода или маячки?</summary><div class="a">Нет. В комплекте идёт RTK Data Center: робот получает сантиметровую коррекцию GPS, а бинокулярные камеры, ультразвук и IMU дорабатывают карту под деревьями и вдоль стен. Границы зон рисуются в приложении.</div></details>
<details><summary>Переживёт ли русскую зиму?</summary><div class="a">Снегоуборочный модуль рассчитан на свежий и слежавшийся снег: захват 61 см, выброс до 12 м, до 650 м² за заряд. Гусеничный привод держит лёд и наст, а сценарий «Патруль» выводит робот во время снегопада.</div></details>
<details><summary>Какой уклон и сложный рельеф он тянет?</summary><div class="a">До 35° (70 % уклона). Канавы, корни, деревья и пруды объезжает благодаря мультисенсорной навигации: качество среза не падает на неровностях.</div></details>
<details><summary>Что с обслуживанием?</summary><div class="a">Ножи меняются без инструмента примерно раз в 3 месяца активной стрижки, гусеницы нужно чистить и проверять натяжение, камеры — протирать раз в месяц. Прошивки обновляются по воздуху. Сервис FutureKinetix — в 27 регионах, реакция в течение 24 часов.</div></details>
<details><summary>Цены окончательные?</summary><div class="a">Да, мы работаем по официальному прайсу Yarbo в РФ (zimani.ru): Core — 590 000 ₽, M1PRO и S1 — по 880 000 ₽, модули — от 41 800 ₽. Доставка, пусконаладка и обучение включены; для юрлиц возможны лизинг и флотные условия.</div></details>
<details><summary>Можно ли в рассрочку или лизинг?</summary><div class="a">Да: рассрочка 0-0-12 без переплат для частных клиентов и лизинг до 36 месяцев для юрлиц.</div></details>
</div></div></section>
"""

yarbo_js = """
const main=document.getElementById('galMain');
document.querySelectorAll('.thumbs button').forEach(b=>b.addEventListener('click',()=>{
  document.querySelectorAll('.thumbs button').forEach(x=>x.classList.remove('active'));
  b.classList.add('active');main.style.opacity=0;
  setTimeout(()=>{main.src=b.dataset.img;main.alt=b.dataset.alt;main.style.opacity=1;},180);
}));
const fmt=n=>n.toLocaleString('ru-RU')+' ₽';
document.querySelectorAll('#cfgSwitch button').forEach(b=>b.addEventListener('click',()=>{
  document.querySelectorAll('#cfgSwitch button').forEach(x=>x.classList.remove('active'));
  b.classList.add('active');const p=+b.dataset.price;
  document.getElementById('pPrice').textContent=fmt(p);
  document.getElementById('pInst').textContent='Рассрочка 0-0-12 — от '+fmt(Math.round(p/12/1000)*1000)+'/мес';
}));
document.querySelectorAll('#specTabs button').forEach(b=>b.addEventListener('click',()=>{
  document.querySelectorAll('#specTabs button').forEach(x=>x.classList.remove('active'));
  b.classList.add('active');
  document.querySelectorAll('.spec-table').forEach(p=>p.hidden=p.dataset.panel!==b.dataset.tab);
}));
document.querySelectorAll('.video-card').forEach(c=>c.addEventListener('click',()=>{
  const f=document.createElement('iframe');
  f.src='https://www.youtube.com/embed/'+c.dataset.vid+'?autoplay=1&rel=0';
  f.allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
  f.allowFullscreen=true;f.title='Видео Yarbo';
  c.innerHTML='';c.appendChild(f);c.style.cursor='default';
}));
"""

# ================= AUTOMATION =================
automation_body = f"""
<section class="pagehead"><div class="wrap">
<span class="eyebrow">Инженерный центр</span>
<h1>Роботизация и автоматизация производств</h1>
<p>Не просто продаём роботов — внедряем их в процессы: от аудита операции до серийной эксплуатации линии с диспетчеризацией флота.</p>
</div></section>

<section class="section" style="padding-top:20px"><div class="wrap">
<div class="auto-grid">
<div class="auto-card rv"><span class="auto-num">01</span><h4>Аудит и проектирование</h4><p>Выезжаем на площадку, анализируем операции и считаем точки внедрения. КП с расчётом ROI и сроков окупаемости — за 14 дней.</p></div>
<div class="auto-card rv"><span class="auto-num">02</span><h4>Поставка и интеграция</h4><p>Роботизированные ячейки и линии под ключ: монтаж, пусконаладка, стыковка с ERP/MES, охрана труда и декларирование.</p></div>
<div class="auto-card rv"><span class="auto-num">03</span><h4>Свои разработки</h4><p>Техническое зрение, захваты, конвейеры, защитные ограждения и ПО диспетчеризации флота роботов — собственное бюро.</p></div>
<div class="auto-card rv"><span class="auto-num">04</span><h4>Сервис и модернизация</h4><p>Поддержка 24/7, ЗИП на складе дилера, подменная техника, ретрофит старых линий и обучение персонала на нашей площадке.</p></div>
</div>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
<div class="section-head rv"><span class="eyebrow">Отрасли</span><h2>Где мы уже внедряли роботов</h2></div>
<div class="chips rv">
<span class="chip">Пищепром и напитки</span><span class="chip">Фармацевтика</span><span class="chip">E-commerce и фулфилмент</span><span class="chip">Автокомпоненты</span><span class="chip">Нефтегаз и энергетика</span><span class="chip">Металлообработка</span><span class="chip">Агро и теплицы</span><span class="chip">Логистика и 3PL</span><span class="chip">ЖКХ и клининг</span>
</div>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
<div class="section-head rv"><span class="eyebrow">Как идёт проект</span><h2>Пять шагов от идеи до серийной работы</h2></div>
<div class="steps5">
<div class="step rv"><span class="num">1</span><h4>Аудит</h4><p>1–2 недели на площадке: операции, циклы, узкие места.</p></div>
<div class="step rv"><span class="num">2</span><h4>КП и ROI</h4><p>Состав линии, бюджет, окупаемость, график.</p></div>
<div class="step rv"><span class="num">3</span><h4>Поставка</h4><p>Оборудование, интеграционные комплекты, ЗИП.</p></div>
<div class="step rv"><span class="num">4</span><h4>Внедрение</h4><p>Монтаж, пусконаладка, обучение смен и инженеров.</p></div>
<div class="step rv"><span class="num">5</span><h4>Эксплуатация</h4><p>Сервис 24/7, метрики OEE, модернизация по данным.</p></div>
</div>
<div class="img-duo rv" style="margin-top:40px">
<figure>{img('arm','Роборука-манипулятор на сборочной линии','loading="lazy"')}<figcaption>Роботизированная ячейка сборки: кобот + техзрение</figcaption></figure>
<figure>{img('warehouse','AMR-роботы на складе фулфилмента','loading="lazy"')}<figcaption>Флот AMR на складе e-commerce: «товар к человеку»</figcaption></figure>
</div>
<div style="margin-top:40px" class="rv"><div class="cta-band"><h2>Получить КП с расчётом ROI</h2><p>Опишите процесс или пришлите техзадание — вернёмся с расчётом окупаемости и планом внедрения за 14 дней.</p><div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" href="{topic_url('Автоматизация производства под ключ')}">Запросить КП</a><a class="btn btn-ghost" href="products.html">Смотреть каталог</a></div></div></div>
</div></section>
"""

# ================= COMPANY =================
company_body = f"""
<section class="pagehead"><div class="wrap">
<span class="eyebrow">О компании</span>
<h1>FutureKinetix — инженерная компания в робототехнике</h1>
<p>Мы занимаемся роботами, роботизацией и автоматизацией производств: поставляем автономную технику, проектируем линии и обслуживаем флоты роботов по всей России.</p>
</div></section>

<section class="section" style="padding-top:20px"><div class="wrap">
<div class="band rv">
{img('lineup','Линейка роботов Yarbo','loading="lazy"')}
<div>
<h3>Что мы делаем</h3>
<ul class="feat-list" style="margin-top:16px">
<li>{CHECK} Поставляем роботов для дома и бизнеса: Yarbo, промышленные уборщики, складские AMR, манипуляторы, курьеры, дроны, робособаки</li>
<li>{CHECK} Проектируем и внедряем роботизированные ячейки и линии собственным интеграционным бюро</li>
<li>{CHECK} Разрабатываем техзрение, захваты и ПО диспетчеризации флотов роботов</li>
<li>{CHECK} Обслуживаем технику: сервис 24/7 в 27 регионах, ЗИП, подменные машины, обучение</li>
</ul>
<p style="color:var(--muted);font-size:15px">Компания основана в 2018 году командой инженеров-робототехников. Сегодня в команде 120 специалистов: конструкторы, программисты, интеграторы и сервисные инженеры.</p>
</div></div>

<div class="comp-stats rv" style="margin-top:26px">
<div class="comp-stat"><b class="grad-text">1 400+</b><span>роботов и дронов поставлено</span></div>
<div class="comp-stat"><b class="grad-text">27</b><span>регионов с сервис-центрами</span></div>
<div class="comp-stat"><b class="grad-text">120</b><span>инженеров и интеграторов</span></div>
<div class="comp-stat"><b class="grad-text">14</b><span>отраслей: от ЖКХ до нефтегаза</span></div>
</div>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
<div class="section-head rv"><span class="eyebrow">Принципы</span><h2>Как мы работаем</h2></div>
<div class="auto-grid" style="grid-template-columns:repeat(3,1fr)">
<div class="auto-card rv"><span class="auto-num">01</span><h4>Прозрачные расчёты</h4><p>КП с окупаемостью и честными сроками: если робот не окупается — говорим об этом прямо и предлагаем альтернативу.</p></div>
<div class="auto-card rv"><span class="auto-num">02</span><h4>Официальные поставки</h4><p>Техника с регистрацией серийных номеров, официальной гарантией и обновлениями: Yarbo — по прайсу РФ, пром-линейки — от производителей.</p></div>
<div class="auto-card rv"><span class="auto-num">03</span><h4>Сервис на весь цикл</h4><p>Не исчезаем после продажи: обучение, ЗИП, подменная техника и модернизация по мере роста ваших задач.</p></div>
</div>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap">
<div class="section-head rv"><span class="eyebrow">Направления</span><h2>Куда идти дальше</h2></div>
<div class="dir-list rv">
<a href="yarbo.html">Yarbo Y40 — всесезонный робот для участка <span>→</span></a>
<a href="products.html#clean">Промышленные роботы-уборщики <span>→</span></a>
<a href="products.html#warehouse">Складские роботы AMR/AGV <span>→</span></a>
<a href="products.html#arm">Роборуки-манипуляторы <span>→</span></a>
<a href="products.html#delivery">Роботы-доставщики <span>→</span></a>
<a href="products.html#drone">Дроны-доставщики <span>→</span></a>
<a href="products.html#dog">Робособаки <span>→</span></a>
<a href="automation.html">Автоматизация производств под ключ <span>→</span></a>
</div>
<div class="img-duo rv" style="margin-top:40px">
<figure>{img('dog','Робособака на инспекции объекта','loading="lazy"')}<figcaption>Пилот робособаки на энергообъекте: 6 недель от договора до отчётов</figcaption></figure>
<figure>{img('modules','Роботы Yarbo четырех сезонов','loading="lazy"')}<figcaption>Yarbo — наша флагманская линейка для дома и участка</figcaption></figure>
</div>
<div style="margin-top:40px" class="rv"><div class="cta-band"><h2>Приезжайте в демо-зал</h2><p>Покажем роботов в работе: полигон Yarbo, ячейка с коботом и флот AMR под управлением диспетчерской.</p><div class="hero-actions" style="justify-content:center"><a class="btn btn-primary" href="contacts.html">Записаться на демо</a></div></div></div>
</div></section>
"""

# ================= CONTACTS =================
opts = ''.join(f'<option{" selected" if t=="Робот-газонокосилка Yarbo PRO (M1PRO) — 880 000 ₽" else ""}>{t}</option>' for t in TOPICS)
contacts_body = f"""
<section class="pagehead"><div class="wrap">
<span class="eyebrow">Контакты</span>
<h1>Обсудим вашу задачу</h1>
<p>Тест-драйв Yarbo на вашем участке, демо-зал промышленной робототехники в Москве или КП с расчётом ROI для производства — выберите тему, и мы подключим нужного инженера.</p>
</div></section>

<section class="section" style="padding-top:20px"><div class="wrap">
<div class="contact-grid">
<form class="form rv" id="orderForm" name="order" data-netlify="true">
<div><label for="fname">Ваше имя</label><input id="fname" name="name" type="text" placeholder="Иван Петров" required></div>
<div><label for="fphone">Телефон</label><input id="fphone" name="phone" type="tel" placeholder="+7 (___) ___-__-__" required></div>
<div><label for="fcfg">Интересует</label><select id="fcfg" name="config">{opts}</select></div>
<div><label for="fmsg">Комментарий</label><textarea id="fmsg" name="message" placeholder="Площадь участка, тип объекта, задача…"></textarea></div>
<button class="btn btn-primary" type="submit">Отправить заявку</button>
<div class="form-ok" id="formOk">Спасибо! Заявка принята — инженер FutureKinetix свяжется с вами в течение 30 минут в рабочее время.</div>
<p style="color:var(--dim);font-size:12.5px">Нажимая кнопку, вы соглашаетесь с политикой обработки персональных данных.</p>
</form>
<div class="contact-info rv">
<div class="ci-card"><div class="ci-ico"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M5 4h4l2 5-2.5 1.5a12 12 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z" stroke="#38bdf8" stroke-width="2" stroke-linejoin="round"/></svg></div><div><b>+7 (903) 997-10-47</b><span>Ежедневно с 9:00 до 22:00 (НСК)</span></div></div>
<div class="ci-card"><div class="ci-ico"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><rect x="3" y="5" width="18" height="14" rx="2.5" stroke="#38bdf8" stroke-width="2"/><path d="m4 7 8 6 8-6" stroke="#38bdf8" stroke-width="2" stroke-linejoin="round"/></svg></div><div><b>futurekinetix@ya.ru</b><span>Ответим в течение часа</span></div></div>
<div class="ci-card"><div class="ci-ico"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11Z" stroke="#38bdf8" stroke-width="2" stroke-linejoin="round"/><circle cx="12" cy="10" r="2.6" stroke="#38bdf8" stroke-width="2"/></svg></div><div><b>Демо-зал и полигон</b><span>Москва, Инновационный центр «Сколково», ул. Нобеля, 5 · ежедневно 10:00–20:00</span></div></div>
<div class="ci-card"><div class="ci-ico"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M13 2 4.5 13.5H11L10 22l8.5-11.5H12L13 2Z" stroke="#38bdf8" stroke-width="2" stroke-linejoin="round"/></svg></div><div><b>Интеграционное бюро</b><span>Аудит, проектирование и внедрение линий по всей России</span></div></div>
<div class="ci-card"><div class="ci-ico"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M12 3 4 6v6c0 5 3.4 8.3 8 9 4.6-.7 8-4 8-9V6l-8-3Z" stroke="#38bdf8" stroke-width="2" stroke-linejoin="round"/><path d="m9 12 2.2 2.2L15.5 10" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></div><div><b>Сервис 24/7</b><span>По всей России, реакция в течение 24 часов, подменная техника</span></div></div>
</div></div></div></section>
"""

contacts_js = """
const sel=document.getElementById('fcfg');
const t=new URLSearchParams(location.search).get('topic');
if(t){[...sel.options].forEach(o=>{if(o.text===t)sel.value=o.text;});}
const FORM_ENDPOINT='__FE__';
const WEB3_KEY='__WK__';
const MAIL_TO='__MAIL__';
const okBox=document.getElementById('formOk');
const showOk=msg=>{okBox.textContent=msg;okBox.style.display='block';};
document.getElementById('orderForm').addEventListener('submit',async e=>{
  e.preventDefault();
  const f=e.target;
  const payload={name:f.name.value,phone:f.phone.value,topic:f.config.value,message:f.message.value,source:location.href};
  const clear=()=>f.querySelectorAll('input,textarea').forEach(i=>i.value='');
  if(FORM_ENDPOINT){
    try{
      const body=Object.assign({},payload);
      if(FORM_ENDPOINT.includes('web3forms'))body.access_key=WEB3_KEY;
      const r=await fetch(FORM_ENDPOINT,{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(body)});
      if(r.ok){showOk('Спасибо! Заявка отправлена — она пришла на почту команды. Ответим в рабочее время.');clear();return;}
    }catch(err){}
    showOk('Сервис форм не ответил. Открываем почтовый клиент с готовым письмом на '+MAIL_TO+'…');
  }else if(location.hostname.includes('netlify')){
    try{
      const fd=new FormData(f);fd.append('form-name','order');
      const r=await fetch(location.pathname,{method:'POST',body:fd});
      if(r.ok||r.status===202){showOk('Спасибо! Заявка принята — уведомление пришло на почту команды (Netlify Forms).');clear();return;}
    }catch(err){}
  }
  const subj=encodeURIComponent('Заявка с сайта: '+payload.topic);
  const body=encodeURIComponent('Имя: '+payload.name+'\\nТелефон: '+payload.phone+'\\nТема: '+payload.topic+'\\nКомментарий: '+payload.message+'\\nСтраница: '+payload.source);
  showOk('Почтовый сервис не подключён: открыли ваш почтовый клиент с письмом на '+MAIL_TO+'. Если не открылось — напишите напрямую: '+MAIL_TO+' или позвоните +7 (903) 997-10-47.');
  location.href='mailto:'+MAIL_TO+'?subject='+subj+'&body='+body;
});
""".replace('__FE__', FORM_ENDPOINT).replace('__WK__', WEB3_KEY).replace('__MAIL__', MAIL_TO)

pages = [
 ('index.html', page('FutureKinetix — роботы, роботизация и автоматизация производств', 'FutureKinetix: поставка и внедрение роботов — Yarbo, промышленные уборщики, складские AMR, манипуляторы, курьеры, дроны, робособаки.', 'index.html', index_body)),
 ('products.html', page('Все продукты — FutureKinetix', 'Каталог роботов FutureKinetix: Yarbo Y40, промышленные уборщики, складские роботы, роборуки, доставщики, дроны, робособаки. Цены «от».', 'products.html', products_body)),
 ('yarbo.html', page('Yarbo Y40 — цены, комплектации, характеристики | FutureKinetix', 'Модульный всесезонный робот Yarbo Y40: цены официального прайса РФ, модули, характеристики, комплектации, видео и FAQ.', 'yarbo.html', yarbo_body, yarbo_js)),
 ('automation.html', page('Автоматизация и роботизация производств — FutureKinetix', 'Аудит, проектирование и внедрение роботизированных линий под ключ: манипуляторы, AMR, техзрение, сервис. КП с ROI за 14 дней.', 'automation.html', automation_body)),
 ('company.html', page('О компании FutureKinetix — роботы и роботизация', 'FutureKinetix: инженерная компания в робототехнике. Поставка роботов, интеграция линий, сервис 24/7 в 27 регионах.', 'company.html', company_body)),
 ('contacts.html', page('Контакты — FutureKinetix', 'Связаться с FutureKinetix: тест-драйв Yarbo, демо-зал, подбор промышленного робота, КП с расчётом ROI.', 'contacts.html', contacts_body, contacts_js)),
]
for name, html in pages:
    (ROOT/name).write_text(html, encoding='utf-8')
    print(name, len(html)//1024, 'KB')
