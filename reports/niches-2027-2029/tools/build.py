#!/usr/bin/env python3
"""Assemble the niche research report into one HTML page."""
import json, os, re, html, glob
import markdown

S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(S, 'data')
OUT = os.path.join(S, 'index.html')

CRIT = [
    ('expertise', 'Экспертиза', 2),
    ('demand', 'Спрос доказан', 2),
    ('freeness', 'Свободность ниши', 1),
    ('clone', 'Защита от ИИ-клонов', 2),
    ('platform', 'Защита от платформ', 2),
    ('speed', 'Скорость запуска', 1),
    ('support', 'Малая поддержка', 2),
    ('unit_econ', 'Юнит-экономика', 1),
    ('channels', 'Бесплатные каналы', 1),
    ('payments_reg', 'Платежи и регуляторика', 1),
    ('viability', 'Жизнь через 3 года', 2),
]
MAX = sum(5 * w for _, _, w in CRIT)
SHORT = {'expertise': 'Эксп', 'demand': 'Спрос', 'freeness': 'Своб', 'clone': 'Клон', 'platform': 'Плат',
         'speed': 'Скор', 'support': 'Подд', 'unit_econ': 'Юнит', 'channels': 'Кан', 'payments_reg': 'Плат/рег',
         'viability': '3 года'}
TYPE_LABEL = {'A': 'А', 'B': 'Б', 'AB': 'А+Б'}


def load(name, default):
    p = os.path.join(D, name)
    if os.path.exists(p):
        return json.load(open(p))
    return default


def md(text):
    if not text:
        return ''
    return markdown.markdown(text, extensions=['tables', 'sane_lists', 'fenced_code'])


def esc(t):
    return html.escape(str(t or ''))


def linkify(t):
    """Escape text and turn bare URLs / markdown links into anchors."""
    t = str(t or '')
    out = []
    pos = 0
    pat = re.compile(r'\[([^\]]+)\]\((https?://[^)\s]+)\)|(https?://[^\s<>()\]"«»]+[^\s<>()\]"«».,;:])')
    for m in pat.finditer(t):
        out.append(html.escape(t[pos:m.start()]))
        if m.group(1):
            out.append(f'<a href="{html.escape(m.group(2))}" target="_blank" rel="noopener">{html.escape(m.group(1))}</a>')
        else:
            url = m.group(3)
            dom = re.sub(r'^https?://(www\.)?', '', url).split('/')[0]
            out.append(f'<a href="{html.escape(url)}" target="_blank" rel="noopener">{html.escape(dom)}</a>')
        pos = m.end()
    out.append(html.escape(t[pos:]))
    return ''.join(out)


BULLET = re.compile(r'^\s*([-•*]|\d+[.)])\s+')


def para(t):
    t = str(t or '').strip()
    if not t:
        return ''
    parts = [p for p in re.split(r'\n\s*\n', t) if p.strip()]
    res = []
    for p in parts:
        lines = [l for l in p.split('\n') if l.strip()]
        if all(BULLET.match(l) for l in lines) and len(lines) > 1:
            res.append('<ul>' + ''.join('<li>' + linkify(BULLET.sub('', l)) + '</li>' for l in lines) + '</ul>')
        else:
            res.append('<p>' + '<br>'.join(linkify(l) for l in lines) + '</p>')
    return ''.join(res)


def dom(u):
    return re.sub(r'^https?://(www\.)?', '', str(u)).split('/')[0]


def total(scores):
    return sum(int(scores.get(k, 0)) * w for k, _, w in CRIT)


def money(v):
    try:
        v = float(v)
    except Exception:
        return esc(v)
    if v >= 1000:
        return f'${v/1000:.1f}k'.replace('.0k', 'k')
    return f'${v:.0f}'


