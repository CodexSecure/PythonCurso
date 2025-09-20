"""
Cyber Log Monitor - Parser de auth.log
---------------------------------------
Este script procesa un archivo auth.log simulado (1000 líneas de intentos fallidos)
y genera un CSV limpio para usar en Power BI.
"""

import re
import pandas as pd

# Ruta del archivo auth.log
log_file = "auth.log"

# Expresión regular para detectar intentos fallidos en auth.log
pattern = re.compile(
    r"(?P<Mes>\w{3})\s+(?P<Dia>\d{1,2})\s+(?P<Hora>\d{2}:\d{2}:\d{2}) .* Failed password for (?P<Usuario>\w+) from (?P<IP>[\d\.]+) port (?P<Puerto>\d+) ssh2"
)

# Lista para almacenar resultados
data = []

# Leer el archivo línea por línea
with open(log_file, "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            data.append(match.groupdict())

# Convertir a DataFrame
df = pd.DataFrame(data)

# Guardar en CSV para usar en Power BI
df.to_csv("logs_resultados_powerbi.csv", index=False)

print("✅ Archivo exportado: logs_resultados_powerbi.csv")
print("Primeras filas:\n", df.head())
