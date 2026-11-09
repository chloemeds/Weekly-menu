"""Base de macros y utilidades para montar un wkNN.json del menú.

Valores por 100 g: (HC netos, P, G, Fib). Hidratos SIEMPRE netos (sin fibra).
Arroz, pasta y legumbre en CRUDO. Uso: ver plans/wk46.py.
"""
import json

# clave: (nombre que se ve, HC netos, P, G, Fib, gramos por unidad o None)
DB = {
    # Hidratos
    'arroz':      ('Arroz (crudo)', 77, 7, 0.6, 1.3, None),
    'arroz_int':  ('Arroz integral (crudo)', 72, 7.5, 2.7, 3.5, None),
    'pasta':      ('Pasta (cruda)', 71, 12.5, 1.5, 3, None),
    'pasta_int':  ('Pasta integral (cruda)', 62, 13, 2.5, 8, None),
    'patata':     ('Patata', 15.5, 2, 0.1, 2, None),
    'boniato':    ('Boniato', 17.5, 1.6, 0.1, 3, None),
    'lentejas':   ('Lentejas (secas)', 49, 24, 1.5, 11, None),
    'gnocchi':    ('Ñoquis de patata Hacendado', 37.6, 4.5, 0.4, 1, 150 / 23),  # etiqueta; 23 ñoquis = 150 g
    'pan_int':    ('Pan integral', 38, 11, 3.5, 7, None),
    'baguette':   ('Pan baguette', 52, 9, 1.5, 2.5, None),
    'tortita':    ('Tortitas de arroz', 78, 8, 3, 3, 8),
    'tortilla_trigo': ('Tortilla de trigo integral', 42, 9, 6, 7, 40),
    'granola':    ('Granola sin azúcar', 52, 10, 16, 9, None),
    'avena':      ('Copos de avena', 58, 13.5, 7, 10, None),
    # Proteína
    'pollo':      ('Pechuga de pollo', 0, 23, 1.5, 0, None),
    'muslo':      ('Contramuslo de pollo sin piel', 0, 19, 6, 0, None),
    'pavo':       ('Filete de pavo', 0, 22, 1, 0, None),
    'lomo':       ('Lomo de cerdo', 0, 21.5, 6, 0, None),
    'solomillo':  ('Solomillo de cerdo', 0, 21, 3.5, 0, None),
    'ternera':    ('Ternera (filete magro)', 0, 21, 5, 0, None),
    'picada_ternera': ('Carne picada de ternera 5% grasa', 0, 21, 5, 0, None),
    'salmon':     ('Salmón', 0, 20, 13, 0, None),
    'rodaballo':  ('Rodaballo', 0, 16, 2, 0, None),
    'salmon_lata': ('Salmón en lata (escurrido)', 0, 21.7, 6.7, 0, None),
    'merluza':    ('Merluza', 0, 17, 1.5, 0, None),
    'bacalao':    ('Bacalao fresco (lomo)', 0, 18, 0.7, 0, None),
    'lubina':     ('Lubina', 0, 19, 5, 0, None),
    'dorada':     ('Dorada', 0, 19, 5, 0, None),
    'rape':       ('Rape', 0, 16, 1, 0, None),
    'gambas':     ('Gambas o langostinos pelados', 0, 20, 1.2, 0, None),
    'calamar':    ('Calamar', 1, 16, 1.4, 0, None),
    'huevo':      ('Huevos', 0.7, 12.5, 10, 0, 55),
    'claras':     ('Claras de huevo', 0.7, 11, 0.2, 0, None),
    'york':       ('Jamón york extra', 1.5, 18, 2.5, 0, None),
    'pavo_l':     ('Pechuga de pavo en lonchas', 1.5, 19, 1.5, 0, None),
    'serrano':    ('Jamón serrano', 0, 30, 12, 0, None),
    'salmon_ahum': ('Salmón ahumado', 0, 22, 8, 0, None),
    'queso_l':    ('Queso en lonchas light', 1.6, 27, 17, 0, 25),
    'mozza_l':    ('Mozzarella light', 1, 20, 9, 0, None),
    # Lácteos (sus productos)
    'yog_light':  ('Yogur griego light Mercadona', 4.7, 5.8, 2, 0, 125),
    'koukakis':   ('Yogur griego Koukakis', 3.8, 6.2, 10, 0, 150),
    'koukakis0':  ('Yogur griego Koukakis 0%', 4, 7.9, 0, 0, 150),
    'skyr':       ('Skyr Danone natural', 3.4, 9, 0.1, 0, 100),
    'yog_prot':   ('Yogur +Proteínas Hacendado', 4.3, 10, 0.2, 0, None),
    'leche_d':    ('Leche desnatada', 4.8, 3.4, 0.2, 0, None),
    'leche_a':    ('Bebida de almendra sin azúcar', 0, 0.5, 1.1, 0.3, None),
    'leche_s':    ('Leche semidesnatada', 4.7, 3.2, 1.6, 0, None),
    # Grasas
    'aceite':     ('Aceite de oliva', 0, 0, 100, 0, None),
    'nueces':     ('Nueces', 7, 15, 65, 6.7, None),
    'almendras':  ('Almendras', 9, 21, 50, 12.5, None),
    'anacardos':  ('Anacardos', 27, 18, 44, 3.3, None),
    'chia':       ('Chía', 7.7, 17, 31, 34, None),
    'sesamo':     ('Sésamo', 12, 18, 50, 12, None),
    'crema_cac':  ('Crema de cacahuete 100%', 14, 25, 50, 6, None),
    'crema_ave':  ('Crema de avellana y cacao Ametller', 6, 9, 30, 45, None),
    'pesto':      ('Pesto', 4, 5, 45, 1.5, None),
    'aguacate':   ('Aguacate', 1.8, 2, 15, 6.7, None),
    'choco':      ('Chocolate negro 72% (1 onza)', 32.5, 10, 42.5, 11.25, 8),
    'coco':       ('Coco rallado', 7, 7, 62, 16, None),
    # Fruta (netos)
    'fresas':     ('Fresas', 5.7, 0.7, 0.3, 2, None),
    'arandanos':  ('Arándanos', 12, 0.7, 0.3, 2.4, None),
    'granada':    ('Granada', 14.7, 1.7, 1.2, 4, None),
    'frambuesas': ('Frambuesas', 5.4, 1.2, 0.7, 6.5, None),
    'kiwi':       ('Kiwi', 11.7, 1.1, 0.5, 3, 75),
    'platano':    ('Plátano', 20.2, 1.1, 0.3, 2.6, None),
    'manzana':    ('Manzana', 11.4, 0.3, 0.2, 2.4, None),
    'pera':       ('Pera', 12.1, 0.4, 0.1, 3.1, None),
    'mandarina':  ('Mandarina', 11.5, 0.8, 0.3, 1.8, 70),
    'mango':      ('Mango', 13.4, 0.8, 0.4, 1.6, None),
    # Verduras (solo las suyas)
    'judias':     ('Judías verdes', 4.3, 1.8, 0.2, 2.7, None),
    'calabacin':  ('Calabacín', 2.1, 1.2, 0.3, 1, None),
    'brocoli':    ('Brócoli', 4.4, 2.8, 0.4, 2.6, None),
    'champis':    ('Champiñones', 2.3, 3.1, 0.3, 1, None),
    'setas':      ('Setas', 3.8, 3.3, 0.4, 2.3, None),
    'alcachofa':  ('Alcachofas (corazones)', 5.1, 3.3, 0.2, 5.4, None),
    'edamame':    ('Edamame (con vaina)', 1.9, 6.5, 2.9, 2.9, None),
}

