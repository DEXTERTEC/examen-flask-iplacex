from flask import Flask, render_template, request

app = Flask(__name__)

PRECIO_TARRO = 9000

USUARIOS = {
    "juan": {"password": "admin", "rol": "Administrador"},
    "pepe": {"password": "user", "rol": "Usuario"},
}


def calcular_compra(edad, cantidad):
    total_sin_descuento = cantidad * PRECIO_TARRO

    if edad >= 18 and edad <= 30:
        porcentaje_descuento = 0.15
    elif edad > 30:
        porcentaje_descuento = 0.25
    else:
        porcentaje_descuento = 0.0

    descuento = total_sin_descuento * porcentaje_descuento
    total_a_pagar = total_sin_descuento - descuento
    return total_sin_descuento, descuento, total_a_pagar


def verificar_login(nombre, password):
    if nombre in USUARIOS and USUARIOS[nombre]["password"] == password:
        rol = USUARIOS[nombre]["rol"]
        return f"Bienvenido {rol} {nombre}"
    return "Usuario o contraseña incorrectos"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad = int(request.form["cantidad"])
        total_sin_descuento, descuento, total_a_pagar = calcular_compra(edad, cantidad)
        resultado = {
            "nombre": nombre,
            "total_sin_descuento": total_sin_descuento,
            "descuento": descuento,
            "total_a_pagar": total_a_pagar,
        }
    return render_template("ejercicio1.html", resultado=resultado)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None
    if request.method == "POST":
        nombre = request.form["nombre"]
        password = request.form["password"]
        mensaje = verificar_login(nombre, password)
    return render_template("ejercicio2.html", mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)