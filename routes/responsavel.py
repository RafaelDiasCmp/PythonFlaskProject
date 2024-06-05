from flask import Blueprint, render_template, request
from database.resp import PRODUTO

responsavel_route = Blueprint('responsavel', __name__)

@responsavel_route.route('/')
def lista_responsavel():
    return render_template('lista_produtos.html', produto=PRODUTO)

@responsavel_route.route('/', methods=['POST'])
def inserir_responsavel(): #inserir os dados do produto
    
    data = request.json
    
    novo_produto = {
        "id": len(PRODUTO) + 1,
        "nome": data['nome'],
        "preco": data['preco'],
        "qtde": data['qtde'],
    }

    PRODUTO.append(novo_produto)

    return render_template('item_produto_responsavel.html', produto=novo_produto)

@responsavel_route.route('/new')
def form_responsavel(): #cadastrar um produto/responsavel
    return render_template('form_produtos.html')

@responsavel_route.route('/<int:responsavel_id>')
def detalhe_responsavel(cliente_id): # exibir detalhes responsavel
    return render_template('detalhe_responsavel.html')

@responsavel_route.route('/<int:responsavel_id>/edit')
def editar_form_responsavel(cliente_id): # editar detalhes responsavel
    return render_template('edit_form_responsavel.html')

@responsavel_route.route('/<int:responsavel_id>/update', methods=['PUT'])
def atualizar_form_responsavel(cliente_id): # atualizar detalhes responsavel
    pass

@responsavel_route.route('/<int:responsavel_id>/delete', methods=['DELETE'])
def deletar_produto(responsavel_id): # deletar detalhes responsavel
    
    global PRODUTO
    PRODUTO = [ c for c in PRODUTO if c['id'] != responsavel_id ]

    return {'deleted': 'ok'}