# ---------------------------------------------------------------- data
cards = load('cards.json', [])
skeptic = {s['id']: s for s in load('skeptic.json', [])}
mmap = load('market_map.json', [])
for c in cards:
    c['total'] = total(c['scores'])
    sk = skeptic.get(c['id'])
    if sk and sk.get('new_scores'):
        c['total_after'] = total(sk['new_scores'])
    else:
        c['total_after'] = None
    c['rank_score'] = c['total_after'] if c['total_after'] is not None else c['total']
cards.sort(key=lambda c: (-c['rank_score'], -c['total']))
for i, c in enumerate(cards, 1):
    c['rank'] = i

sec = {}
for p in glob.glob(os.path.join(S, 'sections', '*.md')):
    sec[os.path.splitext(os.path.basename(p))[0]] = open(p).read()


# ---------------------------------------------------------------- pieces
def score_bars(scores, notes=None, after=None):
    rows = []
    for k, label, w in CRIT:
        v = int(scores.get(k, 0))
        a = int(after.get(k, v)) if after else None
        note = (notes or {}).get(k, '')
        chg = ''
        if a is not None and a != v:
            chg = f'<span class="chg {"up" if a > v else "down"}">{v}→{a}</span>'
        cells = ''.join(f'<i class="{"on" if j < (a if a is not None else v) else ""}"></i>' for j in range(5))
        rows.append(
            f'<div class="sb"><span class="sb-l">{label}{" <b>×2</b>" if w == 2 else ""}</span>'
            f'<span class="sb-v" aria-label="{a if a is not None else v} из 5">{cells}</span>'
            f'<span class="sb-n">{a if a is not None else v}{chg}</span>'
            + (f'<span class="sb-note">{linkify(note)}</span>' if note else '') + '</div>')
    return '<div class="scorebars">' + ''.join(rows) + '</div>'


