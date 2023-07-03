from flask import Flask, request,render_template


app = Flask(__name__)
modelo_url = "http://localhost:5001"

@app.route("/", methods=["GET", "POST"])
def handle_root():
    if request.method == "GET":
        return render_template("crearnota.html")
    elif request.method == "POST":
        nota = request.data.decode("utf-8")
        request.post(modelo_url + "/nota", data=nota)
        return "Nota agregada correctamente."

@app.route("/<codigo>", methods=["GET"])
def handle_codigo(codigo):
    return request.get(modelo_url + "/nota/" + codigo).text

if __name__ == "__main__":
    app.run()

