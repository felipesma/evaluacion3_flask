from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def calculoPromedio():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        promedio = round((nota1 + nota2 + nota3) / 3, 1)
        asistencia = int(request.form['asistencia'])
        if promedio >= 40 and asistencia >= 75:
            resultado = 'APROBADO'
        else:
            resultado = 'REPROBADO'
        return render_template('ejercicio1.html', resultado=resultado, promedio=promedio, nota1=int(nota1), nota2=int(nota2), nota3=int(nota3), asistencia=asistencia)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def evaluarNombre():
    if request.method == 'POST':
        nombre1 = request.form.get('nombre1', '')
        nombre2 = request.form.get('nombre2', '')
        nombre3 = request.form.get('nombre3', '')
        nombres = [nombre1, nombre2, nombre3]
        nombreMayor = max(nombres, key=len)
        largoNombreMayor = len(nombreMayor)
        return render_template('ejercicio2.html',nombre1=nombre1, nombre2=nombre2, nombre3=nombre3,nombreMayor=nombreMayor, largoNombreMayor=largoNombreMayor)
    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)