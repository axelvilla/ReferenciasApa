from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        data = {
        'apellido': apellido,
        'nombre': nombre,
        'anio': anio,
        'titulo': titulo,
        'editorial': editorial,
    }
        apellido = request.form['Apellido']
        nombre = request.form['Nombre']
        anio = request.form['Anio']
        titulo = request.form['Titulo']
        editorial = request.form['Editorial']
    
    return render_template('index.html', data = data)

@app.route('/institucional', methods = ['GET', 'POST'])
def institucional():
    if request.method == 'POST':
        apellido = request.form['Apellido']
        nombre = request.form['Nombre']
        anio = request.form['Anio']
        titulo = request.form['Titulo']
        editorial = request.form['Editorial']
        data = {
            'apellido': apellido,
            'nombre': nombre,
            'anio': anio,
            'titulo': titulo,
            'editorial': editorial,
        }
    return render_template('institucional.html', data = data)




if __name__ == '__main__':
    app.run(debug=True)