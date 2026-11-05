import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from modules.catalogo.routes import catalogo_bp
from modules.favoritos.routes import favoritos_bp

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__, template_folder=template_dir)

# Registro dos módulos na arquitetura Monolítica Modular
app.register_blueprint(catalogo_bp)
app.register_blueprint(favoritos_bp, url_prefix='/favoritos')

if __name__ == '__main__':
    app.run(debug=True)