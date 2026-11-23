"""Lista de la compra WK48 -> data/compra-wk48.json (ids estables, sin matcha ni aceite)."""
import json, os
A = ' Precio aproximado (no lo he comprobado en la web de Mercadona)'
G = [
 ('Fruta y verdura', [
  ('judias', 'Judías verdes', '<em>450 g</em>', 1.3, 'Judía verde redonda Hacendado ultracongelada, bolsa de 1 kg'),
  ('calabacin', 'Calabacín', '<em>600 g</em> · unos 3', 0.84, 'Calabacín verde a granel, 1,40 €/kg'),
  ('champi', 'Champiñones', '<em>300 g</em>', 1.56, 'Champiñones blancos, bandeja de 300 g'),
  ('setas', 'Setas', '<em>150 g</em>', 2.2, 'Setas de cardo u ostra, bandeja.' + A),
  ('brocoli', 'Brócoli', '<em>150 g</em> · 1 pequeño', 0.4, 'Brócoli a granel, 2,30 €/kg'),
  ('alcachofa', 'Alcachofas', '<em>150 g</em>', 2.15, 'Corazones de alcachofa Hacendado, tarro de 430 g'),
  ('patata', 'Patata', '<em>200 g</em> · 1 grande', 0.38, 'Patata a granel, 1,90 €/kg'),
  ('boniato', 'Boniato', '<em>250 g</em> · 1 mediano', 0.6, 'Boniato a granel.' + A),
  ('arandano', 'Arándanos', '<em>120 g</em>', 2.2, 'Arándanos, tarrina de 125 g.' + A),
  ('granada', 'Granada', '<em>30 g</em> · si te queda', 1.2, 'Granada suelta o desgranada.' + A),
  ('kiwi', 'Kiwi', '<em>2</em>', 0.7, '2 kiwis verdes sueltos'),
  ('platano', 'Plátano', '<em>2 pequeños</em>', 0.6, 'Plátano de Canarias suelto.' + A),
  ('mandarina', 'Mandarina', '<em>2</em>', 0.5, '2 mandarinas sueltas.' + A),
  ('limon', 'Limón', '<em>1</em>', 0.36, '1 limón'),
 ]),
 ('Carne y pescado', [
  ('pollo', 'Pechuga de pollo', '<em>245 g</em>', 3.2, 'Filetes pechuga de pollo, bandeja de unos 350 g.' + A),
  ('ternera', 'Filetes de ternera', '<em>160 g</em>', 4.5, 'Filetes finos de ternera, bandeja pequeña.' + A),
  ('lomo', 'Lomo de cerdo en filetes', '<em>130 g</em>', 3.5, 'Filetes de lomo de cerdo, bandeja pequeña.' + A),
  ('merluza', 'Merluza', '<em>170 g</em>', 4.5, 'Filetes de merluza Hacendado ultracongelados.' + A),
  ('salmon', 'Salmón', '<em>170 g</em> · 1 lomo grande', 5.95, 'Lomos de salmón sin piel Hacendado congelados, 250 g (2 lomos)'),
  ('dorada', 'Dorada', '<em>1 en lomos</em> · unos 150 g limpios', 4.5, 'Dorada limpia, 1 pieza (que te la abran en lomos).' + A),
  ('calamar', 'Calamar', '<em>160 g</em>', 4.0, 'Anillas o tiras de calamar Hacendado ultracongeladas.' + A),
  ('gambas', 'Gambas o langostinos pelados', '<em>280 g</em>', 4.9, 'Gamba pelada cruda mediana Hacendado ultracongelada, 360 g'),
 ]),
 ('Huevos, charcutería y lácteos', [
  ('huevos', 'Huevos', '<em>5</em>', 1.8, 'Huevos grandes L, media docena'),
  ('york', 'Jamón york', '<em>110 g</em>', 2.0, 'Jamón cocido extra Hacendado finas lonchas, 200 g'),
  ('pavol', 'Pechuga de pavo en lonchas', '<em>60 g</em>', 1.9, 'Pechuga de pavo en finas lonchas Hacendado.' + A),
  ('serrano', 'Jamón serrano', '<em>40 g</em>', 2.5, 'Jamón serrano en lonchas, sobre pequeño.' + A),
  ('queso', 'Queso en lonchas cremoso light Hacendado', '<em>3 lonchas</em>', 2.9, 'Queso lonchas cremoso light Hacendado, 300 g (12 lonchas)'),
  ('mozza', 'Mozzarella light', '<em>80 g</em>', 1.3, 'Mozzarella light Hacendado, 1 bola.' + A),
  ('leched', 'Leche desnatada', '<em>600 ml</em> · para el matcha', 0.81, 'Leche desnatada Hacendado, brick de 1 L'),
  ('almendra', 'Bebida de almendra sin azúcar', '<em>375 ml</em> · para el matcha', 1.1, 'Bebida de almendras 0% azúcar Hacendado, brick de 1 L'),
 ]),
 ('Despensa', [
  ('pan', 'Pan integral', '<em>215 g</em> · unas 5 rebanadas', 0.9, 'Pan de molde 100% integral Hacendado, 460 g'),
  ('panburger', 'Pan de hamburguesa', '<em>1</em>', 1.2, 'Panes de hamburguesa Hacendado.' + A),
  ('pasta', 'Pasta', '<em>70 g</em>', 0.9, 'Macarrones o espaguetis Hacendado, 500 g.' + A),
  ('granola', 'Granola sin azúcar', '<em>65 g</em>', 1.9, 'Muesli Crunchy Hacendado sin azúcares añadidos, 500 g'),
  ('chia', 'Chía', '<em>30 g</em>', 2.05, 'Semillas de chía Hacendado, 250 g'),
  ('almendras', 'Almendras', '<em>20 g</em>', 2.3, 'Almendra natural Hacendado, 200 g'),
  ('nueces', 'Nueces', '<em>6 ud</em> (24 g)', 1.7, 'Nuez troceada pelada Hacendado, 150 g'),
  ('cremaave', 'Crema de avellana y cacao Ametller', '<em>10 g</em> · la que tienes', 0, 'Ya la tienes en casa'),
  ('choco', 'Chocolate negro 72% Mercadona', '<em>12 onzas</em> · 1 tableta', 1.65, 'Chocolate negro 72% cacao Hacendado, tableta de 100 g'),
  ('eneldo', 'Eneldo', '<em>una pizca</em>', 1.2, 'Eneldo seco Hacendado, bote.' + A),
  ('brochetas', 'Palitos de brocheta', '<em>3 o 4</em>', 1.0, 'Palitos de madera para brochetas.' + A),
 ]),
 ('Fuera de Mercadona', [
  ('kouk0', 'Yogur griego Koukakis 0%', '<em>3</em>', 2.97, 'Precio aproximado', True),
  ('kouk10', 'Yogur griego Koukakis', '<em>2</em> · 160 g en total', 1.98, 'Precio aproximado', True),
  ('skyr', 'Skyr natural Danone', '<em>3</em>', 2.75, 'Precio aproximado, pack de 4', True),
 ]),
]
out = {'week': 'WK48', 'title': 'Lista de la compra · WK48 · 23 al 29 nov',
       'note': 'Todo lo del menú WK48 de lunes a domingo, sin matcha ni aceite. Precios de Mercadona (tienda de Madrid); los marcados como aproximados no los he podido comprobar. Marca lo que ya tienes en casa y te queda a la vista lo que falta.',
       'groups': [{'name': n, 'items': [{'id': i[0], 'name': i[1], 'qty': i[2], 'price': i[3], 'out': len(i) > 5 and i[5], 'buy': i[4]} for i in its]} for n, its in G]}
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
json.dump(out, open(os.path.join(root, 'data', 'compra-wk48.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(round(sum(i['price'] for g in out['groups'] for i in g['items']), 2))
