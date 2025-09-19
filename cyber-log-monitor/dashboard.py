import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="Cyber Log Monitor", page_icon="🔐", layout="wide")

st.title("🔐 Cyber Log Monitor")
st.write("Dashboard de intentos fallidos de login (ejemplo en Windows con archivo simulado).")

# Ruta al archivo de logs (usa el ejemplo en logs/auth.log)
LOG_FILE = "logs/auth.log"

pattern = re.compile(r"Failed password for (invalid user )?(\w+) from ([\d\.]+)")
data = []

try:
    with open(LOG_FILE, "r") as f:
        for line in f:
            match = pattern.search(line)
            if match:
                user = match.group(2)
                ip = match.group(3)
                data.append({"Usuario": user, "IP": ip})
except FileNotFoundError:
    st.error(f"No se encontró el archivo {LOG_FILE}. Asegúrate de que existe en la carpeta logs/")

# Convertir a DataFrame
if data:
    df = pd.DataFrame(data)

    st.subheader("📋 Detalle de intentos fallidos")
    st.dataframe(df)

    st.subheader("📊 Intentos fallidos por IP")
    st.bar_chart(df["IP"].value_counts())

    st.subheader("👤 Intentos fallidos por usuario")
    st.bar_chart(df["Usuario"].value_counts())
else:
    st.warning("No se encontraron intentos fallidos en los logs.")
