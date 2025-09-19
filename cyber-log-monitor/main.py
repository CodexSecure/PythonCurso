import re
from collections import Counter

# Ruta al archivo de logs de ejemplo (Windows)
LOG_FILE = "logs/auth.log"

# Regex para detectar intentos fallidos de login (estilo Linux/SSH)
pattern = re.compile(r"Failed password for (invalid user )?(\w+) from ([\d\.]+)")

failed_attempts = []

try:
    with open(LOG_FILE, "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                user = match.group(2)
                ip = match.group(3)
                failed_attempts.append((user, ip))
except FileNotFoundError:
    print(f"❌ No se encontró el archivo {LOG_FILE}. Asegúrate de que existe.")

# Contar intentos por IP
counter = Counter([ip for _, ip in failed_attempts])

print("🚨 Intentos fallidos por IP:")
for ip, count in counter.most_common():
    print(f"{ip} → {count} intentos")

print("\n📋 Detalle de intentos fallidos:")
for user, ip in failed_attempts:
    print(f"Usuario: {user} | IP: {ip}")
