"""Menú WK48 (23 a 29 nov 2026). python3 tools/plans/wk48.py -> data/wk48.json
Lunes muy ligero y martes ligero para compensar el viernes 20 (Bosco de Lobos). Martes y jueves carbs reducidos.
Viernes comida fuera en El Xampanyet."""
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
    ('Desayuno', 'Jamón york, queso light y fuet + Cinnamon Cloud en Reset Matcha (tomado)',
     [('york', 35), ('queso_l', 25), ('fuet', 12),
      ('custom', [4, 0.8, 1.9, 0], 'Matcha con Alpro Barista almendra', '155 ml'),
      ('custom', [1.5, 0.1, 1, 0], 'Cloud de canela', '~10 g')]),
    ('Comida', 'Entraña y pechuga de pollo a la plancha con champiñones salteados + kiwi y onza (tomado)',
     [('custom', [0, 15.6, 9.8, 0], 'Entraña', '82 g'), ('pollo', 53), ('champis', 130), OIL, CH,
      ('kiwi', 75, '1 ud', 'Kiwi (postre)')],
     ['Champiñones laminados en sartén con la cucharadita de aceite y sal, 5 min, y reserva.',
      'Pechuga en filetes finos con sal y pimienta en la misma sartén muy caliente, 3 min por lado, y reserva.',
      'Entraña con sal gorda a la sartén bien caliente, 2–3 min por lado; deja reposar 2 min y córtala en tiras.',
      'Sirve con los champiñones, unas gotas de limón y perejil.']),
    ('Merienda', 'Yogur griego Mercadona con granada, chía, miel, Chocapic y nueces (tomado)',
     [('custom', [4.8, 4.4, 12, 0], 'Yogur griego Mercadona', '1 ud (125 g)'), ('granada', 40), ('chia', 10),
      ('custom', [5.7, 0, 0, 0], 'Miel', '1 cucharadita (7 g)'),
      ('custom', [4.3, 0.5, 0.3, 0.4], 'Chocapic chocolate', '6 g'), ('nueces', 10, '2,5 ud (10 g)')]),
    ('Cena', 'Lubina a la plancha con alcachofas y fuet (tomado)',
     [('lubina', 120), ('alcachofa', 155), ('fuet', 10), OIL, CH],
     ['Alcachofas en láminas en sartén con la cucharadita de aceite, 5 min, y reserva.',
      'Lubina con sal y pimienta en la misma sartén, 3 min por la piel y 2 min por el otro lado.',
      'Sirve con las alcachofas y unas rodajas de fuet.']),
    )

# ---------------- Miércoles: regular
day('Miércoles', '25 nov', 'reg',
    ('Desayuno', 'Queso light, jamón york y nueces + matcha latte (tomado)',
     [('queso_l', 25), ('york', 25), ('nueces', 12, '3 ud (12 g)'), ('custom', [9.4, 6.2, 3.2, 0], 'Matcha con leche semidesnatada Asturiana Hostelería', '200 ml')]),
    ('Comida', 'Lentejas de casa con chorizo + muslo y alita de pollo (tomado)',
     [('lentejas', 71, '~250 g de guiso (71 g en crudo)', 'Lentejas (plato normal)'),
      ('custom', [1.2, 3, 6.5, 0.6], 'Chorizo y sofrito del guiso', '2 trocitos de chorizo'),
      ('custom', [0, 17, 12, 0], 'Muslo de pollo con piel', '1 ud (~100 g de carne y piel)'), ('custom', [0, 6, 5, 0], 'Alita de pollo', '1 ud'), OIL, ('custom', [3.45, 0.25, 1.1, 0.15], 'Stick de barquillo (postre)', '1 ud')],
     ['Calienta un plato normal de lentejas (unos 250 g), con solo 2 trocitos de chorizo.',
      'Muslo y alita con sal y pimienta en sartén con la cucharadita de aceite, 5–6 min por lado a fuego medio.',
      'Primero las lentejas y de segundo el pollo.']),
    ('Merienda', 'Skyr y yogur griego light con kiwi y granola + matcha latte (tomado)',
     [('skyr', 100), ('yog_light', 62.5, '½ ud (62 g)', 'Yogur griego light Mercadona'), ('kiwi', 75, '1 ud'), ('granola', 20), MATCHA_D]),
    ('Cena', 'Revuelto de judías verdes',
     [('huevo', 55, '1 ud'), ('custom', [0.2, 3.6, 0, 0], 'Clara de huevo', '1 ud'), ('judias', 150), OIL],
     ['Judías verdes en trozos al vapor en el microondas, bol tapado con 2 cdas de agua, 6 min.',
      'Saltéalas 1 min en sartén antiadherente con la cucharadita de aceite y sal.',
      'Añade el huevo y la clara batidos y remueve a fuego suave 1–2 min, hasta que cuajen jugosos.']),
    )