def card_html(c):
    sk = skeptic.get(c['id'])
    ev = ''.join(
        f'<li><span class="kind k-{esc(e.get("kind","факт"))}">{esc(e.get("kind","факт"))}</span> {linkify(e.get("text"))}'
        + (f' <a class="src" href="{esc(e["url"])}" target="_blank" rel="noopener">{esc(dom(e["url"]))}</a>' if e.get('url', '').startswith('http') else '')
        + (f' <span class="dt">{esc(e.get("date"))}</span>' if e.get('date') else '') + '</li>'
        for e in c.get('demand_evidence', []))
    comp = ''.join(
        f'<tr><td>' + (f'<a href="{esc(x["url"])}" target="_blank" rel="noopener">{esc(x["name"])}</a>' if str(x.get('url', '')).startswith('http') else esc(x['name']))
        + f'</td><td class="num">{esc(x.get("price"))}</td><td>{linkify(x.get("quality"))}</td></tr>'
        for x in c.get('competitors', []))
    apis = ''.join(f'<li>{esc(a.get("name"))}: <span class="mono">{esc(a.get("unit_cost"))}</span></li>' for a in c['mvp'].get('apis', []))
    r = c['revenue']
    rev = (
        '<table class="rev"><thead><tr><th></th><th>Консервативно</th><th>База</th><th>Оптимистично</th></tr></thead><tbody>'
        f'<tr><th>Месяц 12, выручка в мес.</th><td>{money(r["m12"]["conservative"])}</td><td>{money(r["m12"]["base"])}</td><td>{money(r["m12"]["optimistic"])}</td></tr>'
        f'<tr><th>Месяц 36, выручка в мес.</th><td>{money(r["m36"]["conservative"])}</td><td>{money(r["m36"]["base"])}</td><td>{money(r["m36"]["optimistic"])}</td></tr>'
        '</tbody></table>' + para(r.get('assumptions')))
    srcs = ''.join(
        f'<li><a href="{esc(s["url"])}" target="_blank" rel="noopener">{esc(s.get("title") or s["url"])}</a>'
        + (f' <span class="dt">{esc(s.get("date"))}</span>' if s.get('date') else '') + '</li>'
        for s in c.get('sources', []) if str(s.get('url', '')).startswith('http'))
    after = sk.get('new_scores') if sk else None
    tot_after = f'<span class="tot-after" title="после скептика">→ {c["total_after"]}</span>' if c['total_after'] is not None else '<span class="unchk-card">без проверки скептиком</span>'
    sk_html = ''
    if sk:
        args_ = ''.join(f'<li><b>{esc(a.get("angle"))}.</b> {linkify(a.get("argument"))}'
                        + (f' <span class="sev sev-{esc(a.get("severity"))}">{esc(a.get("severity"))}</span>' if a.get('severity') else '') + '</li>'
                        for a in sk.get('arguments', []))
        sk_html = (
            '<section class="skeptic"><h4>Проверка скептиком</h4>'
            f'<p class="verdict"><b>Вердикт:</b> {linkify(sk.get("verdict"))}</p>'
            f'<ul>{args_}</ul>'
            + (f'<p><b>Что изменилось в оценке:</b> {linkify(sk.get("changes"))}</p>' if sk.get('changes') else '')
            + (f'<p><b>Как снизить риск:</b> {linkify(sk.get("mitigations"))}</p>' if sk.get('mitigations') else '')
            + '</section>')
    fc = c.get('forecast', {})
    sup = c.get('support', {})
    bp = c.get('buyer_pain', {})
    return f'''
<article class="card t-{esc(c['type'])}" id="idea-{esc(c['id'])}">
  <header class="card-h">
    <div class="card-rank mono">#{c['rank']:02d}</div>
    <div class="card-title">
      <h3>{esc(c['name'])}</h3>
      <div class="card-meta"><span class="chip type-{esc(c['type'])}">Тип {TYPE_LABEL.get(c['type'], c['type'])}</span><span class="fmt">{esc(c.get('format'))}</span></div>
    </div>
    <div class="card-score"><span class="tot mono">{c['total']}</span>{tot_after}<span class="max mono">/ {MAX}</span></div>
  </header>
  <p class="lede">{linkify(c.get('one_liner'))}</p>
  {('<p class="cverdict"><b>Итог карточки:</b> ' + linkify(c.get('verdict')) + '</p>') if c.get('verdict') else ''}
  {score_bars(c['scores'], c.get('score_notes'), after)}
  <div class="fields">
    <section><h4>Для кого и какая боль</h4>
      <p><b>Покупатель:</b> {linkify(bp.get('buyer'))}</p><p><b>Боль:</b> {linkify(bp.get('pain'))}</p>
      <p><b>Как часто:</b> {linkify(bp.get('frequency'))}</p><p><b>Сколько и кому платит сейчас:</b> {linkify(bp.get('current_spend'))}</p></section>
    <section><h4>Доказательства спроса</h4><ul class="ev">{ev}</ul></section>
    <section><h4>Конкуренты</h4><div class="tw"><table class="comp"><thead><tr><th>Кто</th><th>Цена</th><th>Качество и заметки</th></tr></thead><tbody>{comp}</tbody></table></div>
      {para(c.get('competitors_dynamics'))}</section>
    <section><h4>Почему сейчас и прогноз</h4>{para(c.get('why_now'))}
      <dl class="fc"><dt>1 год</dt><dd>{linkify(fc.get('y1'))}</dd><dt>2 года</dt><dd>{linkify(fc.get('y2'))}</dd><dt>3 года</dt><dd>{linkify(fc.get('y3'))}</dd></dl></section>
    <section><h4>Защита</h4><p><b>От ИИ-клонов:</b> {linkify(c.get('moat_clone'))}</p>
      <p><b>От платформ</b> <span class="risk r-{esc(c.get('platform_risk_level'))}">риск: {esc(c.get('platform_risk_level'))}</span>: {linkify(c.get('moat_platform'))}</p></section>
    <section><h4>MVP за {esc(c['mvp'].get('weeks'))} нед.</h4>{para(c['mvp'].get('scope'))}
      <p><b>Стек:</b> {linkify(c['mvp'].get('stack'))}</p>{'<p><b>API и цена за единицу:</b></p><ul>' + apis + '</ul>' if apis else ''}</section>
    <section><h4>Монетизация и юнит-экономика</h4><p><b>Модель:</b> {linkify(c['monetization'].get('model'))}</p>
      <p><b>Цена:</b> {linkify(c['monetization'].get('price'))}</p>{para(c['monetization'].get('unit_economics'))}</section>
    <section><h4>Каналы и первые 100 клиентов</h4>{para(c['channels'].get('channels'))}{para(c['channels'].get('first_100'))}</section>
    <section><h4>Поддержка</h4><p><b>{esc(sup.get('hours_per_week'))} ч в неделю.</b> {'Посильна без чтения кода.' if sup.get('non_coder_ok') else 'Без чтения кода будет тяжело.'}</p>{para(sup.get('automation'))}{para(sup.get('notes'))}</section>
    <section><h4>Платежи и юрисдикция</h4>{para(c.get('payments'))}</section>
    <section><h4>Регуляторика и риски</h4>{para(c.get('regulatory'))}</section>
    <section class="wide"><h4>Доход через 12 и 36 месяцев</h4>{rev}</section>
    <section><h4>Проверка спроса до разработки</h4>{para(c.get('pre_build_test'))}</section>
    <section><h4>Связь с портфелем</h4>{para(c.get('portfolio_synergy'))}</section>
    <section class="wide kill"><h4>Критерий закрытия (60–90 дней)</h4>{para(c.get('kill_criteria'))}</section>
    {sk_html}
    <details class="srcs"><summary>Источники карточки ({len(c.get('sources', []))})</summary><ol>{srcs}</ol></details>
  </div>
</article>'''


