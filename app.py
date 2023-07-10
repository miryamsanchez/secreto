from flask import Flask, request,render_template
from modelo import crear_tabla, leer_nota, guardar_nota
from qrcode import make as make_qrcode
import secrets
BASE_URL = "http://localhost:5000" # Ruta de ejecución para el ejercicio

app = Flask(__name__)#__name__ es una variable especial de Python

def generar_codigo_qr(contenido):
    qr=make_qrcode(contenido)
    qr_image_path= f"static/qrcode.png"
    qr.save(qr_image_path)
    return qr_image_path


@app.route("/", methods=["GET", "POST"])#@route() es un decorador que asigna una url a una función
def crear_nota():
    if request.method == "GET":
        return render_template("crearnota.html")
    elif request.method == "POST":
        nota = request.form.get("nota")#Obtener el texto de la nota desde el formulario. 
        codigo = secrets.token_urlsafe(8)#Genera un token seguro
        guardar_nota(codigo,nota)
        enlace = BASE_URL + "/nota/" +codigo#Construir el enlace a la nota utilizando el código y renderizar la plantilla 'enlace.html'
        qr_image_path = generar_codigo_qr(enlace)
        return  render_template("enlace.html", enlace=enlace, qr_image_path = qr_image_path)


@app.route("/nota/<codigo>", methods=["GET"])
def g_nota(codigo):
    codigo,text = leer_nota(codigo)
    return render_template("leernota.html", text=text)



@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    crear_tabla()
    app.run()  
