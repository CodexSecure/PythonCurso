from flask import Flask, request

# Ejemplo de peticion
# http://127.0.0.1:5000/patata?color=rojo&cantidad=12&tamanyo=grande

app = Flask(__name__)
contador = 0


@app.route("/")
def helloworld():
    global contador
    contador += 1

    return f"Hello World! numero de visitas: {contador}"

@app.route("/patata")
def hello_poteito():
    def sanitize(arg):
        cantidad = 0
        try:
            cantidad = int(request.args.get(arg))
        except TypeError:
            pass
        except ValueError:
            pass

        return cantidad

    respuesta = f"Hello POTEIGOO! Nº {contador}"

    cantidad = sanitize('cantidad')
    tamanyo = request.args.get('tamanyo', '')
    tamanyo_invertido = tamanyo[::-1]
    respuesta += f"<p>Tamaño al revés: {tamanyo_invertido}</p>"

    respuesta += f"cantidad: {cantidad}"
    respuesta += "<ul>"
    for i in range(cantidad):
        respuesta += f"<li>{i}</li>"
    respuesta += "</ul>"

    return respuesta

@app.route("/html")
def hello_html():
    return """
    <html>
        <head>
            <title>Mi pagina</title>
        </head>
        <body>
            <h1>Hola mundo</h1>
            <p>Esto es un parrafo</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