VERDURAS = {'judias', 'calabacin', 'brocoli', 'champis', 'setas', 'alcachofa', 'edamame'}
HIDRATOS = {'arroz', 'arroz_int', 'pasta', 'pasta_int', 'patata', 'boniato', 'lentejas', 'gnocchi',
            'pan_int', 'baguette', 'tortita', 'tortilla_trigo', 'granola', 'avena'}
FRUTA = {'fresas', 'arandanos', 'frambuesas', 'kiwi', 'platano', 'manzana', 'pera', 'mandarina', 'mango', 'granada'}
EXENTOS = {'aceite', 'choco', 'leche_d', 'leche_a', 'leche_s'}  # pueden repetirse en el día

TARGETS = {'reg': (138, 103, 46), 'low': (50, 103, 85), 'fiesta': (173, 129, 58)}
CHIPS = {'reg': 'Macros regulares', 'low': 'Carbs reducidos', 'fiesta': 'Día de fiesta'}


def kcal(c, p, g, f):
    return 4 * (c + p) + 9 * g + 2 * f


def macros(items):
    """items: lista de (clave, gramos[, texto cantidad]) o ('custom', (c,p,g,f), nombre, texto)."""
    t = [0.0, 0.0, 0.0, 0.0]
    for it in items:
        if it[0] == 'custom':
            m = it[1]
        else:
            d = DB[it[0]]
            m = [v * it[1] / 100 for v in d[1:5]]
        for i in range(4):
            t[i] += m[i]
    return t


