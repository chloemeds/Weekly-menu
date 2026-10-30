# Menú semanal

App del menú de Chloe para la pantalla de inicio del iPhone (GitHub Pages).

- `data/weeks.json`: semanas que salen en las pestañas (`current` es la que se abre).
- `data/wkNN.json`: un archivo por semana. Cada día tiene `meals` (con el HTML de cada comida, igual que en el menú de Claude) y `total`.
- Los cambios se piden desde la app: abren una issue en este repositorio con el día y el mensaje. Una tarea programada de Claude las lee cada hora, cambia el JSON, sube el cambio y cierra la issue con un resumen.
- La app lee los JSON sin caché, así que un cambio de datos no necesita subir `version.txt`. Solo hay que subirlo (y `VERSION` en `index.html`) si cambia el propio `index.html`.
