"""Genera el HTML del artefacto del menú desde data/wkNN.json usando la página de la semana anterior como plantilla.
python3 tools/build_artifact.py data/wk46.json plantilla.html salida.html "subtítulo"
"""
import json, re, sys
src, tpl, out, sub = sys.argv[1:5]
w = json.load(open(src, encoding='utf-8'))
s = open(tpl, encoding='utf-8').read()
s = re.sub(r'<title>.*?</title>', '<title>Menú %s</title>' % w['week'], s, count=1)
s = re.sub(r'<h1>.*?</h1>', '<h1>%s</h1>' % w['title'], s, count=1)
s = re.sub(r'<p class="sub">.*?</p>', '<p class="sub">%s</p>' % sub, s, count=1, flags=re.S)
head = '<thead><tr><th class="corner"></th>' + ''.join(
    '<th class="dayh"><div class="dn">%s <small>%s</small></div><span class="chip %s">%s</span></th>' %
    (d['name'], d['date'], d['chip']['cls'], d['chip']['text']) for d in w['days']) + '</tr></thead>'
names = ['Desayuno', 'Comida', 'Merienda', 'Cena']
body = '<tbody>'
for n in names:
    body += '<tr><th class="mealh">%s</th>' % n
    for d in w['days']:
        m = next((m for m in d['meals'] if m['meal'] == n), None)
        body += '<td>%s</td>' % (m['html'] if m else '')
    body += '</tr>'
body += '<tr class="tot"><th class="mealh">Total del día</th>' + ''.join('<td>%s</td>' % d['total'] for d in w['days']) + '</tr></tbody>'
s = re.sub(r'<thead>.*?</tbody>', lambda _: head + '\n      ' + body, s, count=1, flags=re.S)
open(out, 'w', encoding='utf-8').write(s)
