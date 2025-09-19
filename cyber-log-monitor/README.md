<em> # 🔐 Cyber Log Monitor </em>

Cyber Log Monitor es un proyecto de **ciberseguridad en Python** que analiza intentos de login fallidos en un archivo de logs simulado y muestra resultados tanto en **consola** como en un **dashboard web interactivo** con Streamlit.

Este proyecto está pensado para un **portafolio de desarrollador Python + Ciberseguridad** y es totalmente ejecutable en **Windows**.

---

## 🚀 Funcionalidades

- Detecta intentos fallidos de login en logs simulados.
- Identifica usuarios e IPs sospechosas.
- Muestra reportes en consola.
- Dashboard con gráficos interactivos (Streamlit).

---

## 📂 Estructura

cyber-log-monitor/
│── logs/
│ └── auth.log # archivo de logs simulado
│── main.py # análisis en consola
│── dashboard.py # dashboard con Streamlit
│── requirements.txt # dependencias
│── README.md # documentación

## ⚙️ Instalación y uso (Windows)

### 1. Clonar el repositorio
```powershell
git clone https://github.com/tuusuario/cyber-log-monitor.git
cd cyber-log-monitor
```
### 2. Crear entorno virtual
python -m venv venv
.\venv\Scripts\Activate.ps1

### 3. Instalar dependencias
pip install -r requirements.txt

### 4. Ejecutar análisis en consola
python main.py

### 5. Ejecutar el dashboard web
streamlit run dashboard.py

🛡️ Notas de seguridad

Los logs incluidos son falsos (no datos reales).

No subas registros sensibles de sistemas reales a GitHub.

Este proyecto es educativo y pensado para prácticas de portafolio.
