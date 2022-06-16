from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Hello World com CSRF Protect - 7ASOO – Grupo 17"

if __name__ == '__main__':
    app.run()