def table_html():
    head = ''.join(f'<th data-k="{k}" title="{label}{" (вес ×2)" if w == 2 else ""}" class="num">{SHORT[k]}{"²" if w == 2 else ""}</th>' for k, label, w in CRIT)
    rows = []
    for c in cards:
        s = c['scores']
        sk = skeptic.get(c['id'], {}).get('new_scores') or s
        cells = ''.join(
            f'<td class="num s{int(sk.get(k, s.get(k, 0)))}" data-v="{int(sk.get(k, s.get(k, 0)))}">{int(sk.get(k, s.get(k, 0)))}</td>'
            for k, _, _ in CRIT)
        after = c['total_after'] if c['total_after'] is not None else ''
        rows.append(
            f'<tr data-type="{esc(c["type"])}"><td class="num mono" data-v="{c["rank"]}">{c["rank"]}</td>'
            f'<td class="nm" data-v="{esc(c["name"])}"><a href="#idea-{esc(c["id"])}">{esc(c["name"])}</a><span class="fmt">{esc(c.get("format"))}</span></td>'
            f'<td data-v="{esc(c["type"])}"><span class="chip type-{esc(c["type"])}">{TYPE_LABEL.get(c["type"], c["type"])}</span></td>'
            f'{cells}<td class="num tot" data-v="{c["total"]}">{c["total"]}</td>'
            f'<td class="num tot2" data-v="{after if after != "" else c["total"]}">' + (str(after) if after != '' else '<span class="unchk" title="скептиком не проверялась">—</span>') + '</td></tr>')
    return f'''
<div class="filters" role="group" aria-label="Фильтр по типу">
  <button class="flt on" data-f="all" type="button">Все ({len(cards)})</button>
  <button class="flt" data-f="A" type="button">Тип А</button>
  <button class="flt" data-f="B" type="button">Тип Б</button>
  <button class="flt" data-f="AB" type="button">А+Б</button>
</div>
<div class="tw"><table id="rank" class="rank">
<thead><tr><th data-k="rank" class="num">#</th><th data-k="name">Идея</th><th data-k="type">Тип</th>{head}<th data-k="total" class="num">Итог</th><th data-k="after" class="num">После скептика</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table></div>
<p class="note">Баллы 0–5, веса как в задании (²: вес ×2), максимум {MAX}. Для идей, прошедших скептика, в столбцах критериев показаны баллы после проверки, и порядок строк идёт по ним. Прочерк в последнем столбце означает, что идея скептика не проходила. Таких 12, у всех балл карточки 35–42. У проверенных идей скептик снимал в среднем 7 баллов, так что баллы непроверенных, вероятно, завышены на столько же. Сортировка: клик по заголовку столбца.</p>'''


