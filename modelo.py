from flask import Flask, request
import sqlite3
DB_NAME ="notas.db"

app = Flask(__name__)

def crear_tabla():
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS notas(
            codigo CHAR(40) PRIMARY KEY,
            texto TEXT NOT NULL)
       """)
    con.commit()
    con.close()
    
def leer_nota(codigo):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("""
        SELECT codigo, texto FROM notas
        WHERE codigo = ?
    """, (codigo,))
    con.commit()
    con.close
    result = cur.fetchone() #result contiene codigo y texto
    con.close()
    if result:
        codigo,texto =result
        return codigo, texto
    else:
        return None

def guardar_nota(codigo, texto):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("""
        INSERT INTO notas (codigo, texto)
        VALUES(?,?)
        """, (codigo,texto))
    con.commit()
    con.close()

def borrar_nota(codigo):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    cur.execute("""
        DELETE FROM notas 
        WHERE codigo = ?
        """, (codigo))
    con.commit()
    con.close()