def fmt_g(x):
    s = ('%g' % x).replace('.', ',')
    return s


def qty_text(key, g):
    d = DB[key]
    unit = d[5]
    if key in ('leche_d', 'leche_a', 'leche_s'):
        return '%s ml' % fmt_g(g)
    if key == 'aceite':
        if g == 5:
            return '1 cucharadita'
        if g == 10:
            return '1 cda'
        if g == 15:
            return '1½ cda'
        if g == 20:
            return '2 cdas'
        return '%s g' % fmt_g(g)
    if key == 'choco':
        return '8 g'
    if unit:
        n = g / unit
        if abs(n - round(n)) < 0.01:
            n = int(round(n))
            return '%d ud' % n + ('' if key in ('huevo',) else ' (%s g)' % fmt_g(g))
        if abs(n * 2 - round(n * 2)) < 0.01:
            half = {0.5: '½'}.get(n, '%s½' % int(n) if n > 1 else '½')
            return '%s %s (%s g)' % (half, 'loncha' if key == 'queso_l' else 'ud', fmt_g(g))
    return '%s g' % fmt_g(g)


def meal_html(dish, items):
    lis = []
    for it in items:
        if it[0] == 'custom':
            name, q = it[2], it[3]
        else:
            name = it[3] if len(it) > 3 and it[3] else DB[it[0]][0]
            q = it[2] if len(it) > 2 and it[2] else qty_text(it[0], it[1])
        lis.append('<li><span>%s</span><span class="q">%s</span></li>' % (name, q))
    c, p, g, f = [round(x) for x in macros(items)]
    k = round(kcal(*macros(items)))
    mac = ('<div class="mac"><span><b>%d</b> HC netos</span><span><b>%d</b> P</span>'
           '<span><b>%d</b> G</span><span><b>%d</b> Fib</span><span><b>%d</b> kcal</span></div>') % (c, p, g, f, k)
    return '<p class="dish">%s</p><ul>%s</ul>%s' % (dish, ''.join(lis), mac)


def total_html(tipo, t):
    tc, tp, tg = TARGETS[tipo]
    c, p, g, f = [round(x) for x in t]
    k = round(kcal(*t))
    row = '<div class="tr"><span class="tl">%s</span><span class="tv">%d</span><span class="tg">%s</span></div>'
    return (row % ('HC netos', c, '/ %d g' % tc) + row % ('Proteína', p, '/ %d g' % tp) +
            row % ('Grasa', g, '/ %d g' % tg) + row % ('Fibra', f, '/ 25 g') + row % ('Calorías', k, 'kcal'))


def src(items):
    out = []
    for it in items:
        if it[0] == 'custom':
            out.append(['custom', [round(x, 1) for x in it[1]], it[2]])
        else:
            out.append([it[0], it[1]])
    return out


def build_day(name, date, tipo, meals):
    """meals: lista de dict(meal, dish, items, recipe=None)."""
    out = []
    tot = [0.0] * 4
    for m in meals:
        mm = macros(m['items'])
        tot = [a + b for a, b in zip(tot, mm)]
        d = {'meal': m['meal'], 'span': 1, 'cls': [], 'html': meal_html(m['dish'], m['items']),
             'src': src(m['items'])}
        if m.get('recipe'):
            d['recipe'] = m['recipe']
        out.append(d)
    return {'name': name, 'date': date, 'chip': {'cls': tipo, 'text': CHIPS[tipo]}, 'meals': out,
            'total': total_html(tipo, tot)}


def write_week(path, week, title, days):
    with open(path, 'w', encoding='utf-8') as fh:
        json.dump({'week': week, 'title': title, 'days': days}, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