# ---------------- Jueves: carbs reducidos
day('Jueves', '26 nov', 'low',
    ('Desayuno', 'Huevos revueltos con queso Cadí y jamón york, dos nueces + matcha latte (tomado)',
     [('huevo', 110, '2 ud'), ('custom', [0, 3.5, 4.6, 0], 'Queso Cadí', '14 g'), ('york', 30), ('nueces', 8, '2 ud (8 g)'), MATCHA_A]),
    ('Comida', 'Hamburguesa de ternera con judías verdes + kiwi (tomado)',
     [('custom', [1.9, 22.3, 11.2, 0], 'Hamburguesa de ternera ecológica Ametller Origen', '1 ud (120 g)'), ('judias', 150), OIL, ('kiwi', 75, '1 ud'), CH],
     ['Judías verdes al vapor en el microondas, bol tapado con 2 cdas de agua, 6 min.',
      'Hamburguesa en sartén con la cucharadita de aceite a fuego medio-alto, 4 min por lado (o airfryer a 190 °C, 10 min, dándole la vuelta a mitad).',
      'Sirve sin pan con las judías; el kiwi y la onza de postre.']),
    ('Merienda', 'Skyr con granada + yogur helado griego Myka con chocolate y baklava (tomado)',
     [('skyr', 100, '1 ud'), ('granada', 15), ('custom', [52, 8, 22.5, 1], 'Yogur helado griego Myka pequeño con chocolate y baklava (estimado)', '1 ud')]),
    ('Cena', 'Salmón a la plancha (tomado)',
     [('salmon', 90), OIL],
     ['Salmón con sal y pimienta en sartén con la cucharadita de aceite, 4 min por la piel y 3 min por el otro lado.',
      'Sirve con unas gotas de limón o un chorrito de soja.']),
    )

# ---------------- Viernes: regular, comida fuera
day('Viernes', '27 nov', 'reg',
    ('Desayuno', 'Tostada integral con jamón york + matcha latte',
     [('pan_int', 50), ('york', 40), MATCHA_D]),
    ('Comida', 'Comida en El Xampanyet: margen reservado. Cuando sepas lo que has pedido, dímelo y ajusto el día',
     [('custom', [60, 35, 24, 4], 'Unas tapas, mejor con proteína (jamón, tortilla, pescado, pulpo) y una copa de cava si te apetece', '~650 kcal')]),
    ('Merienda', 'Yogur griego light con mandarina y granola',
     [('yog_light', 125, '1 ud (125 g)', 'Yogur griego light Mercadona'), ('mandarina', 140, '2 ud (140 g)'), ('granola', 15)]),
    ('Cena', 'Dorada al horno con brócoli',
     [('dorada', 150), ('brocoli', 150), OIL],
     ['Horno a 200 °C. Dorada en lomos con sal, pimienta, limón y la cucharadita de aceite, 12 min.',
      'Mientras, brócoli en ramilletes al vapor en el microondas, bol tapado con 2 cdas de agua, 5 min.',
      'Sirve con unas gotas de limón.']),
    )

# ---------------- Sábado: regular
day('Sábado', '28 nov', 'reg',
    ('Desayuno', 'Tostada integral con pechuga de pavo + matcha latte',
     [('pan_int', 60), ('pavo_l', 30), MATCHA_D]),
    ('Comida', 'Pasta al pesto con gambas y calabacín',
     [('pasta', 80), ('gambas', 120), ('calabacin', 120), ('pesto', 15), OIL, CH],
     ['Pasta en agua con sal 10–11 min (o según el paquete).',
      'Calabacín en dados en sartén con la cucharadita de aceite, 5 min a fuego medio-alto.',
      'Añade las gambas con sal, pimienta y una pizca de guindilla, 2–3 min.',
      'Escurre la pasta y mézclala con la sartén, el pesto y un chorrito del agua de cocer.']),
    ('Merienda', 'Yogur griego light con plátano y granola',
     [('yog_light', 125, '1 ud (125 g)', 'Yogur griego light Mercadona'), ('platano', 100, '1 ud pequeña (100 g)'), ('granola', 20)]),
    ('Cena', 'Omelette de champiñones',
     [('huevo', 110, '2 ud'), ('champis', 150, '8 champiñones medianos'), OIL, CH],
     ['Champiñones laminados en sartén antiadherente con la cucharadita de aceite y sal, 5 min, y reserva.',
      'Bate los huevos con sal, échalos a la sartén a fuego medio y deja que cuajen por abajo 2 min.',
      'Pon los champiñones en una mitad, dobla y 1 min más tapado.']),
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
    ('Merienda', 'Yogur griego light con plátano y granola',
     [('yog_light', 125, '1 ud (125 g)', 'Yogur griego light Mercadona'), ('platano', 100, '1 ud pequeña (100 g)'), ('granola', 15)]),
    ('Cena', 'Brochetas de pollo con calabacín',
     [('pollo', 125, '', 'Pechuga de pollo (en dados)'), ('calabacin', 150), OIL, CH],
     ['Pollo en dados y calabacín en rodajas gruesas con sal, pimienta, pimentón y la cucharadita de aceite.',
      'Ensártalos alternando en palitos de brocheta.',
      'Airfryer a 200 °C, 12 min, dándoles la vuelta a mitad.']),
    )

if __name__ == '__main__':
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
    write_week(os.path.join(root, 'data', 'wk48.json'), 'WK48', 'Menú WK48 · 23 al 29 de noviembre', DAYS)
