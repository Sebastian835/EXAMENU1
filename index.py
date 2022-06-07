from flask import Flask, render_template, request, redirect, url_for


# Inicializar la aplicacion
app = Flask(__name__, template_folder='templates')


# Ruta principal 
@app.route('/')
def home():
    return render_template('home.html')

    