def mmap_html():
    out = []
    for d in mmap:
        facts = ''.join(
            f'<li><span class="kind k-{esc(f.get("kind"))}">{esc(f.get("kind"))}</span> {linkify(f.get("text"))}'
            + (f' <a class="src" href="{esc(f["source_url"])}" target="_blank" rel="noopener">{esc(dom(f["source_url"]))}</a>' if str(f.get('source_url', '')).startswith('http') else '')
            + (f' <span class="dt">{esc(f.get("date"))}</span>' if f.get('date') else '') + '</li>'
            for f in d['key_facts'])
        scen = ''
        for s in d['scenarios']:
            sig = ''.join(f'<li>{linkify(x["signal"])} <span class="how">Где смотреть: {linkify(x["how_to_monitor"])}. Порог: {linkify(x["threshold"])}</span></li>' for x in s['signals'])
            scen += (f'<div class="scen sc-{esc(s["name"])}"><div class="scen-h"><b>{esc(s["name"])}</b> <span class="lbl">{esc(s.get("label"))}</span>'
                     f'<span class="prob mono">{int(s["probability"])}%</span></div>'
                     f'<div class="pbar"><i style="width:{int(s["probability"])}%"></i></div>'
                     f'<dl><dt>12 мес</dt><dd>{linkify(s["m12"])}</dd><dt>24 мес</dt><dd>{linkify(s["m24"])}</dd><dt>36 мес</dt><dd>{linkify(s["m36"])}</dd></dl>'
                     f'<p class="sig-h">Сигналы</p><ul class="sig">{sig}</ul></div>')
        a = d['answers']
        ans = ''.join(f'<div><dt>{q}</dt><dd>{linkify(a.get(k))}</dd></div>' for k, q in [
            ('mass_cheap', 'Станет массовым и дешёвым'), ('platforms_absorb', 'Поглотят платформы'),
            ('money_remains', 'Где останутся деньги'), ('access', 'У кого доступ'),
            ('skills_devalued', 'Навыки обесценятся'), ('skills_scarce', 'Навыки в дефиците')])
        imp = ''.join(f'<li>{linkify(x)}</li>' for x in d['implications'])
        out.append(f'''
<section class="domain" id="map-{esc(d['domain_key'])}">
  <h3>{esc(d['title'])}</h3>
  {para(d['summary'])}
  <div class="scens">{scen}</div>
  <dl class="answers">{ans}</dl>
  <div class="imp"><h4>Что это значит для вас</h4><ul>{imp}</ul></div>
  <details><summary>Ключевые факты ({len(d['key_facts'])})</summary><ul class="ev">{facts}</ul>
  <p class="note">Перепроверка: {linkify(d.get('verification_notes'))}</p></details>
</section>''')
    return ''.join(out)


