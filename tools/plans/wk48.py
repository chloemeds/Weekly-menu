"""Menú WK48 (23 a 29 nov 2026). python3 tools/plans/wk48.py -> data/wk48.json
Lunes muy ligero y martes ligero para compensar el viernes 20 (Bosco de Lobos). Martes y jueves carbs reducidos.
Miércoles sin cena: palomitas en el cine. Viernes comida fuera en El Xampanyet."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from menu import build_day, write_week  # noqa: E402

CH = ('choco', 8)
OIL = ('aceite', 5)
DAYS = []


def day(name, date, tipo, *meals):
    DAYS.append(build_day(name, date, tipo, [dict(zip(('meal', 'dish', 'items', 'recipe'), m)) for m in meals]))


MATCHA_D = ('leche_d', 150, '', 'Matcha con leche desnatada')
MATCHA_A = ('leche_a', 150, '', 'Matcha con bebida de almendra')
BUN = ('custom', [28.5, 5, 3, 1.5], 'Pan de hamburguesa', '1 ud (60 g)')

# ---------------- Lunes: regular, muy ligero
day('Lunes', '23 nov', 'reg',
    ('Desayuno', 'Matcha con bebida de almendra y leche semidesnatada (tomado)',
     [('leche_a', 75, '', 'Matcha: bebida de almendra'), ('leche_s', 75, '', '+ leche semidesnatada')]),
    ('Comida', 'Albóndigas caseras en salsa con arroz, brócoli y champiñones + kiwi y 2 barquillos (tomado)',
     [('custom', [7, 22.4, 16.8, 0], 'Albóndigas caseras', '140 g'),
      ('custom', [3, 0.5, 1.5, 0.6], 'Salsa de las albóndigas', '3 cucharadas'),
      ('custom', [28, 2.7, 0.3, 0.4], 'Arroz (cocido)', '100 g'),
      ('brocoli', 75), ('champis', 70), OIL,
      ('custom', [6.9, 0.5, 2.2, 0.3], 'Barquillos rellenos Antiu Xixona (postre)', '2 sticks (11 g)'),
      ('kiwi', 75, '1 ud', 'Kiwi (postre)')],
     ['Calienta las albóndigas con su salsa en un cazo tapado a fuego medio, 5–6 min.',
      'Brócoli en ramilletes y champiñones laminados en sartén con la cucharadita de aceite y sal, 5–6 min.',
      'Calienta el arroz 1 min en el microondas y sirve todo junto, con la salsa por encima.']),
    ('Merienda', 'Skyr con granada, arándanos, granola sin azúcar, crema de avellana y una onza de chocolate (tomado)',
     [('skyr', 200, '2 ud (200 g)'), ('granada', 30), ('arandanos', 35), ('granola', 20, '', 'Granola sin azúcar'),
      ('crema_ave', 10), CH]),
    ('Cena', 'Lubina al horno con calabacín + una esquina de tortilla de patatas (tomado)',
     [('lubina', 120), ('calabacin', 150), OIL,
      ('custom', [7.8, 3.9, 6.6, 0.6], 'Tortilla de patatas (esquina pequeña)', '~60 g'), CH],
     ['Horno a 200 °C. Calabacín en rodajas en la bandeja con la cucharadita de aceite y sal, 8 min.',
      'Pon la lubina en lomos encima con sal, pimienta y limón, 10 min más.',
      'Sirve con perejil picado.']),
    )

# ---------------- Martes: carbs reducidos, ligero
day('Martes', '24 nov', 'low',
    ('Desayuno', 'Rollitos de jamón york con queso light y dos nueces + matcha latte',
     [('york', 40), ('queso_l', 12.5), ('nueces', 8, '2 ud (8 g)'), MATCHA_A]),
    ('Comida', 'Ternera a la plancha con champiñones salteados',
     [('ternera', 160), ('champis', 150), OIL, CH],
     ['Champiñones laminados en sartén con la cucharadita de aceite y sal, 5 min, y reserva.',
      'Filetes de ternera con sal y pimienta en la misma sartén muy caliente, 2 min por lado.',
      'Sirve con unas gotas de limón y perejil.']),
    ('Merienda', 'Koukakis griego con arándanos y almendras',
     [('koukakis', 120), ('arandanos', 40), ('almendras', 10)]),
    ('Cena', 'Calamares a la plancha con alcachofas',
     [('calamar', 160), ('alcachofa', 150), OIL, CH],
     ['Alcachofas (de bote, escurridas, en cuartos) en sartén con la cucharadita de aceite, 4–5 min hasta que se doren, y reserva.',
      'Calamar en anillas o tiras, bien seco, a la sartén muy caliente con sal, 2–3 min.',
      'Sirve con perejil picado y limón.']),
    )

# ---------------- Miércoles: regular, cine por la noche
day('Miércoles', '25 nov', 'reg',
    ('Desayuno', 'Tostada integral con pechuga de pavo y queso light + matcha latte',
     [('pan_int', 45), ('pavo_l', 30), ('queso_l', 12.5), MATCHA_D]),
    ('Comida', 'Pasta con gambas y calabacín',
     [('pasta', 70), ('gambas', 170), ('calabacin', 150), OIL, CH],
     ['Pasta en agua con sal 10–11 min (o según el paquete).',
      'Calabacín en dados en sartén con la cucharadita de aceite, 5 min a fuego medio-alto.',
      'Añade las gambas con sal, pimienta y una pizca de guindilla, 2–3 min.',
      'Escurre la pasta y mézclala con la sartén y un chorrito del agua de cocer.']),
    ('Merienda', 'Koukakis 0% con kiwi y chía',
     [('koukakis0', 150), ('kiwi', 75, '1 ud'), ('chia', 10)]),
    ('Cena', 'Sin cena: palomitas en el cine (macros aproximados)',
     [('custom', [60, 6.5, 20, 8], 'Palomitas mixtas, dulces y saladas', 'medianas (~100 g)')]),
    )

# ---------------- Jueves: carbs reducidos
day('Jueves', '26 nov', 'low',
    ('Desayuno', 'Jamón serrano con queso light y nueces + matcha latte',
     [('serrano', 40), ('queso_l', 12.5), ('nueces', 8, '2 ud (8 g)'), MATCHA_A]),
    ('Comida', 'Salmón al horno con salsa de yogur y eneldo y judías verdes',
     [('salmon', 170), ('judias', 150), ('koukakis', 40, '', 'Yogur griego Koukakis (para la salsa)'), OIL, CH],
     ['Horno a 200 °C. Salmón con sal, pimienta y la cucharadita de aceite en una bandeja, 12–14 min.',
      'Mientras, judías verdes al vapor en el microondas, bol tapado con 2 cdas de agua, 6 min.',
      'Salsa: mezcla el yogur con eneldo, sal y unas gotas de limón, y ponla por encima del salmón.']),
    ('Merienda', 'Skyr con arándanos, granada, almendras y crema de avellana',
     [('skyr', 100), ('arandanos', 40), ('granada', 30), ('almendras', 10), ('crema_ave', 10)]),
    ('Cena', 'Tortilla de calabacín con mozzarella',
     [('huevo', 110, '2 ud'), ('calabacin', 150), ('mozza_l', 50), OIL, CH],
     ['Calabacín en dados finos en sartén antiadherente con la cucharadita de aceite y sal, 6 min.',
      'Bate los huevos, échalos sobre el calabacín y reparte la mozzarella en trocitos.',
      'Cuaja tapado a fuego medio-bajo 3–4 min, dale la vuelta con un plato y 1 min más.']),
    )

# ---------------- Viernes: regular, comida fuera
day('Viernes', '27 nov', 'reg',
    ('Desayuno', 'Tostada integral con jamón york + matcha latte',
     [('pan_int', 50), ('york', 40), MATCHA_D]),
    ('Comida', 'Comida en El Xampanyet: margen reservado. Cuando sepas lo que has pedido, dímelo y ajusto el día',
     [('custom', [60, 35, 24, 4], 'Unas tapas, mejor con proteína (jamón, tortilla, pescado, pulpo) y una copa de cava si te apetece', '~650 kcal')]),
    ('Merienda', 'Koukakis 0% con mandarina y granola',
     [('koukakis0', 150), ('mandarina', 140, '2 ud (140 g)'), ('granola', 15)]),
    ('Cena', 'Dorada al horno con brócoli',
     [('dorada', 150), ('brocoli', 150), OIL, CH],
     ['Horno a 200 °C. Dorada en lomos con sal, pimienta, limón y la cucharadita de aceite, 12 min.',
      'Mientras, brócoli en ramilletes al vapor en el microondas, bol tapado con 2 cdas de agua, 5 min.',
      'Sirve con unas gotas de limón.']),
    )

# ---------------- Sábado: regular
day('Sábado', '28 nov', 'reg',
    ('Desayuno', 'Tostada integral con pechuga de pavo + matcha latte',
     [('pan_int', 60), ('pavo_l', 30), MATCHA_D]),
    ('Comida', 'Hamburguesa de pollo casera con loncha light y calabacín a la plancha + kiwi',
     [BUN, ('pollo', 120, '', 'Pechuga de pollo picada (en hamburguesa)'), ('queso_l', 25), ('calabacin', 150), OIL, ('kiwi', 75, '1 ud (de postre)'), CH],
     ['Pica la pechuga (o pídela picada), sal, pimienta y pimentón, y forma una hamburguesa.',
      'Sartén caliente con la cucharadita de aceite: hamburguesa 4 min por lado; el último minuto pon la loncha encima y tapa.',
      'Calabacín en rodajas a la plancha en la misma sartén, 3 min por lado.',
      'Tuesta el pan y monta la hamburguesa; el calabacín, dentro o al lado.']),
    ('Merienda', 'Koukakis 0% con plátano y granola',
     [('koukakis0', 150), ('platano', 100, '1 ud pequeña (100 g)'), ('granola', 20)]),
    ('Cena', 'Omelette de champiñones y mozzarella',
     [('huevo', 110, '2 ud'), ('champis', 150), ('mozza_l', 30), OIL, CH],
     ['Champiñones laminados en sartén antiadherente con la cucharadita de aceite y sal, 5 min, y reserva.',
      'Bate los huevos con sal, échalos a la sartén a fuego medio y deja que cuajen por abajo 2 min.',
      'Pon los champiñones y la mozzarella en una mitad, dobla y 1 min más tapado.']),
    )

# ---------------- Domingo: regular
day('Domingo', '29 nov', 'reg',
    ('Desayuno', 'Tostada integral con jamón york, queso light y dos nueces + matcha latte',
     [('pan_int', 60), ('york', 30), ('queso_l', 12.5), ('nueces', 8, '2 ud (8 g)'), MATCHA_D]),
    ('Comida', 'Lomo a la plancha con boniato asado y judías verdes',
     [('lomo', 130), ('boniato', 250), ('judias', 150), OIL, CH],
     ['Boniato en dados con sal y pimentón: airfryer a 200 °C, 15 min (remueve a mitad).',
      'Judías verdes al vapor en el microondas, bol tapado con 2 cdas de agua, 6 min.',
      'Lomo con sal y pimienta en sartén muy caliente con la cucharadita de aceite, 2–3 min por lado.']),
    ('Merienda', 'Skyr con plátano, chía y granola',
     [('skyr', 100), ('platano', 100, '1 ud pequeña (100 g)'), ('chia', 10), ('granola', 15)]),
    ('Cena', 'Brochetas de pollo con calabacín',
     [('pollo', 125, '', 'Pechuga de pollo (en dados)'), ('calabacin', 150), OIL, CH],
     ['Pollo en dados y calabacín en rodajas gruesas con sal, pimienta, pimentón y la cucharadita de aceite.',
      'Ensártalos alternando en palitos de brocheta.',
      'Airfryer a 200 °C, 12 min, dándoles la vuelta a mitad.']),
    )

if __name__ == '__main__':
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
    write_week(os.path.join(root, 'data', 'wk48.json'), 'WK48', 'Menú WK48 · 23 al 29 de noviembre', DAYS)
