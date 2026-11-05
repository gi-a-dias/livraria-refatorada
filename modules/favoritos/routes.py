from flask import Blueprint, jsonify
from modules.favoritos.services import alternar_favorito, obter_favoritos

favoritos_bp = Blueprint('favoritos', __name__)


@favoritos_bp.route('/api/favoritos', methods=['GET'])
def listar_favoritos():
    return jsonify({
        "status": "sucesso",
        "favoritos": obter_favoritos()
    }), 200


@favoritos_bp.route('/api/favoritos/<livro_id>', methods=['POST'])
def favoritar(livro_id):
    is_favorito = alternar_favorito(livro_id)
    estado = "adicionado" if is_favorito else "removido"

    return jsonify({
        "status": "sucesso",
        "mensagem": f"Livro {livro_id} {estado} dos favoritos.",
        "is_favorito": is_favorito
    }), 200