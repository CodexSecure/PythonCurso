
# parse_auth_log.py
# Script que parsea un archivo auth.log y genera logs_resultados_powerbi_7000.csv (listo para Power BI).
# Comentarios en cada línea explican qué hace el script.

import re  # re: expresiones regulares para parsear líneas
import pandas as pd  # pandas: manejo de tablas (DataFrame)
from datetime import datetime  # datetime: manejo de fechas y horas
import os  # os: operaciones del sistema (comprobar archivos)

# Definición de posibles rutas del auth.log (primero busca 'logs/auth.log', luego 'auth.log').
LOG_PATHS = ["logs/auth.log", "auth.log", "auth_7000.log"]  # rutas candidatas

# Función para devolver la primera ruta existente del log o None si no existe.
def encontrar_log():
    for p in LOG_PATHS:  # iteramos las rutas
        if os.path.isfile(p):  # si el archivo existe
            return p  # devolvemos la ruta
    return None  # si no existe ninguno devolvemos None

# Localizamos el archivo usando la función anterior.
log_file = encontrar_log()  # ruta encontrada o None

# Si no encontramos el archivo, mostramos mensaje y salimos del programa.
if not log_file:  # comprobación de existencia
    print("❌ No se encontró 'logs/auth.log' ni 'auth.log' ni 'auth_7000.log'. Coloca el archivo en la carpeta 'logs/' o en la raíz del proyecto.")
    raise SystemExit(1)  # finalizamos la ejecución

# Expresión regular para capturar líneas tipo auth.log de sshd.
pattern = re.compile(
    r"(?P<Mes>\w{3})\s+(?P<Dia>\d{1,2})\s+(?P<Hora>\d{2}:\d{2}:\d{2}).*"
    r"Failed password for (?:invalid user )?(?P<Usuario>[\w\.\-]+) from (?P<IP>[\d\.]+) port (?P<Puerto>\d+)",
    re.IGNORECASE
)

# Mapa para convertir meses abreviados (inglés) a número de mes.
MES_MAP = {
    "Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,
    "Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12
}

# Lista donde almacenaremos las filas parseadas como diccionarios.
rows = []  # lista vacía para almacenar resultados

# Abrimos el archivo de logs en modo lectura; usamos encoding utf-8 e ignoramos errores de encoding.
with open(log_file, "r", encoding="utf-8", errors="ignore") as f:  # abrir archivo
    # Recorremos línea a línea
    for line in f:  # iterar líneas
        # Aplicamos la regex a la línea actual
        m = pattern.search(line)  # buscar coincidencia
        # Si no hay coincidencia, saltamos a la siguiente línea
        if not m:  # sin match
            continue  # continuar bucle

        # Extraemos campos desde la regex
        mes = m.group("Mes")               # mes abreviado, p.ej. 'Sep'
        dia = int(m.group("Dia"))          # día como entero
        hora_str = m.group("Hora")         # hora como 'HH:MM:SS'
        usuario = m.group("Usuario")       # usuario extraído
        ip = m.group("IP")                 # dirección IP extraída
        puerto = int(m.group("Puerto"))    # puerto convertido a entero
        resultado = "Failed"               # resultado fijo (en este ejercicio son fallos)

        # Intentamos construir una fecha completa (añadiendo el año actual)
        try:  # bloque try para manejar errores en fecha/hora
            # Normalizamos el nombre del mes con capital inicial y buscamos su número
            month = MES_MAP.get(mes.capitalize(), None)  # número de mes
            # Convertimos la hora a horas, minutos y segundos
            h,mi,s = map(int, hora_str.split(":"))  # parseo hora
            # Tomamos el año actual (si necesitas otro, cámbialo aquí)
            year = datetime.now().year  # año actual
            # Construimos el objeto datetime completo
            dt = datetime(year, month, dia, h, mi, s)  # datetime completo
            # Formateamos fecha e hora a ISO para Power BI ('YYYY-MM-DD', 'HH:MM:SS')
            fecha_iso = dt.date().isoformat()  # 'YYYY-MM-DD'
            hora_iso = dt.time().isoformat()   # 'HH:MM:SS'
            timestamp = dt.isoformat(sep=" ")  # 'YYYY-MM-DD HH:MM:SS'
        except Exception:  # si ocurre error con la fecha, guardamos strings crudos
            fecha_iso = f"{mes} {dia}"  # fecha cruda
            hora_iso = hora_str         # hora cruda
            timestamp = f"{mes} {dia} {hora_str}"  # timestamp crudo

        # Añadimos la fila a la lista de resultados como diccionario
        rows.append({  # añadir fila
            "Fecha": fecha_iso,       # fecha en formato ISO o 'Mes Dia' si falló
            "Hora": hora_iso,         # hora en formato HH:MM:SS
            "Timestamp": timestamp,   # timestamp
            "Usuario": usuario,       # usuario atacado
            "IP": ip,                 # IP origen del intento
            "Puerto": puerto,         # puerto origen
            "Resultado": resultado    # resultado (Failed)
        })  # fin append

# Convertir la lista de diccionarios a un DataFrame de pandas con columnas ordenadas.
df = pd.DataFrame(rows, columns=["Fecha","Hora","Timestamp","Usuario","IP","Puerto","Resultado"])  # DataFrame

# Nombre del archivo CSV de salida que importaremos en Power BI
out_csv = "logs_resultados_powerbi_7000.csv"  # nombre fichero salida

# Guardamos el DataFrame como CSV con encoding utf-8-sig para compatibilidad con Excel/Power BI.
df.to_csv(out_csv, index=False, encoding="utf-8-sig")  # exportar CSV

# Mostramos un resumen en consola: número de filas procesadas y top IPs/usuarios.
print(f"✅ Procesado: {len(df)} filas. CSV generado -> {out_csv}")  # resumen general
if not df.empty:  # si hay datos
    # Mostramos las 10 IPs con más intentos
    print('\nTop 10 IPs (más intentos):')  # cabecera
    print(df['IP'].value_counts().head(10))  # conteo IPs
    # Mostramos los 10 usuarios más atacados
    print('\nTop 10 Usuarios (más atacados):')  # cabecera
    print(df['Usuario'].value_counts().head(10))  # conteo usuarios
