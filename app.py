from flask import Flask, request,render_template
from modelo import crear_tabla, leer_nota, guardar_nota, borrar_nota
import secrets
BASE_URL = "http://localhost:5000" # Ruta de ejecución para el ejercicio

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def crear_nota():
    if request.method == "GET":
        return render_template("crearnota.html")
    elif request.method == "POST":
        nota = request.data.decode("utf-8")
        codigo = secrets.token_urlsafe(8)
        guardar_nota(codigo,nota)
        return "Nota agregada correctamente."

@app.route("/nota/<codigo>", methods=["GET"])
def guardar_nota(codigo):
    return request.get(BASE_URL + "/nota/" + codigo).text

if __name__ == "__main__":
    crear_tabla()
    app.run()  

@app.errorhandler(404)
def pagina_no_encontrada():
    return render_template("404.html") 

