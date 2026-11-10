# Cómo aplicar un cambio del menú

Chloe pide cambios desde la app; cada petición llega como una issue con el día y la semana. Para aplicarla:

1. Abre `data/<semana en minúsculas>.json` (por ejemplo `data/wk44.json`) y busca el día en `days` por `name` y `date`.
2. Cambia solo lo que pide, manteniendo exactamente la misma estructura HTML de cada comida:
   `<p class="dish">…</p><ul><li><span>Alimento</span><span class="q">cantidad</span></li>…</ul><div class="mac"><span><b>HC</b> HC netos</span><span><b>P</b> P</span><span><b>G</b> G</span><span><b>Fib</b> Fib</span><span><b>kcal</b> kcal</span></div>`
3. Si cambia o añade un alimento de una comida que aún no ha comido, ajusta los demás alimentos de esa misma comida (cantidades, o cambiar uno por otro que le guste) para que la comida mantenga más o menos sus macros. Si dice que ya lo ha comido (o "he comido más de…"), deja lo que comió tal cual y reajusta las comidas que quedan de ese día, si quedan.
4. Recalcula los macros de cada comida tocada y el `total` del día (mismo HTML que ya tiene). Calorías = 4 × (HC netos + P) + 9 × G + 2 × Fib. Cada comida lleva también sus calorías totales (el último span, "kcal"), calculadas con la misma fórmula a partir de los macros de esa comida; nunca calorías por alimento. El día lleva su total como siempre.
5. Añade " (tomado)" al final del plato si dice que ya lo ha comido.
6. Comprueba que el JSON es válido, haz commit en `main` con un mensaje corto en español y push.
7. Comenta en la issue 2 o 3 líneas en español: qué has cambiado y los totales nuevos del día. Cierra la issue.
8. Chloe escribe mensajes cortos desde el móvil. Aplica siempre la lectura más probable (por ejemplo "Arándanos 30gr" = cambia la cantidad de arándanos de ese día a 30 g; si no hay arándanos ese día, añádelos a la merienda) y explica en el comentario lo que has entendido. Nunca dejes una issue abierta: ella no lee las preguntas y la app se queda esperando.
9. Chloe no lee los comentarios de una issue cerrada, así que no preguntes "si quieres lo compenso": si al final la fibra queda fuera de 25 a 32 g o algún macro se pasa del objetivo, reajusta tú las comidas que aún no ha comido ese día y dilo en el comentario. La primera línea del comentario es la que ve en la app: que sea un resumen corto y claro.

10. Nunca cambies cantidades de una comida que ya ha comido (marcada "(tomado)" o que ella ha descrito como lo que ha comido "hoy"). Si añade algo a esa comida, súmalo y reajusta solo las comidas que quedan.

11. Las comidas y cenas tienen `recipe`: una lista de 3 o 4 pasos cortos con tiempos y temperaturas (tiene sartén, horno y airfryer). Si cambias el plato o un ingrediente principal de una comida o cena, reescribe también su `recipe`. Si solo cambian cantidades, déjala.

## Reglas

- Hidratos siempre netos (sin fibra).
- Cuando dice lo que ha comido, el arroz, la pasta y las patatas son pesos en cocido salvo que diga "crudo" (en el menú planificado van en crudo).
- Objetivos (el día queda unos 5 g por debajo de cada uno en HC, P y G cuando reajustas; fibra entre 25 y 32 g):
  - Macros regulares: 138 HC netos, 103 P, 46 G, 25 Fib.
  - Carbs reducidos: 50 HC netos, 103 P, 85 G, 25 Fib.
  - Día de fiesta: 173 HC netos, 129 P, 58 G, 25 Fib.
