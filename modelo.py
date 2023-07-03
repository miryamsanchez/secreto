from flask import Flask, request
import sqlite3
DB_NAME ="notas.db"

app = Flask(__name__)

def crear_tabla():
    con = sqlite3.connect(DB_NAME)
    cur = con. cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notas(
            codigo CHAR(40) PRIMARY KEY,
            texto TEXT);
        
       """)
    con.close()
    
def get_nota(codigo):
    pass
def guardar_nota(codigo, texto):
    pass
def borrar_nota(codigo):
    pass

class Mensaje:
    def __init__(self):
        self.notas = {}

    def crear_nota(self, codigo, nota):
        self.notas[codigo] = nota

    def leer_nota(self, codigo):
        if codigo in self.notas:
            nota_leida = self.notas[codigo]
            del self.notas[codigo]
            return nota_leida
        else:
            return "No se encontró la nota con el código especificado."

mensaje = Mensaje()

@app.route("/nota", methods=["POST"])
def crear_nota():
    codigo = request.headers.get("X-Codigo")
    nota = request.data.decode("utf-8")
    mensaje.crear_nota(codigo, nota)
    return "Nota creada correctamente."

@app.route("/nota", methods=["GET"])
def leer_ultima_nota():
    codigo = list(mensaje.notas.keys())[-1]
    nota = mensaje.leer_nota(codigo)
    return "Nota leída: " + nota

@app.route("/nota/<codigo>", methods=["GET"])
def leer_nota(codigo):
    nota = mensaje.leer_nota(codigo)
    return "Nota leída: " + nota

if __name__ == "__main__":
    app.run(port=5001)
