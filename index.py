from flask import Flask, render_template, request, redirect, url_for


# Inicializar la aplicacion
app = Flask(__name__, template_folder='templates')

datosUsuario = []

# Ruta principal 
@app.route('/' , methods=['GET','POST'])
def home():
    if(request.method == "POST"):
        placa = request.form['placa']
        fecha = request.form['fecha']
        hora = request.form['hora'] 

        if(placa == "" or fecha  == "" or hora == ""):
            return redirect(url_for('home'))
        else:
            datosUsuario.append(placa, fecha, hora )
            print(datosUsuario)
            return redirect(url_for('home'))

    return render_template('home.html')


# Ejecutar la aplicacion
if __name__ == '__main__':
    app.run(debug=True)