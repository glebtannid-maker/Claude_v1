#!/usr/bin/env python3
"""Build a compact digest of all cards + skeptic results, and the skeptic summary section."""
import json, os, re
S = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = {'expertise': 2, 'demand': 2, 'freeness': 1, 'clone': 2, 'platform': 2, 'speed': 1, 'support': 2,
     'unit_econ': 1, 'channels': 1, 'payments_reg': 1, 'viability': 2}
LBL = {'expertise': 'экспертиза', 'demand': 'спрос', 'freeness': 'свободность', 'clone': 'клоны', 'platform': 'платформы',
       'speed': 'скорость', 'support': 'поддержка', 'unit_econ': 'юнит-экономика', 'channels': 'каналы',
       'payments_reg': 'платежи/регуляторика', 'viability': '3 года'}
cards = json.load(open(os.path.join(S, 'data', 'cards.json')))
sk = {s['id']: s for s in json.load(open(os.path.join(S, 'data', 'skeptic.json')))}
FULL = {'spec_packs', 'creative_rates', 'sea_atlas', 'finishing_report_media', 'branded_worlds', 'brand_motion_system',
        'oblique2', 'clearance', 'intake_kit', 'plugin_price_radar', 'prof_pay_calcs', 'vernisazh'}


def tot(sc):
    return sum(int(sc[k]) * w for k, w in W.items())


rows = []
for c in cards:
    b = tot(c['scores'])
    s = sk.get(c['id'])
    a = tot(s['new_scores']) if s else None
    rows.append((a if a is not None else b, b, a, c, s))
rows.sort(key=lambda r: (-r[0], -r[1]))

with open(os.path.join(S, 'data', 'final_digest.md'), 'w') as f:
    f.write('# Сводка всех 35 карточек (баллы из 85; «после» — после проверки скептиком)\n\n')
    for i, (rank, b, a, c, s) in enumerate(rows, 1):
        r = c['revenue']
        f.write(f"## {i}. {c['name']} [id={c['id']}, тип {c['type']}] — карточка {b}" + (f", после скептика {a}" if a is not None else ", скептиком не проверялась") + "\n")
        f.write(f"- Суть: {c['one_liner']}\n- Формат: {c['format']}\n")
        f.write(f"- Вердикт карточки: {c['verdict']}\n")
        if s:
            f.write(f"- Вердикт скептика: {s['verdict']}\n- Как снизить риск: {s['mitigations'][:700]}\n")
        f.write(f"- Выручка/мес (конс/база/опт): m12 {r['m12']['conservative']}/{r['m12']['base']}/{r['m12']['optimistic']}; m36 {r['m36']['conservative']}/{r['m36']['base']}/{r['m36']['optimistic']}\n")
        f.write(f"- Поддержка: {c['support']['hours_per_week']}; MVP {c['mvp']['weeks']} нед.; риск платформ: {c['platform_risk_level']}\n")
        f.write(f"- Проверка до разработки: {c['pre_build_test'][:600]}\n- Критерий закрытия: {c['kill_criteria'][:600]}\n")
        f.write(f"- Синергия: {c['portfolio_synergy'][:450]}\n\n")

# skeptic summary section
checked = [r for r in rows if r[4] is not None]
lines = []
lines.append('### Что изменил скептик\n')
drops = [r[1] - r[2] for r in checked]
avg = sum(drops) / len(drops) if drops else 0
lines.append(f'Скептиков прошли {len(checked)} идеи из 35. Двенадцать прошли полный проход: два скептика с разными задачами («рынок и дистрибуция», «клоны, платформы, API, закон») и судья. Среди них топ-10 по баллам карточек, калькуляторы с другом и школьный «Вернисаж». Ещё {len(checked) - 12} идей с баллом карточки 43–48 прошли облегчённый проход: один агент атаковал с обеих сторон и пересчитал баллы. Средняя потеря — {avg:.1f} балла, разброс от {min(drops)} до {max(drops)}. Ни одна идея не выросла.\n')
lines.append('Чаще всего скептики снижали четыре критерия: **жизнь через 3 года** (функцию встроят или обесценят к 2028), **доказанность спроса** (платящих за именно этот слой не нашлось), **защиту от платформ** и **платежи/регуляторику** (дети, Индонезия, ответственность за «вердикты»). Идеи с оценкой 42 и ниже скептиков не проходили, поэтому их баллы, по всей видимости, завышены на ту же величину.\n')
lines.append('| Идея | Проход | Было | Стало | Самый сильный аргумент скептика | В какой форме идея ещё имеет смысл |')
lines.append('|---|---|---|---|---|---|')
for rank, b, a, c, s in sorted(checked, key=lambda r: -r[2]):
    crit = max(s['arguments'], key=lambda x: ['низкая', 'средняя', 'высокая', 'критическая'].index(x['severity']))
    sents = [x.strip() for x in re.split(r'(?<=[.!?])\s+', s['verdict']) if x.strip()]
    pick = [x for x in sents if re.search(r'только|допуст|имеет смысл|остаётся|Остаётся|стоит делать|Делать стоит|Разумн|Оставить|форма|выживает', x)]
    tail = (pick[0] if pick else sents[-1])
    if len(tail) > 320:
        cut = tail[:320]
        tail = cut[:cut.rfind(' ')] + '…'
    name = c['name'].split(':')[0]
    lines.append(f"| [{name}](#idea-{c['id']}) | {'полный' if c['id'] in FULL else 'облегчённый'} | {b} | **{a}** | {crit['angle']} | {tail} |")
open(os.path.join(S, 'sections', 'skeptic_summary.md'), 'w').write('\n'.join(lines) + '\n')
print('digest rows', len(rows), 'checked', len(checked), 'avg drop', round(avg, 1))
for rank, b, a, c, s in rows[:15]:
    print(rank, b, a, c['id'])
