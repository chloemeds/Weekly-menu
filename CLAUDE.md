# Cómo aplicar un cambio del menú

Chloe pide cambios desde la app; cada petición llega como una issue con el día y la semana. Para aplicarla:

1. Abre `data/<semana en minúsculas>.json` (por ejemplo `data/wk44.json`) y busca el día en `days` por `name` y `date`.
2. Cambia solo lo que pide, manteniendo exactamente la misma estructura HTML de cada comida:
   `<p class="dish">…</p><ul><li><span>Alimento</span><span class="q">cantidad</span></li>…</ul><div class="mac"><span><b>HC</b> HC netos</span><span><b>P</b> P</span><span><b>G</b> G</span><span><b>Fib</b> Fib</span></div>`
3. Si cambia o añade un alimento de una comida que aún no ha comido, ajusta los demás alimentos de esa misma comida (cantidades, o cambiar uno por otro que le guste) para que la comida mantenga más o menos sus macros. Si dice que ya lo ha comido (o "he comido más de…"), deja lo que comió tal cual y reajusta las comidas que quedan de ese día, si quedan.
4. Recalcula los macros de cada comida tocada y el `total` del día (mismo HTML que ya tiene). Calorías = 4 × (HC netos + P) + 9 × G + 2 × Fib. Las calorías solo van en el total del día.
5. Añade " (tomado)" al final del plato si dice que ya lo ha comido.
6. Comprueba que el JSON es válido, haz commit en `main` con un mensaje corto en español y push.
7. Comenta en la issue 2 o 3 líneas en español: qué has cambiado y los totales nuevos del día. Cierra la issue.
8. Si la petición no se entiende, comenta preguntando y deja la issue abierta sin tocar nada.

## Reglas

- Hidratos siempre netos (sin fibra).
- Objetivos (el día queda unos 5 g por debajo de cada uno en HC, P y G cuando reajustas; fibra entre 25 y 32 g):
  - Macros regulares: 138 HC netos, 103 P, 46 G, 25 Fib.
  - Carbs reducidos: 50 HC netos, 103 P, 85 G, 25 Fib.
  - Día de fiesta: 173 HC netos, 129 P, 58 G, 25 Fib.
- Nunca cambies el tipo de día (la etiqueta `chip`).
- Una onza de chocolate negro 72% de 8 g después de comer y de cenar (3,4 G, 2,6 HC netos, 0,9 Fib, 0,8 P).
- Verduras: solo judías verdes, calabacín, brócoli, edamame, alcachofas, setas y champiñones.
- No le gustan: cuscús, quinoa, bulgur, pan de centeno, garbanzos, alubias, guisantes, hummus, uvas, sandía, higos, dátiles, cecina, sardinas, caballa, boquerones, mejillones, queso fresco, tofu, tempeh, soja texturizada, ghee, lino, feta, quesos fuertes, espinacas, zanahoria, aceitunas, caqui, aguacate en el desayuno.
- Sus productos (por 100 g): yogur griego Mercadona 125 g (3,9 HC / 3,9 P / 10,8 G); Koukakis griego 150 g (3,8 / 6,2 / 10); Koukakis 0% 150 g (4 / 7,9 / 0); Skyr Danone 100 g (3,4 / 9 / 0,1); queso en lonchas light Hacendado, loncha de 25 g (1,6 / 27 / 17).
- Recetas sencillas, de 15 minutos como mucho.
- No toques `index.html` ni `version.txt`.
