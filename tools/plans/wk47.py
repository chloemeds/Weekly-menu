"""Menú WK47 (16 a 22 nov 2026). python3 tools/plans/wk47.py  -> escribe data/wk47.json
Semana ligera: cenas fuera viernes (Bosque de Lobos), sábado (Parco Sushi) y domingo (Salsa, mexicano).
Lunes y martes con menos grasa para compensar WK46."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from menu import build_day, write_week, macros  # noqa: E402

CH = ('choco', 8)
OIL = ('aceite', 5)
DAYS = []


def day(name, date, tipo, *meals):
    DAYS.append(build_day(name, date, tipo, [dict(zip(('meal', 'dish', 'items', 'recipe'), m)) for m in meals]))


MATCHA_D = ('leche_d', 150, '', 'Matcha con leche desnatada')
MATCHA_A = ('leche_a', 150, '', 'Matcha con bebida de almendra')

# ---------------- Lunes: regular (sencillo, sin compra del domingo)
day('Lunes', '16 nov', 'reg',
    ('Desayuno', 'Matcha con plátano congelado y espuma de Koukakis y canela + tostada de payés con york y queso (tomado)',
     [('leche_d', 200, '150 ml + 50 ml para la espuma', 'Leche desnatada'), ('platano', 50, 'unos ⅖ de plátano mediano (50 g, congelado)'),
      ('koukakis', 15, '1 cucharada (~15 g)'), ('custom', [17.9, 3.2, 0.5, 0.9], 'Pan de payés', '35 g'), ('queso_l', 12.5), ('york', 30)]),
    ('Comida', 'Contramuslo de pavo a la plancha con ñoquis y judías verdes (tomado)',
     [('gnocchi', 150), ('contramuslo_pavo', 140), ('judias', 150), OIL],
     ['Judías verdes al vapor en el microondas, bol tapado con 2 cdas de agua, 6 min.',
      'Contramuslo abierto en filete, con sal, pimienta y pimentón: sartén caliente con la cucharadita de aceite, 5–6 min por lado, y reserva.',
      'Ñoquis en agua hirviendo con sal hasta que floten (2–3 min) y escúrrelos.',
      'Saltéalos 2 min en la misma sartén del pavo para que se doren un poco y sirve todo junto.']),
    ('Merienda', 'Skyr con kiwi, granola y almendras (tomado)',
     [('skyr', 100), ('kiwi', 75, '1 ud'), ('granola', 15), ('almendras', 5, '4 ud (~5 g)')]),
    ('Cena', 'Dorada al horno con calabacín + Koukakis con crema de cacao (tomado)',
     [('dorada', 150), ('calabacin', 150), OIL, ('koukakis', 45), ('crema_ave', 10)],
     ['Horno a 200 °C. Calabacín en rodajas en la bandeja con sal y la cucharadita de aceite, 8 min.',
      'Pon la dorada en lomos encima con sal, pimienta y limón, 10–12 min más.',
      'Sirve con perejil picado.']),
    )

# ---------------- Martes: carbs reducidos
day('Martes', '17 nov', 'low',
    ('Desayuno', 'Tostada integral con queso light y york + matcha latte',
     [('pan_int', 30), ('york', 40), ('queso_l', 12.5), MATCHA_A]),
    ('Comida', 'Muslos de pollo con setas',
     [('custom', [0, 38, 12, 0], 'Muslo de pollo sin piel', '2 ud (~200 g de carne)'),
      ('setas', 150), OIL, CH],
     ['Muslos con sal, pimienta y pimentón: airfryer a 200 °C, 20–22 min, dándole la vuelta a mitad.',
      'Mientras, setas troceadas en la sartén con la cucharadita de aceite y sal, 5–6 min.',
      'Sirve los muslos sobre las setas.']),
    ('Merienda', 'Koukakis griego con arándanos',
     [('koukakis', 150), ('arandanos', 40)]),
    ('Cena', 'Lubina al horno con brócoli',
     [('lubina', 150), ('brocoli', 150), OIL, CH],
     ['Horno a 200 °C. Lubina en lomos en una bandeja con sal, pimienta, limón y la cucharadita de aceite, 10–12 min.',
      'Mientras, brócoli en ramilletes al vapor en el microondas, bol tapado con 2 cdas de agua, 5 min.',
      'Sirve la lubina con el brócoli y unas gotas de limón.']),
    )

# ---------------- Miércoles: regular
day('Miércoles', '18 nov', 'reg',
    ('Desayuno', 'Tostada integral con pechuga de pavo + matcha latte',
     [('pan_int', 50), ('pavo_l', 30), MATCHA_D]),
    ('Comida', 'Sopa de caldo de pollo con fideos + filete de pavo con judías verdes',
     [('custom', [1, 1.5, 0.5, 0], 'Caldo de pollo', '350 ml'), ('pasta', 65, '65 g (en crudo)', 'Fideos'),
      ('pavo', 120), ('judias', 150), OIL, CH],
     ['Calienta el caldo; cuando hierva, echa los fideos y cuécelos el tiempo del paquete (4–5 min).',
      'Judías verdes al vapor en el microondas, bol tapado con 2 cdas de agua, 6 min.',
      'Filete de pavo con sal y pimienta: sartén caliente con la cucharadita de aceite, 3 min por lado.',
      'Primero la sopa y de segundo el pavo con las judías.']),
    ('Merienda', 'Skyr con plátano y crema de avellana',
     [('skyr', 100), ('platano', 120, '1 mediano (120 g pelado)'), ('crema_ave', 10)]),
    ('Cena', 'Tortilla francesa con champiñones',
     [('huevo', 110, '2 ud'), ('champis', 150), OIL, CH],
     ['Champiñones laminados en la sartén con la cucharadita de aceite y sal, 5 min a fuego medio-alto.',
      'Bate los 2 huevos con sal y pimienta y échalos sobre los champiñones.',
      'Cuaja 2 min a fuego medio, dobla la tortilla y sirve.']),
    )

# ---------------- Jueves: carbs reducidos
day('Jueves', '19 nov', 'low',
    ('Desayuno', 'Tortilla francesa de 2 huevos con jamón york + matcha latte',
     [('huevo', 110, '2 ud'), ('york', 20), MATCHA_A]),
    ('Comida', 'Pollo al limón con brócoli',
     [('pollo', 150), ('brocoli', 150), OIL, CH],
     ['Pechuga en tacos con sal, pimienta y la ralladura de medio limón.',
      'Brócoli en ramilletes al vapor en el microondas, bol tapado con 2 cdas de agua, 4 min.',
      'Sartén con la cucharadita de aceite: pollo 5–6 min, añade el brócoli 2 min y el zumo del limón al final.']),
    ('Merienda', 'Koukakis griego con frambuesas',
     [('koukakis', 150), ('frambuesas', 100)]),
    ('Cena', 'Salmón al horno con judías verdes',
     [('salmon', 130), ('judias', 150), OIL, CH],
     ['Horno a 200 °C. Salmón con sal, pimienta y eneldo en una bandeja con la cucharadita de aceite, 12 min.',
      'Judías verdes al vapor en el microondas, bol tapado con 2 cdas de agua, 6 min.',
      'Sirve el salmón con las judías y unas gotas de limón.']),
    )

# ---------------- Viernes: regular, cena en Bosque de Lobos
day('Viernes', '20 nov', 'reg',
    ('Desayuno', 'Tostada integral con jamón york + matcha latte',
     [('pan_int', 40), ('york', 30), MATCHA_D]),
    ('Comida', 'Merluza a la plancha con judías verdes',
     [('merluza', 170), ('judias', 150), OIL],
     ['Judías verdes al vapor en el microondas, bol tapado con 2 cdas de agua, 6 min.',
      'Seca la merluza, sal y pimienta: sartén caliente con la cucharadita de aceite, 3 min por la piel y 2 min por el otro lado.',
      'Sirve con las judías, unas gotas de limón y una pizca de pimentón.']),
    ('Cena', 'Cena en Bosque de Lobos (estimado)',
     [('custom', [23, 7, 6, 1], 'Pizza margherita (compartida)', '1 porción'),
      ('custom', [6, 2, 4.5, 0.3], 'Croqueta de jamón ibérico', '1 ud'),
      ('custom', [3, 5, 9, 2], 'Alcachofas a la plancha con burrata y panceta (compartidas)', 'un poco'),
      ('custom', [45, 12, 18, 2], 'Rigatoni gratinados y trufados', '½ ración'),
      ('custom', [22, 25, 18, 2], 'Tagliata de solomillo con portobello y patatas', '½ ración'),
      ('custom', [20, 6, 20, 0], 'Tarta de queso parmesano', '⅔ de porción'),
      ('custom', [0, 0, 0, 0], 'Ron con cola zero (unas 110 kcal de alcohol cada uno, no suman macros)', '3 copas')]),
    )

# ---------------- Sábado: regular, cena en Parco Sushi
day('Sábado', '21 nov', 'reg',
    ('Comida', 'Brochetas de pollo con calabacín',
     [('pollo', 150), ('calabacin', 150), OIL, CH],
     ['Pollo en tacos y calabacín en rodajas gruesas con sal, pimienta, pimentón y la cucharadita de aceite.',
      'Ensártalos alternando en brochetas.',
      'Airfryer a 200 °C, 12–14 min, dándoles la vuelta a mitad.']),
    ('Merienda', 'Skyr con fresas',
     [('skyr', 100), ('fresas', 150)]),
    ('Cena', 'Cena en Parco Sushi (estimado)',
     [('custom', [0, 6, 0.5, 0], 'Sashimi de gamba', '2 piezas'),
      ('custom', [44, 21, 18, 1], 'Nigiris: salmón, gamba, pez mantequilla, vieira, anguila y toro', '6 piezas'),
      ('custom', [14, 4, 5, 0.5], 'Maki de gamba', '2 piezas'),
      ('custom', [14, 4, 6, 1], 'Maki de gamba y aguacate', '2 piezas'),
      ('custom', [28, 3.5, 11, 0.5], 'Saquitos de helado de vainilla en pasta filo (postre)', '2 ud'),
      ('custom', [7, 1, 4.5, 0.5], 'Chocolate caliente para mojar', '~15 g')]),
    )

# ---------------- Domingo: regular, cena en Salsa (mexicano)
day('Domingo', '22 nov', 'reg',
    ('Desayuno', 'Matcha latte (el brunch hace de desayuno y comida)',
     [MATCHA_D]),
    ('Comida', 'Brunch en casa de una amiga (estimado, por confirmar)',
     [('custom', [35, 15, 6, 2], 'Pan con jamón', '2 tostas pequeñas'),
      ('custom', [15, 7, 12, 1.5], 'Tortilla de patatas', '1 pincho'),
      ('custom', [15, 2, 10, 1], 'Patatas chips', 'un puñado (~30 g)')]),
    ('Merienda', 'Skyr con kiwi',
     [('skyr', 100), ('kiwi', 75)]),
    ('Cena', 'Cena en Salsa, mexicano (estimado; dime qué pides y lo ajusto)',
     [('custom', [30, 6, 12, 4], 'Nachos con guacamole (compartidos)', 'un poco'),
      ('custom', [45, 30, 22, 4], 'Tacos o fajitas de pollo', '3 tacos'),
      ('custom', [10, 1, 5, 0], 'Bebida o postre (compartido)', '—')]),
    )

if __name__ == '__main__':
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
    write_week(os.path.join(root, 'data', 'wk47.json'), 'WK47', 'Menú WK47 · 16 al 22 de noviembre', DAYS)
    import re
    tot = [0] * 5
    for d in DAYS:
        v = [float(x) for x in re.findall(r'tv">([^<]*)', d['total'])]
        tot = [a + b for a, b in zip(tot, v)]
        print(d['name'], d['chip']['cls'], v, [re.findall(r'<b>([^<]*)', m['html'])[-5:] for m in d['meals']])
    print('semana', tot, 'objetivo 790/721/400(-32 F de WK46)')