def appendix_html():
    order = ['gen_ai', 'motion_industry', 'adobe_platforms', 'agents_mcp', 'dooh_3d', 'consumer_apps', 'seo_utilities',
             'ai_dev_economics', 'payments_legal', 'kids_market', 'kids_ops', 'demand_scout']
    names = {'gen_ai': 'Генерация изображений и видео', 'motion_industry': 'Моушн-индустрия', 'adobe_platforms': 'Adobe, соседи, маркетплейсы',
             'agents_mcp': 'Агенты и MCP', 'dooh_3d': 'DOOH и 3D', 'consumer_apps': 'Потребительские фото/видео-приложения',
             'seo_utilities': 'SEO и утилитарные сайты', 'ai_dev_economics': 'Экономика ИИ-разработки', 'payments_legal': 'Платежи и регуляторика',
             'kids_market': 'Детские рисунки: рынок', 'kids_ops': 'Детские рисунки: экономика и правила', 'demand_scout': 'Боли в сообществах'}
    out = []
    for k in order:
        for suffix, lab in [('', ''), ('_plus', ' — дополнение')]:
            p = os.path.join(S, 'research', f'{k}{suffix}.md')
            if not os.path.exists(p):
                continue
            body = open(p).read()
            body = re.sub(r'^# .*\n', '', body, count=1)
            out.append(f'<details class="appx"><summary>{esc(names[k])}{lab}</summary><div class="prose">{md(body)}</div></details>')
    return ''.join(out)



def sources_html():
    seen = {}
    def add(url, title='', date=''):
        url = str(url or '').strip()
        if not url.startswith('http'):
            return
        key = url.rstrip('/')
        if key not in seen:
            seen[key] = (title or '', date or '')
    for c in cards:
        for x in c.get('sources', []):
            add(x.get('url'), x.get('title'), x.get('date'))
        for x in c.get('demand_evidence', []):
            add(x.get('url'), '', x.get('date'))
        for x in c.get('competitors', []):
            add(x.get('url'), x.get('name'), '')
    for d in mmap:
        for f in d['key_facts']:
            add(f.get('source_url'), '', f.get('date'))
    groups = {}
    for url, (t, dt) in seen.items():
        groups.setdefault(dom(url), []).append((url, t, dt))
    hosts = sorted(groups, key=lambda h: (-len(groups[h]), h))
    items = []
    for h in hosts:
        links = ''.join(f'<li><a href="{esc(u)}" target="_blank" rel="noopener">{esc(t or u)}</a>' + (f' <span class="dt">{esc(dt)}</span>' if dt else '') + '</li>' for u, t, dt in sorted(groups[h]))
        items.append(f'<details class="srcgroup"><summary>{esc(h)} <span class="dt">{len(groups[h])}</span></summary><ul>{links}</ul></details>')
    return len(seen), len(hosts), ''.join(items)


CSS = open(os.path.join(S, 'tools', 'report.css')).read()
JS = open(os.path.join(S, 'tools', 'report.js')).read()

TOC = [('s1', '00:01', 'Главное'), ('s2', '00:02', 'Карта рынка'), ('s3', '00:03', 'Таблица идей'),
       ('s4', '00:04', 'Карточки идей'), ('s5', '00:05', 'Детские рисунки → видео'), ('s6', '00:06', 'Портфель и 90 дней'),
       ('s7', '00:07', 'Чего избегать'), ('s8', '00:08', 'Источники и метод')]
toc = ''.join(f'<li><a href="#{i}"><span class="tc mono">{t}</span>{n}</a></li>' for i, t, n in TOC)
top10 = [c for c in cards if c['total_after'] is not None]
SRC_N, SRC_H, SRC_HTML = sources_html()

