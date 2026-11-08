"""Lista de la compra WK46 -> data/compra-wk46.json (ids estables, sin matcha ni aceite)."""
import json, os
A = ' Precio aproximado (no lo he comprobado en la web de Mercadona)'
G = [
 ('Fruta y verdura', [
  ('calabacin', 'Calabacín', '<em>650 g</em> · unos 3', 0.91, 'Calabacín verde a granel, 1,40 €/kg'),
  ('judias', 'Judías verdes', '<em>700 g</em>', 1.3, 'Judía verde redonda Hacendado ultracongelada, bolsa de 1 kg'),
  ('brocoli', 'Brócoli', '<em>890 g</em> · 3 pequeños', 2.05, 'Brócoli a granel, 2,30 €/kg'),
  ('champi', 'Champiñones', '<em>150 g</em>', 1.56, 'Champiñones blancos, bandeja de 300 g'),
  ('setas', 'Setas', '<em>270 g</em>', 2.2, 'Setas de cardo u ostra, bandeja.' + A),
  ('alcachofa', 'Alcachofas', '<em>450 g</em>', 4.3, '2 tarros de corazones de alcachofa Hacendado de 430 g'),
  ('patata', 'Patata', '<em>250 g</em> · 2 medianas', 0.48, 'Patata a granel, 1,90 €/kg'),
  ('boniato', 'Boniato', '<em>150 g</em> · 1 pequeño', 0.4, 'Boniato a granel.' + A),
  ('fresa', 'Fresas', '<em>150 g</em>', 2.5, 'Fresas, tarrina de 500 g.' + A),
  ('frambuesa', 'Frambuesas', '<em>120 g</em>', 3.16, 'Frambuesas, bandeja de 200 g'),
  ('arandano', 'Arándanos', '<em>60 g</em>', 2.2, 'Arándanos, tarrina de 125 g.' + A),
  ('kiwi', 'Kiwi', '<em>2</em>', 0.7, '2 kiwis verdes sueltos'),
  ('manzana', 'Manzana', '<em>1</em> · 170 g', 0.4, 'Manzana suelta.' + A),
  ('platano', 'Plátano', '<em>1</em>', 0.3, 'Plátano de Canarias suelto.' + A),
  ('mango', 'Mango', '<em>100 g</em> · medio pequeño', 1.2, 'Mango suelto.' + A),
  ('limon', 'Limón', '<em>1</em>', 0.36, '1 limón'),
 ]),
 ('Carne y pescado', [
  ('pollo', 'Pechuga de pollo', '<em>370 g</em>', 4.0, 'Filetes pechuga de pollo, bandeja de unos 520 g'),
  ('contramuslo', 'Contramuslo de pollo sin piel', '<em>140 g</em>', 3.2, 'Contramuslo de pollo deshuesado sin piel, bandeja.' + A),
  ('pavof', 'Filetes de pechuga de pavo', '<em>110 g</em>', 5.07, 'Filetes pechuga de pavo, bandeja de unos 580 g'),
  ('lomo', 'Lomo de cerdo en filetes', '<em>130 g</em>', 3.5, 'Filetes de lomo de cerdo, bandeja pequeña.' + A),
  ('salmon', 'Salmón', '<em>120 g</em> · 1 lomo', 5.95, 'Lomos de salmón sin piel Hacendado congelados, 250 g (2 lomos)'),
  ('merluza', 'Merluza', '<em>140 g</em>', 4.5, 'Filetes de merluza Hacendado ultracongelados.' + A),
  ('dorada', 'Dorada', '<em>1 en lomos</em> · unos 140 g limpios', 4.5, 'Dorada limpia, 1 pieza (que te la abran en lomos).' + A),
  ('lubina', 'Lubina', '<em>1 en lomos</em> · unos 140 g limpios', 5.5, 'Lubina limpia, 1 pieza.' + A),
  ('bacalao', 'Bacalao fresco', '<em>130 g</em> · 1 lomo', 3.5, 'Lomo de bacalao fresco o ultracongelado.' + A),
  ('gambas', 'Gambas o langostinos pelados', '<em>120 g</em>', 4.9, 'Gamba pelada cruda mediana Hacendado ultracongelada, 360 g'),
 ]),
 ('Huevos, charcutería y lácteos', [
  ('huevos', 'Huevos', '<em>5</em>', 1.8, 'Huevos grandes L, media docena'),
  ('claras', 'Claras de huevo', '<em>150 g</em>', 1.5, 'Claras de huevo pasteurizadas Hacendado, brick.' + A),
  ('york', 'Jamón york', '<em>60 g</em>', 2.0, 'Jamón cocido extra Hacendado finas lonchas, 200 g'),
  ('pavol', 'Pechuga de pavo en lonchas', '<em>60 g</em>', 1.9, 'Pechuga de pavo en finas lonchas Hacendado.' + A),
  ('serrano', 'Jamón serrano', '<em>25 g</em>', 2.5, 'Jamón serrano en lonchas, sobre pequeño.' + A),
  ('salmonah', 'Salmón ahumado', '<em>30 g</em>', 3.0, 'Salmón ahumado Hacendado, sobre de 100 g.' + A),
  ('queso', 'Queso en lonchas cremoso light Hacendado', '<em>1 loncha</em>', 2.9, 'Queso lonchas cremoso light Hacendado, 300 g (12 lonchas)'),
  ('yogm', 'Yogur griego light Mercadona', '<em>3</em>', 1.45, 'Yogur natural al estilo griego light Hacendado, pack de 6 x 125 g'),
  ('leched', 'Leche desnatada', '<em>800 ml</em> · para el matcha', 0.81, 'Leche desnatada Hacendado, brick de 1 L'),
  ('almendra', 'Bebida de almendra sin azúcar', '<em>250 ml</em> · para el matcha', 1.1, 'Bebida de almendras 0% azúcar Hacendado, brick de 1 L'),
 ]),
 ('Despensa', [
  ('pan', 'Pan integral', '<em>150 g</em> · unas 4 rebanadas', 0.9, 'Pan de molde 100% integral Hacendado, 460 g'),
  ('baguette', 'Pan baguette', '<em>60 g</em> · un trozo', 0.45, 'Barra de pan del día.' + A),
  ('tortitas', 'Tortitas de arroz', '<em>3</em>', 1.0, 'Tortitas de arroz Hacendado.' + A),
  ('arroz', 'Arroz blanco', '<em>80 g</em>', 1.2, 'Arroz largo Hacendado, 1 kg'),
  ('pastaint', 'Pasta integral', '<em>90 g</em>', 1.0, 'Macarrones o espaguetis integrales Hacendado, 500 g.' + A),
  ('gnocchi', 'Gnocchi de patata', '<em>200 g</em>', 1.5, 'Gnocchi de patata Hacendado (nevera), 500 g.' + A),
  ('pesto', 'Pesto', '<em>15 g</em> · si no te queda', 2.0, 'Salsa pesto Hacendado, tarro.' + A),
  ('granola', 'Granola sin azúcar', '<em>40 g</em>', 1.9, 'Muesli Crunchy Hacendado sin azúcares añadidos, 500 g'),
  ('chia', 'Chía', '<em>32 g</em>', 2.05, 'Semillas de chía Hacendado, 250 g'),
  ('sesamo', 'Sésamo', '<em>5 g</em>', 1.2, 'Sésamo tostado Hacendado.' + A),
  ('almendras', 'Almendras', '<em>20 g</em> · 10 g laminadas', 2.3, 'Almendra natural Hacendado, 200 g (o laminada)'),
  ('nueces', 'Nueces', '<em>25 g</em>', 1.7, 'Nuez troceada pelada Hacendado, 150 g'),
  ('cremaave', 'Crema de avellana y cacao Ametller', '<em>20 g</em> · la que tienes', 0, 'Ya la tienes en casa'),
  ('choco', 'Chocolate negro 72% Mercadona', '<em>14 onzas</em> · 2 tabletas', 3.3, 'Chocolate negro 72% cacao Hacendado, tableta de 100 g (1,65 € cada una)'),
  ('canela', 'Canela', '<em>un poco</em>', 1.0, 'Canela molida Hacendado, bote'),
 ]),
 ('Fuera de Mercadona', [
  ('kouk0', 'Yogur griego Koukakis 0%', '<em>1</em>', 0.99, 'Precio aproximado', True),
  ('skyr', 'Skyr natural Danone', '<em>3</em>', 2.75, 'Precio aproximado, pack de 4', True),
 ]),
]
out = {'week': 'WK46', 'title': 'Lista de la compra · WK46 · 9 al 15 nov',
       'note': 'Todo lo del menú WK46 de lunes a domingo, sin matcha ni aceite. Precios de Mercadona (tienda de Madrid); los marcados como aproximados no los he podido comprobar. Marca lo que ya tienes en casa y te queda a la vista lo que falta.',
       'groups': [{'name': n, 'items': [{'id': i[0], 'name': i[1], 'qty': i[2], 'price': i[3], 'out': len(i) > 5 and i[5], 'buy': i[4]} for i in its]} for n, its in G]}
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
json.dump(out, open(os.path.join(root, 'data', 'compra-wk46.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(sum(i['price'] for g in out['groups'] for i in g['items']))
