from flask import Blueprint, render_template, request
from database.resp import PRODUTO

responsavel_route = Blueprint('responsavel', __name__)

@responsavel_route.route('/')
def lista_produtos():
    return render_template('lista_produtos.html', produto=PRODUTO)

@responsavel_route.route('/', methods=['POST'])
def inserir_produtos(): #inserir os dados do produto
    
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
def form_produtos(): #cadastrar um produto
    return render_template('form_produtos.html')

@responsavel_route.route('/<int:produto_id>')
def detalhe_produtos(produto_id): # exibir detalhes responsavel
    
    produto = list(filter(lambda c: c['id'] == produto_id, PRODUTO))[0]
    return render_template('detalhe_produto.html', produto=produto)

@responsavel_route.route('/<int:produto_id>/edit')
def editar_form_produtos(produto_id): # editar detalhes do produto
    
    produto = None
    for c in PRODUTO:
        if c['id'] == produto_id:
            produto = c

    return render_template('form_produtos.html', produto=produto)

@responsavel_route.route('/<int:produto_id>/update', methods=['PUT'])
def atualizar_form_produtos(produto_id): # atualizar detalhes do produto
    
    produto_editado = None
    
    #obtendo dados do form
    data = request.json

    #obter usuário pelo id
    for c in PRODUTO:
        if c['id'] == produto_id:
            c['nome'] = data['nome']
            c['preco'] = data['preco']
            c['qtde'] = data['qtde']

            produto_editado = c
    # editar usuário
    return render_template('item_produto_responsavel.html', produto=produto_editado)


@responsavel_route.route('/<int:produto_id>/delete', methods=['DELETE'])
def deletar_produto(produto_id): # deletar detalhes do produto
    
    global PRODUTO
    PRODUTO = [ c for c in PRODUTO if c['id'] != produto_id ]

    return {'deleted': 'ok'}


