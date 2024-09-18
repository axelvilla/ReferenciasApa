from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    data = {'tituloPagina': 'Autor único'}
    if request.method == 'POST':
        apellido = request.form['Apellido']
        nombre = request.form['Nombre']
        anio = request.form['Anio']
        titulo = request.form['Titulo']
        editorial = request.form['Editorial']
        data = {
            'tituloPagina': 'Autor único',
            'apellido': apellido.capitalize(),
            'nombre': nombre[0:1].capitalize(),
            'anio': anio,
            'titulo': titulo.capitalize(),
            'editorial': editorial.capitalize(),
        }
    return render_template('index.html', data = data)

@app.route('/institucional', methods = ['GET', 'POST'])
def institucional():
    data = {'tituloPagina': 'Autor Institucional'}
    if request.method == 'POST':
        institucion = request.form['institucion']
        anio = request.form['Anio']
        titulo = request.form['Titulo']
        editorial = request.form['Editorial']
        data = {
            'tituloPagina': 'Autor Institucional',
            'institucion': institucion.capitalize(),
            'anio': anio,
            'titulo': titulo.capitalize(),
            'editorial': editorial.capitalize(),
        }
    return render_template('institucional.html', data = data)

@app.route('/libros', methods = ['GET', 'POST'])
def libros():
    data = {'tituloPagina': 'Libros Electronicos'}
    if request.method == 'POST':
        apellido = request.form['Apellido']
        nombre = request.form['Nombre']
        anio = request.form['Anio']
        titulo = request.form['Titulo']
        editorial = request.form['Editorial']
        url = request.form['url']
        data = {
            'tituloPagina': 'Libros Electronicos',
            'apellido': apellido.capitalize(),
            'nombre': nombre[0:1].capitalize(),
            'anio': anio,
            'titulo': titulo.capitalize(),
            'editorial': editorial.capitalize(),
            'url': url
        }
    return render_template('libros_electronicos.html', data = data)

@app.route('/web_autor', methods = ['GET', 'POST'])
def web_autor():
    data = {'tituloPagina': 'Sitio Web con autor'}
    if request.method == 'POST':
        apellido = request.form['Apellido']
        nombre = request.form['Nombre']
        fecha = request.form['fecha']
        titulo = request.form['Titulo']
        nombreSitio = request.form['nombreSitio']
        url = request.form['url']
        data = {
            'tituloPagina': 'Sitio Web con autor',
            'apellido': apellido.capitalize(),
            'nombre': nombre[0:1].capitalize(),
            'fecha': fecha,
            'titulo': titulo.capitalize(),
            'nombreSitio': nombreSitio.capitalize(),
            'url': url
        }
    return render_template('web_autor.html', data = data)

@app.route('/web_no_autor', methods = ['GET', 'POST'])
def web_no_autor():
    data = {'tituloPagina': 'Sitio Web sin autor'}
    if request.method == 'POST':
        titulo = request.form['titulo']
        fecha = request.form['fecha']
        nombreSitio = request.form['nombreSitio']
        url = request.form['url']
        data = {
            'tituloPagina': 'Sitio Web sin autor',
            'fecha': fecha,
            'titulo': titulo.capitalize(),
            'nombreSitio': nombreSitio.capitalize(),
            'url': url
        }
    return render_template('web_no_autor.html', data = data)

@app.route('/video_internet', methods = ['GET', 'POST'])
def video_internet():
    data = {'tituloPagina': 'Video de Internet'}
    if request.method == 'POST':
        canal = request.form['canal']
        fecha = request.form['fecha']
        titulo = request.form['Titulo']
        nombreSitio = request.form['nombreSitio']
        url = request.form['url']
        data = {
            'tituloPagina': 'Video de Internet',
            'canal': canal,
            'fecha': fecha,
            'titulo': titulo.capitalize(),
            'nombreSitio': nombreSitio.capitalize(),
            'url': url
        }
    return render_template('video_internet.html', data = data)




if __name__ == '__main__':
    app.run( debug=False)