from flask import Blueprint, render_template, request
from modules.catalogo.services import obter_todos_livros
from modules.favoritos.services import obter_favoritos

catalogo_bp = Blueprint('catalogo', __name__)


@catalogo_bp.route('/')
def index():
    genero = request.args.get('genero', '')
    livros = obter_todos_livros()
    favoritos = obter_favoritos()

    if genero:
        livros = [l for l in livros if l['genero'].lower() == genero.lower()]

    return render_template('index.html', livros=livros, genero=genero, favoritos=favoritos)