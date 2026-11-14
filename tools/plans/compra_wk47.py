"""Lista de la compra WK47 -> data/compra-wk47.json (ids estables, sin matcha ni aceite)."""
import json, os
A = ' Precio aproximado (no lo he comprobado en la web de Mercadona)'
L = ' Para el lunes: cómpralo el sábado.'
G = [
 ('Fruta y verdura', [
  ('judias', 'Judías verdes', '<em>450 g</em>', 1.3, 'Judía verde redonda Hacendado ultracongelada, bolsa de 1 kg.' + L),
  ('champi', 'Champiñones', '<em>150 g</em>', 1.56, 'Champiñones blancos, bandeja de 300 g.' + L),
  ('brocoli', 'Brócoli', '<em>450 g</em> · 2 pequeños', 1.05, 'Brócoli a granel, 2,30 €/kg'),
  ('calabacin', 'Calabacín', '<em>300 g</em> · unos 2', 0.45, 'Calabacín verde a granel, 1,40 €/kg'),
  ('setas', 'Setas', '<em>150 g</em>', 2.2, 'Setas de cardo u ostra, bandeja.' + A),
  ('fresa', 'Fresas', '<em>150 g</em>', 2.5, 'Fresas, tarrina de 500 g.' + A),
  ('frambuesa', 'Frambuesas', '<em>100 g</em>', 3.16, 'Frambuesas, bandeja de 200 g'),
  ('arandano', 'Arándanos', '<em>40 g</em>', 2.2, 'Arándanos, tarrina de 125 g.' + A),
  ('kiwi', 'Kiwi', '<em>2</em>', 0.7, '2 kiwis verdes sueltos (1 es para el lunes)'),
  ('mandarina', 'Mandarina', '<em>2</em> · 140 g', 0.5, '2 mandarinas sueltas.' + A),
  ('platano', 'Plátano', '<em>1</em>', 0.3, 'Plátano de Canarias suelto.' + A),
  ('limon', 'Limón', '<em>1</em>', 0.36, '1 limón'),
 ]),
 ('Carne y pescado', [
  ('pollo', 'Pechuga de pollo', '<em>450 g</em>', 4.5, 'Filetes pechuga de pollo, bandeja de unos 520 g (150 g son para el lunes: cómprala el sábado)'),
  ('pavof', 'Filete de pechuga de pavo', '<em>120 g</em>', 2.5, 'Filetes pechuga de pavo, bandeja pequeña.' + A),
  ('picada', 'Carne picada de ternera 5% grasa', '<em>150 g</em>', 2.5, 'Burger meat o picada de vacuno 5% grasa Hacendado.' + A),
  ('lubina', 'Lubina', '<em>1 en lomos</em> · unos 150 g limpios', 0, 'La que te sobró de esta semana (congelada); si no, 1 lubina limpia'),
  ('dorada', 'Dorada', '<em>1 en lomos</em> · unos 150 g limpios', 4.5, 'Dorada limpia, 1 pieza (que te la abran en lomos).' + A),
  ('salmon', 'Salmón', '<em>130 g</em> · 1 lomo', 5.95, 'Lomos de salmón sin piel Hacendado congelados, 250 g (2 lomos)'),
  ('gambas', 'Gambas peladas', '<em>160 g</em>', 4.9, 'Gamba pelada cruda mediana Hacendado ultracongelada, 360 g'),
 ]),
 ('Huevos, charcutería y lácteos', [
  ('huevos', 'Huevos', '<em>4</em>', 1.8, 'Huevos grandes L, media docena (2 son para el lunes)'),
  ('york', 'Jamón york', '<em>150 g</em>', 2.0, 'Jamón cocido extra Hacendado finas lonchas, 200 g'),
  ('pavol', 'Pechuga de pavo en lonchas', '<em>30 g</em>', 1.9, 'Pechuga de pavo en finas lonchas Hacendado.' + A),
  ('queso', 'Queso en lonchas cremoso light Hacendado', '<em>1½ lonchas</em>', 2.9, 'Queso lonchas cremoso light Hacendado (si no te queda)'),
  ('leched', 'Leche desnatada', '<em>750 ml</em> · para el matcha', 0.81, 'Leche desnatada Hacendado, brick de 1 L'),
  ('almendra', 'Bebida de almendra sin azúcar', '<em>300 ml</em> · para el matcha', 1.1, 'Bebida de almendras 0% azúcar Hacendado, brick de 1 L'),
 ]),
 ('Despensa', [
  ('pan', 'Pan integral', '<em>210 g</em> · unas 6 rebanadas', 0.9, 'Pan de molde 100% integral Hacendado, 460 g'),
  ('arroz', 'Arroz blanco', '<em>75 g</em>', 1.2, 'Arroz largo Hacendado, 1 kg (si no te queda)'),
  ('fideos', 'Fideos', '<em>65 g</em>', 0.6, 'Fideos finos Hacendado, 500 g.' + A),
  ('caldo', 'Caldo de pollo', '<em>350 ml</em>', 1.1, 'Caldo de pollo Hacendado, brick de 1 L.' + A),
  ('granola', 'Granola sin azúcar', '<em>15 g</em>', 1.9, 'Muesli Crunchy Hacendado sin azúcares añadidos (si no te queda)'),
  ('cremaave', 'Crema de avellana y cacao Ametller', '<em>10 g</em> · la que tienes', 0, 'Ya la tienes en casa'),
  ('choco', 'Chocolate negro 72%', '<em>9 onzas</em>', 1.6, 'Chocolate negro 72% Hacendado, tableta (si no te queda)'),
 ]),
 ('Fuera de Mercadona', [
  ('kouk10', 'Yogur griego Koukakis', '<em>2</em>', 1.1, 'Koukakis griego natural 150 g.' + A, True),
  ('skyr', 'Skyr natural Danone', '<em>5</em>', 2.75, 'Precio aproximado, pack de 4 (1 es para el lunes)', True),
 ]),
]
out = {'week': 'WK47', 'title': 'Lista de la compra · WK47 · 16 al 22 nov',
       'note': 'Todo lo del menú WK47 de lunes a domingo, sin matcha ni aceite. Lo del lunes cómpralo el sábado. Precios de Mercadona (tienda de Madrid); los marcados como aproximados no los he podido comprobar.',
       'groups': [{'name': n, 'items': [{'id': i[0], 'name': i[1], 'qty': i[2], 'price': i[3], 'out': len(i) > 5 and i[5], 'buy': i[4]} for i in its]} for n, its in G]}
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
json.dump(out, open(os.path.join(root, 'data', 'compra-wk47.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(round(sum(i['price'] for g in out['groups'] for i in g['items']), 2))
