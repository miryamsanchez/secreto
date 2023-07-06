from flask import Flask, request,render_template
from modelo import crear_tabla, leer_nota, guardar_nota, borrar_nota
import secrets
BASE_URL = "http://localhost:5000" # Ruta de ejecución para el ejercicio

app = Flask(__name__)#__name__ es una variable especial de Python

@app.route("/", methods=["GET", "POST"])#@route() es un decorador que asigna una url a una función
def crear_nota():
    if request.method == "GET":
        return render_template("crearnota.html")
    elif request.method == "POST":
        nota = request.form.get("nota")
        codigo = secrets.token_urlsafe(8)#Genera un token seguro
        guardar_nota(codigo,nota)
        enlace = BASE_URL + "/nota/" +codigo
        return  render_template("enlace.html", enlace=enlace)

@app.route("/nota/<codigo>", methods=["GET"])
def guardar_nota(codigo):
    nota = leer_nota(codigo)
    return request.get(BASE_URL + "/nota/" + codigo).text

@app.errorhandler(404)
def pagina_no_encontrada():
    return render_template("404.html"), 404

if __name__ == "__main__":
    crear_tabla()
    app.run()  
