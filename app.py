# app.py

from flask import Flask, render_template, request, redirect, url_for
from config import Config
from forms import ContactForm

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Procesar el formulario
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
