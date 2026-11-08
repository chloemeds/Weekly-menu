"""Audita un data/wkNN.json montado con tools/menu.py (usa el campo `src` de cada comida).

python3 tools/audit.py data/wk46.json
Recalcula macros por comida y por día, y revisa las reglas de CLAUDE.md que se pueden comprobar.
"""
import json
import re
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from menu import DB, VERDURAS, HIDRATOS, FRUTA, EXENTOS, TARGETS, macros, kcal  # noqa: E402

PROTE = {'pollo', 'muslo', 'pavo', 'lomo', 'solomillo', 'ternera', 'picada_ternera', 'salmon', 'merluza',
         'bacalao', 'lubina', 'dorada', 'rape', 'gambas', 'calamar'}
YOG = {'yog_light', 'koukakis', 'koukakis0', 'skyr'}
RANGOS = {'arroz': (60, 90), 'arroz_int': (60, 90), 'pasta': (60, 90), 'pasta_int': (60, 90),
          'lentejas': (60, 90), 'patata': (150, 250), 'boniato': (100, 250), 'chia': (10, 15)}


def items_of(src):
    out = []
    for s in src:
        if s[0] == 'custom':
            out.append(('custom', s[1], s[2], ''))
        else:
            out.append((s[0], s[1]))
    return out


def shown(html):
    return [int(x) for x in re.findall(r'<b>(\d+)</b>', html.split('class="mac"')[1])]


def main(path):
    w = json.load(open(path, encoding='utf-8'))
    errs = 0
    for day in w['days']:
        tipo = day['chip']['cls']
        tot = [0.0] * 4
        seen = {}
        kc = {}
        print('== %s %s (%s)' % (day['name'], day['date'], tipo))
        for m in day['meals']:
            if 'src' not in m:
                print('   %s: sin src, no se puede auditar' % m['meal'])
                continue
            its = items_of(m['src'])
            mm = macros(its)
            tot = [a + b for a, b in zip(tot, mm)]
            k = kcal(*mm)
            kc[m['meal']] = k
            want = [round(x) for x in mm] + [round(k)]
            got = shown(m['html'])
            flag = '' if want == got else '  <-- HTML dice %s' % got
            print('   %-9s %3d C %3d P %3d G %3d F %4d kcal%s' % (m['meal'], *want, flag))
            probs = []
            if flag:
                probs.append('macros del HTML no cuadran')
            keys = [s[0] for s in m['src'] if s[0] != 'custom']
            grams = {s[0]: s[1] for s in m['src'] if s[0] != 'custom'}
            custom = any(s[0] == 'custom' for s in m['src'])
            for kk in keys:
                if kk in EXENTOS:
                    continue
                if kk in seen:
                    probs.append('%s repetido (también en %s)' % (kk, seen[kk]))
                seen[kk] = m['meal']
            if not custom:
                carbs = [kk for kk in keys if kk in HIDRATOS]
                if len(carbs) > 1:
                    probs.append('dos fuentes de hidratos: %s' % carbs)
                if m['meal'] == 'Cena' and (carbs or [kk for kk in keys if kk in FRUTA]):
                    probs.append('hidratos o fruta en la cena')
                veg = {kk: grams[kk] for kk in keys if kk in VERDURAS}
                for kk, g in veg.items():
                    if not 100 <= g <= 200:
                        probs.append('%s %g g fuera de 100-200' % (kk, g))
                if sum(veg.values()) > 300:
                    probs.append('verdura total %g g > 300' % sum(veg.values()))
                ys = [kk for kk in keys if kk in YOG]
                if len(ys) > 1 or any(grams[kk] > 150 for kk in ys):
                    probs.append('yogur/skyr: máx 1 y 150 g')
                if m['meal'] == 'Desayuno' and (ys or [kk for kk in keys if kk in FRUTA]):
                    probs.append('yogur o fruta en el desayuno')
                for kk in keys:
                    if kk in PROTE and not 100 <= grams[kk] <= 170:
                        probs.append('%s %g g fuera de 100-170' % (kk, grams[kk]))
                    if kk in RANGOS and not RANGOS[kk][0] <= grams[kk] <= RANGOS[kk][1]:
                        probs.append('%s %g g fuera de %s' % (kk, grams[kk], RANGOS[kk]))
                if m['meal'] in ('Comida', 'Cena'):
                    if not m.get('recipe') or not 3 <= len(m['recipe']) <= 4:
                        probs.append('receta de 3-4 pasos')
            if m['meal'] in ('Comida', 'Cena') and 'choco' not in keys:
                probs.append('sin onza de chocolate')
            for p in probs:
                print('      ! ' + p)
                errs += 1
        if kc.get('Merienda') and not 150 <= kc['Merienda'] <= 250:
            print('      ! merienda %d kcal fuera de 150-250' % kc['Merienda']); errs += 1
        if kc.get('Comida') and kc.get('Merienda') and kc['Comida'] <= kc['Merienda']:
            print('      ! comida no es mayor que la merienda'); errs += 1
        if kc.get('Comida') and kc.get('Cena') and kc['Cena'] >= kc['Comida'] and \
                not any(s[0] == 'custom' for m in day['meals'] if m['meal'] == 'Cena' for s in m.get('src', [])):
            print('      ! cena no es más ligera que la comida'); errs += 1
        tc, tp, tg = TARGETS[tipo]
        c, p, g, f = tot
        print('   TOTAL     %3d C %3d P %3d G %3d F %4d kcal   (objetivo %d/%d/%d)' %
              (round(c), round(p), round(g), round(f), round(kcal(*tot)), tc, tp, tg))
        for name, v, t in (('HC', c, tc), ('P', p, tp), ('G', g, tg)):
            if not t - 9 <= v <= t - 1.5:
                print('      ! %s %.1f: debería quedar unos 5 g por debajo de %d' % (name, v, t)); errs += 1
        if not 25 <= round(f) <= 32:
            print('      ! fibra %.1f fuera de 25-32' % f); errs += 1
        want_tot = [round(x) for x in tot] + [round(kcal(*tot))]
        got_tot = [int(x) for x in re.findall(r'class="tv">(\d+)<', day['total'])]
        if want_tot != got_tot:
            print('      ! total del HTML %s no cuadra con %s' % (got_tot, want_tot)); errs += 1
    print('\n%d avisos' % errs)
    return errs


if __name__ == '__main__':
    sys.exit(1 if main(sys.argv[1]) else 0)
