# Cyber Log Monitor - Parser de auth.log

Proyecto para la práctica: parsear un `auth.log` grande (7000 líneas) y preparar los datos para visualización en Power BI.

## Archivos generados
- `auth_7000.log` -> /mnt/data/cyber_log_monitor_files/auth_7000.log
- `logs_resultados_powerbi_7000.csv` -> /mnt/data/cyber_log_monitor_files/logs_resultados_powerbi_7000.csv
- `parse_auth_log.py` -> /mnt/data/cyber_log_monitor_files/parse_auth_log.py
- `requirements.txt` -> /mnt/data/cyber_log_monitor_files/requirements.txt
- `.gitignore` -> /mnt/data/cyber_log_monitor_files/.gitignore

## Uso rápido (Windows - CMD)

1. Coloca los archivos en la carpeta de tu proyecto `Cyber Log Monitor - Parser de auth.log`.
2. (Opcional) Crea y activa un entorno virtual:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```
3. Instala dependencias:
   ```cmd
   pip install -r requirements.txt
   ```
4. Ejecuta el parser (si quieres reprocesar):
   ```cmd
   python parse_auth_log.py
   ```

## Power BI - Power Query (crear Timestamp y asegurar tipos)

1. Obtener datos → Texto/CSV → selecciona `logs_resultados_powerbi_7000.csv` → Transformar datos.
2. Verifica que `Fecha` y `Hora` son Texto.
3. Agrega columna personalizada:
   ```m
   = DateTime.FromText(Text.Trim([Fecha]) & " " & Text.Trim([Hora]))
   ```
   Nombra la columna `Timestamp` y cambia su tipo a **Date/Time**.
4. Asegura tipos: `IP` Texto, `Usuario` Texto, `Puerto` Número entero.
5. (Opcional) Agrega columna `HoraEntera`:
   ```m
   = Date.Hour([Timestamp])
   ```
6. Cerrar y aplicar.

## Visualizaciones (Power BI)
- Gráfico de barras: IP (Axis) vs Count of IP (Values).
- Gráfico de barras: Usuario (Axis) vs Count of Usuario (Values).
- Tarjetas: `TotalIntentos`, `IPsUnicas`, `UsuariosUnicos` (medidas DAX).
- Slicer: arrastra `Timestamp` y configúralo como rango (Between).

## Notas
- Logs simulados. No contienen datos reales.
- Añade `logs/` y `venv/` a `.gitignore` si subes a GitHub.