- Nunca cambies el tipo de día (la etiqueta `chip`).
- Una onza de chocolate negro 72% de 8 g después de comer y de cenar (3,4 G, 2,6 HC netos, 0,9 Fib, 0,8 P). Excepción: de lunes 2 a viernes 6 de noviembre (WK45) nada con azúcar añadido, así que sin chocolate ni fiambres esos días.
- Verduras: solo judías verdes, calabacín, brócoli, edamame, alcachofas, setas y champiñones.
- No le gustan: cuscús, quinoa, bulgur, pan de centeno, garbanzos, alubias, guisantes, hummus, uvas, sandía, higos, dátiles, cecina, sardinas, caballa, boquerones, mejillones, queso fresco, tofu, tempeh, soja texturizada, ghee, lino, feta, quesos fuertes, espinacas, zanahoria, aceitunas, caqui, aguacate en el desayuno, claras de huevo.
- Sus productos (por 100 g): yogur griego LIGHT Mercadona (Hacendado), 125 g (4,7 HC / 5,8 P / 2 G); es el que tiene, no el normal; Koukakis griego 150 g (3,8 / 6,2 / 10); Koukakis 0% 150 g (4 / 7,9 / 0); Skyr Danone 100 g (3,4 / 9 / 0,1); queso en lonchas light Hacendado, loncha de 25 g (1,6 / 27 / 17).
- Huevo nunca a la plancha ni frito: siempre revuelto, tortilla u omelette.
- La comida es siempre la comida más grande del día (más calorías y más cantidad que la merienda). La merienda es un snack ligero (unas 150–250 kcal) y la cena, más ligera que la comida.
- Desayunos salados y ligeros (nunca yogur, skyr ni fruta en el desayuno), meriendas dulces.
- Nunca repitas el mismo alimento en dos comidas del mismo día (por ejemplo brócoli en la comida y en la cena). El aceite, la leche del matcha y la onza de chocolate no cuentan.
- Cenas sin hidratos: nada de arroz, pasta, pan, patata, boniato, legumbres ni fruta en la cena. Solo proteína, verduras de su lista y grasa. Los hidratos van en la comida (y la merienda).
- Una sola fuente de hidratos por comida (nunca pasta con boniato, arroz con patata…). Los platos tienen que tener sentido, como una receta normal; si dudas, inspírate en recetas reales.
- Raciones realistas, como las serviría una persona normal: verdura 100–200 g por alimento y como mucho unos 300 g de verdura en total por comida; nada de cantidades ridículas de algo que haya que cocinar (por ejemplo 30 g de boniato: o una ración normal, 100–150 g, o nada). Legumbre seca 60–90 g, arroz o pasta en crudo 60–90 g, patata 150–250 g, carne o pescado 100–170 g, chía 10–15 g, arándanos 40 g como máximo, yogur o skyr 150 g como máximo. Los ñoquis (Hacendado: 37,6 HC / 4,5 P / 0,4 G por 100 g) se dan en unidades: 23 ñoquis = 150 g. Repasa siempre las cantidades antes de guardar. Las raciones realistas van antes que la fibra: nunca subas la verdura ni añadas otra para llegar a 25 g de fibra; si al quitar algo baja la fibra, se queda baja (como mucho cambia una fruta o un alimento por otro similar con más fibra en una comida que no haya comido).
- Una sola verdura por comida o cena (nunca dos tipos de verdura en el mismo plato: no quiere cocinar dos), en ración normal de 150–200 g.
- Almendras solo en la merienda (como snack), nunca en la comida ni en la cena.
- Nada de sésamo ni semillas añadidas a un plato solo para cuadrar la grasa; si falta grasa, usa aguacate, más cantidad de pescado azul o un yogur más graso. No pongas notas como "(cena temprana)" en el nombre del plato.
- Todas las comidas y cenas en casa llevan siempre 1 cucharadita de aceite de oliva (ni más ni menos), escrita "1 cucharadita", nunca en g o ml.
- Recetas sencillas, de 15 minutos como mucho. Nada al ajillo (ni ajo laminado ni platos "al ajillo").
- No toques `index.html` ni `version.txt`.
