from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def inicio():
    return render_template('index.html')

# Ruta para el apartado de definición
@app.route('/definicion')
def definicion():
    return render_template('definicion.html')

if __name__ == '__main__':
    app.run(debug=True)