# Menú semanal

App del menú de Chloe para la pantalla de inicio del iPhone (GitHub Pages).

- `data/weeks.json`: semanas que salen en las pestañas, en orden (`current` es la que se abre).
- `data/wkNN.json`: un archivo por semana. Cada día tiene `meals` (con el HTML de cada comida, igual que en el menú de Claude) y `total`.
- `data/compra-wkNN.json`: lista de la compra de esa semana (botón del carrito). Grupos con productos: `id`, `name`, `qty` (HTML corto), `price` (envase entero en Mercadona), `out` (true si se compra fuera de Mercadona) y `buy`. Nunca matcha ni aceite de oliva. Las marcas se guardan en el móvil.
- Los cambios se piden desde la app: abren una issue en este repositorio con el día y el mensaje. La acción `.github/workflows/cambios-menu.yml` lanza Claude al momento, que sigue `CLAUDE.md`, cambia el JSON, sube el cambio y cierra la issue con un resumen. La app se actualiza sola al cerrarse la issue.
- La acción necesita el secreto `CLAUDE_CODE_OAUTH_TOKEN` (se saca con `claude setup-token`).
- La app lee los JSON sin caché, así que un cambio de datos no necesita subir `version.txt`. Solo hay que subirlo (y `VERSION` en `index.html`) si cambia el propio `index.html`.
