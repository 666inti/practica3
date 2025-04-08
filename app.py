from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/contactanos')
def contactanos():
    return render_template('contactanos.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    mensaje = request.form.get("mensaje")
    return render_template("salida.html",name=name,email=email,mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)