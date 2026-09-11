from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():

    nombre = None
    total_sin_descuento = None
    descuento = None
    total_a_pagar = None

    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        
        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro
        
        # descuentos
        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25
        else:
            descuento = 0
            
        total_a_pagar = total_sin_descuento - descuento

    return render_template('ejercicio1.html', 
                           nombre=nombre, 
                           total_sin_descuento=total_sin_descuento, 
                           descuento=descuento, 
                           total_a_pagar=total_a_pagar)

#Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    
    if request.method == 'POST':
        usuario = request.form['nombre']
        contrasena = request.form['contrasena']
        
        if usuario == 'juan' and contrasena == 'admin':
            mensaje = "Bienvenido Administrador juan"
        elif usuario == 'pepe' and contrasena == 'user':
            mensaje = "Bienvenido Usuario pepe"
        else:
            mensaje = "Usuario o contraseña incorrectos"
            
    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)