page = f'''<title>Карта ниш 2027–2029</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&family=Unbounded:wght@500;700&display=swap">
<style>{CSS}</style>
<div class="wrap">
<header class="hero">
  <p class="eyebrow mono">TANSKIY DIGITAL · исследование · 26.09.2026</p>
  <h1>Карта ниш 2027–2029</h1>
  <p class="sub">{len(cards)} продуктовых ниш для портфеля небольших продуктов: моушн, After Effects, Figma, ИИ-видео, DOOH и «калькуляторные» сайты. Сценарии рынка до конца 2029 года, карточки с юнит-экономикой, проверка скептиком топ-10 и отдельный разбор идеи с детскими рисунками.</p>
  <div class="hero-stats">
    <div><b class="mono">{len(cards)}</b><span>идей с оценкой</span></div>
    <div><b class="mono">{len(top10)}</b><span>прошли скептика</span></div>
    <div><b class="mono">{len(mmap)}</b><span>доменов рынка</span></div>
    <div><b class="mono">{MAX}</b><span>максимум баллов</span></div>
  </div>
</header>
<div class="layout">
<nav class="toc" aria-label="Содержание"><ol>{toc}</ol></nav>
<main>
<section id="s1" class="block"><h2><span class="tc mono">00:01</span>Главное</h2><div class="prose">{md(sec.get('summary', ''))}</div></section>
<section id="s2" class="block"><h2><span class="tc mono">00:02</span>Карта рынка и сценарии</h2><div class="prose">{md(sec.get('map_intro', ''))}</div>{mmap_html()}
  <section class="domain" id="map-calculators"><h3>Модель «калькуляторных» сайтов</h3><div class="prose">{md(sec.get('calculators', ''))}</div></section></section>
<section id="s3" class="block wide"><h2><span class="tc mono">00:03</span>Таблица всех идей</h2>{table_html()}<div class="prose">{md(sec.get('skeptic_summary', ''))}</div></section>
<section id="s4" class="block"><h2><span class="tc mono">00:04</span>Карточки идей</h2><div class="prose">{md(sec.get('cards_intro', ''))}</div>{''.join(card_html(c) for c in cards)}</section>
<section id="s5" class="block"><h2><span class="tc mono">00:05</span>Детские рисунки → видео: глубокий разбор</h2><div class="prose">{md(sec.get('kids', ''))}</div></section>
<section id="s6" class="block"><h2><span class="tc mono">00:06</span>Портфельная стратегия и план на 90 дней</h2><div class="prose">{md(sec.get('portfolio', ''))}</div></section>
<section id="s7" class="block"><h2><span class="tc mono">00:07</span>Чего избегать</h2><div class="prose">{md(sec.get('avoid', ''))}</div></section>
<section id="s8" class="block"><h2><span class="tc mono">00:08</span>Источники и метод</h2><div class="prose">{md(sec.get('method', ''))}</div>
  <h3>Все источники карточек и карты рынка</h3><p class="note">{SRC_N} уникальных ссылок с {SRC_H} сайтов, сгруппированы по сайту. Источники каждого факта указаны рядом с ним в карточках и блоках карты рынка.</p><div class="srcwrap">{SRC_HTML}</div>
  <h3>Полные исследовательские заметки по потокам</h3><p class="note">Первичные отчёты потоков со всеми фактами и списками источников. Карточки идей ссылаются на них.</p>{appendix_html()}</section>
</main></div>
<footer class="foot"><p>Подготовлено для TANSKIY DIGITAL LTD. Факты с источниками и датами, оценки помечены. Это не юридическая и не налоговая консультация.</p></footer>
</div>
<script>{JS}</script>'''

PIRACY = ('filecr.com', 'intro-hd.net', 'riztagar.com', 'gfx-hub.co', 'psdly.co.uk', 'getintopc')
def _strip_piracy(html_text):
    pat = re.compile(r'<a href="(https?://[^"]*)"[^>]*>(.*?)</a>', re.S)
    def rep(m):
        return m.group(2) if any(d in m.group(1) for d in PIRACY) else m.group(0)
    html_text = pat.sub(rep, html_text)
    for d in PIRACY:
        html_text = re.sub(r'https?://(www\.)?' + re.escape(d) + r'[^\s<"]*', d, html_text)
    return html_text
page = _strip_piracy(page)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w').write(page)
print('written', OUT, len(page) // 1024, 'KB', 'cards', len(cards), 'domains', len(mmap))
