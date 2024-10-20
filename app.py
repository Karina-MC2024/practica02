from flask import Flask, render_template, request

app = Flask(__name__)  # Corregido: __name__ en lugar de _name_

# Ruta principal para mostrar la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar la inscripción en curso
@app.route('/inscripcion', methods=['POST'])
def inscripcion():
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    curso = request.form['curso']
    # Aquí podrías procesar los datos o guardarlos en una base de datos
    return f"Inscripción recibida: {nombre} {apellidos} al curso {curso}"

# Ruta para manejar el registro de usuarios
@app.route('/usuarios', methods=['POST'])
def usuarios():
    nombre = request.form['nombre-usuario']
    apellidos = request.form['apellidos-usuario']
    email = request.form['email']
    password = request.form['password']
    return f"Usuario registrado: {nombre} {apellidos}, Email: {email}"

# Ruta para manejar el registro de productos
@app.route('/productos', methods=['POST'])
def productos():
    producto = request.form['producto']
    categoria = request.form['categoria']
    existencia = request.form['existencia']
    precio = request.form['precio']
    return f"Producto registrado: {producto}, Categoría: {categoria}, Existencia: {existencia}, Precio: {precio}"

# Ruta para manejar el registro de libros
@app.route('/libros', methods=['POST'])
def libros():
    titulo = request.form['titulo']
    autor = request.form['autor']
    resumen = request.form['resumen']
    medio = request.form['medio']
    return f"Libro registrado: {titulo} por {autor}, Medio: {medio}"

# Corregido: __name__ y __main__ en lugar de _name_ y _main_
if __name__ == '__main__':
    app.run(debug=True)
