"""Menú WK46 (9 a 15 nov 2026). python3 tools/plans/wk46.py  -> escribe data/wk46.json"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from menu import build_day, write_week  # noqa: E402

CH = ('choco', 8)
DAYS = []


def day(name, date, tipo, *meals):
    DAYS.append(build_day(name, date, tipo, [dict(zip(('meal', 'dish', 'items', 'recipe'), m)) for m in meals]))


# ---------------- Lunes: regular
day('Lunes', '9 nov', 'reg',
    ('Desayuno', 'Tostada integral con pechuga de pavo + matcha latte',
     [('pan_int', 50), ('pavo_l', 30), ('leche_d', 150, '', 'Matcha con leche desnatada')]),
    ('Comida', 'Arroz salteado con pollo, calabacín y brócoli',
     [('arroz', 80), ('pollo', 120), ('calabacin', 150), ('brocoli', 120), ('aceite', 10), CH],
     ['Arroz en agua con sal 12 min (o según el paquete) y escurre.',
      'Pollo en tacos con sal y pimienta: sartén con la mitad del aceite a fuego fuerte, 5–6 min y reserva.',
      'Calabacín en dados y brócoli en ramilletes pequeños en la misma sartén con el resto del aceite, 6–7 min.',
      'Junta el arroz, el pollo y las verduras 1–2 min con un chorrito de soja si quieres.']),
    ('Merienda', 'Skyr con fresas, chía y granola',
     [('skyr', 100), ('fresas', 150), ('chia', 12), ('granola', 20)]),
    ('Cena', 'Merluza al horno con judías verdes y almendras laminadas',
     [('merluza', 140), ('judias', 200), ('almendras', 10, '', 'Almendras laminadas'), ('aceite', 5), CH],
     ['Horno a 200 °C. Merluza en una bandeja con sal, pimienta, limón y unas gotas del aceite, 12–14 min.',
      'Judías verdes al vapor: bol con 2 cdas de agua, tapado, microondas 6–7 min.',
      'Tuesta las almendras en una sartén sin aceite 1–2 min y échalas por encima de las judías con el resto del aceite.']),
    )

# ---------------- Martes: carbs reducidos
day('Martes', '10 nov', 'low',
    ('Desayuno', 'Revuelto de 2 huevos con jamón york + matcha latte',
     [('huevo', 110, '2 ud'), ('york', 30), ('leche_a', 150, '', 'Matcha con bebida de almendra')]),
    ('Comida', 'Salmón al horno con brócoli y sésamo',
     [('salmon', 120), ('brocoli', 200), ('sesamo', 5), ('aceite', 10), CH],
     ['Horno a 200 °C. Salmón con sal y pimienta en una bandeja, 12–14 min.',
      'Brócoli en ramilletes al vapor en el microondas, bol tapado con 2 cdas de agua, 4–5 min.',
      'Saltea el brócoli 2 min en sartén con el aceite y una pizca de sal.',
      'Sirve con el sésamo por encima.']),
    ('Merienda', 'Yogur griego light con frambuesas y nueces',
     [('yog_light', 125), ('frambuesas', 120), ('nueces', 15)]),
    ('Cena', 'Contramuslos de pollo a la plancha con setas y alcachofas',
     [('muslo', 140), ('setas', 150), ('alcachofa', 150), ('aceite', 10), CH],
     ['Contramuslos con sal, pimienta y pimentón: sartén caliente con la mitad del aceite, 5 min por lado.',
      'Setas troceadas y alcachofas (de bote, escurridas, en cuartos) en la misma sartén con el resto del aceite, 6–7 min.',
      'Sirve el pollo sobre las verduras con perejil picado.']),
    )

# ---------------- Miércoles: carbs reducidos, cena temprana
day('Miércoles', '11 nov', 'low',
    ('Desayuno', 'Tortilla francesa de 2 huevos con queso light + matcha latte',
     [('huevo', 110, '2 ud'), ('queso_l', 12.5), ('leche_a', 100, '', 'Matcha: bebida de almendra'),
      ('leche_d', 50, '', '+ leche desnatada')]),
    ('Comida', 'Lomo de cerdo a la plancha con judías verdes y brócoli',
     [('lomo', 130), ('judias', 150), ('brocoli', 120), ('aceite', 20), CH],
     ['Judías verdes y brócoli al vapor en el microondas, bol tapado con 2 cdas de agua, 5–6 min.',
      'Lomo en filetes con sal y pimienta: sartén muy caliente con 1 cdta de aceite, 2–3 min por lado, y reserva.',
      'Saltea las verduras en la misma sartén con el resto del aceite y una pizca de ajo en polvo, 3 min.']),
    ('Merienda', 'Yogur griego light con arándanos, almendras y crema de avellana',
     [('yog_light', 125), ('arandanos', 60), ('almendras', 10), ('crema_ave', 10)]),
    ('Cena', 'Dorada al horno con alcachofas y calabacín (cena temprana)',
     [('dorada', 140), ('alcachofa', 150), ('calabacin', 150), ('aceite', 10), CH],
     ['Horno a 200 °C. Calabacín en rodajas y alcachofas en una bandeja con 2/3 del aceite y sal, 5 min.',
      'Añade la dorada en lomos con sal, pimienta, limón y el resto del aceite.',
      'Hornea 12 min más, hasta que el pescado se separe en láminas.']),
    )

# ---------------- Jueves: regular, cena fuera
day('Jueves', '12 nov', 'reg',
    ('Desayuno', 'Tostada integral con jamón york + matcha latte',
     [('pan_int', 45), ('york', 30), ('leche_d', 150, '', 'Matcha con leche desnatada')]),
    ('Comida', 'Pollo con boniato asado y brócoli (comida ligera, cenas fuera)',
     [('pollo', 140), ('boniato', 150), ('brocoli', 150), ('aceite', 5), CH],
     ['Boniato en dados con la mitad del aceite, pimentón y sal: airfryer a 200 °C, 15 min (remueve a mitad).',
      'Brócoli al vapor en el microondas, bol tapado con 2 cdas de agua, 4–5 min.',
      'Pollo en filetes finos con sal y pimienta: sartén caliente con el resto del aceite, 3–4 min por lado.']),
    ('Merienda', 'Skyr con kiwi y chía',
     [('skyr', 100), ('kiwi', 150, '2 ud'), ('chia', 10)]),
    ('Cena', 'Cena en Bar Patata: margen reservado. Cuando sepas lo que has pedido, dímelo y ajusto el día',
     [('custom', (48, 28, 20, 5), 'Unas tapas o un plato, mejor con proteína (pollo, pescado, huevo, jamón)', '~500 kcal'), CH]),
    )

# ---------------- Viernes: regular
day('Viernes', '13 nov', 'reg',
    ('Desayuno', 'Tostada integral con salmón ahumado + matcha latte',
     [('pan_int', 55), ('salmon_ahum', 30), ('leche_d', 150, '', 'Matcha con leche desnatada')]),
    ('Comida', 'Pasta integral con gambas y calabacín',
     [('pasta_int', 90), ('gambas', 120), ('calabacin', 200), ('aceite', 5), CH],
     ['Pasta en agua con sal 10–11 min (o según el paquete).',
      'Calabacín en dados en sartén con el aceite, 5 min a fuego medio-alto.',
      'Añade las gambas con sal, pimienta y una pizca de guindilla, 2–3 min.',
      'Escurre la pasta, mézclala con la sartén y un chorrito del agua de cocer.']),
    ('Merienda', 'Yogur griego light con manzana asada, canela y nueces',
     [('yog_light', 125), ('manzana', 170), ('nueces', 10)]),
    ('Cena', 'Pavo a la plancha con brócoli y setas',
     [('pavo', 110), ('brocoli', 150), ('setas', 120), ('aceite', 10), CH],
     ['Brócoli al vapor en el microondas, bol tapado con 2 cdas de agua, 4–5 min.',
      'Filetes de pavo con sal y pimienta: sartén caliente con 1 cdta de aceite, 3 min por lado, y reserva.',
      'Setas y brócoli en la misma sartén con el resto del aceite, 4–5 min.']),
    )

# ---------------- Sábado: regular
day('Sábado', '14 nov', 'reg',
    ('Desayuno', 'Bocadillo pequeño de baguette con jamón serrano + matcha latte',
     [('baguette', 60), ('serrano', 25), ('leche_d', 150, '', 'Matcha con leche desnatada')]),
    ('Comida', 'Lubina al horno con patatas y judías verdes',
     [('lubina', 140), ('patata', 250), ('judias', 200), ('aceite', 5), CH],
     ['Patata en rodajas finas con el aceite y sal: airfryer a 190 °C, 15 min (o microondas 7 min y luego al horno).',
      'Horno a 200 °C: pon la lubina en lomos sobre las patatas con sal y limón, 10–12 min.',
      'Judías verdes al vapor en el microondas, bol tapado con 2 cdas de agua, 6 min.']),
    ('Merienda', 'Koukakis 0% con mango y granola',
     [('koukakis0', 150), ('mango', 100), ('granola', 20)]),
    ('Cena', 'Tortilla de alcachofas y calabacín',
     [('huevo', 55, '1 ud'), ('claras', 150), ('alcachofa', 150), ('calabacin', 150), ('aceite', 5), CH],
     ['Calabacín en dados finos y alcachofas (de bote, escurridas, en láminas) en sartén antiadherente con el aceite, 6 min.',
      'Bate el huevo con las claras y sal, échalos sobre la verdura.',
      'Cuaja a fuego medio-bajo tapado 3–4 min, dale la vuelta con un plato y 1–2 min más.']),
    )

# ---------------- Domingo: regular
day('Domingo', '15 nov', 'reg',
    ('Desayuno', 'Tortitas de arroz con pavo y queso light + matcha latte',
     [('tortita', 24, '3 ud (24 g)'), ('pavo_l', 30), ('queso_l', 12.5), ('leche_d', 150, '', 'Matcha con leche desnatada')]),
    ('Comida', 'Gnocchi salteados con pollo, champiñones y pesto',
     [('gnocchi', 200), ('pollo', 110), ('champis', 150), ('aceite', 5), ('pesto', 15), CH],
     ['Gnocchi en agua hirviendo con sal hasta que floten, 2–3 min, y escurre.',
      'Pollo en tacos con sal y pimienta en sartén con el aceite, 5 min.',
      'Añade los champiñones laminados 4 min y luego los gnocchi 2 min para que se doren un poco.',
      'Fuera del fuego, mezcla con el pesto.']),
    ('Merienda', 'Skyr con plátano, chía y crema de avellana',
     [('skyr', 100), ('platano', 100), ('chia', 10), ('crema_ave', 10)]),
    ('Cena', 'Bacalao al horno con brócoli y judías verdes',
     [('bacalao', 130), ('brocoli', 150), ('judias', 150), ('aceite', 10), CH],
     ['Horno a 200 °C. Bacalao en una bandeja con sal, pimienta, pimentón y la mitad del aceite, 12–14 min.',
      'Mientras, brócoli y judías verdes al vapor en el microondas, bol tapado con 2 cdas de agua, 6 min.',
      'Aliña las verduras con el resto del aceite y sal.']),
    )

if __name__ == '__main__':
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
    write_week(os.path.join(root, 'data', 'wk46.json'), 'WK46', 'Menú WK46 · 9 al 15 de noviembre', DAYS)
