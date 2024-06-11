from flask import Blueprint, render_template, request
from database.models.responsavel import Produto

responsavel_route = Blueprint('responsavel', __name__)

@responsavel_route.route('/')
def lista_produtos(): # Lista de Produtos
    produtos = Produto.select()
    return render_template('lista_produtos.html', produtos=produtos)

@responsavel_route.route('/', methods=['POST'])
def inserir_produtos(): #inserir os dados do produto
    
    data = request.json
    
    novo_produto = Produto.create(
        nome = data['nome'],
        preco = data['preco'],
        qtde = data['qtde'],
    )

    return render_template('item_produto_responsavel.html', produto=novo_produto)

@responsavel_route.route('/new')
def form_produtos(): #cadastrar um produto
    return render_template('form_produtos.html')

@responsavel_route.route('/<int:produto_id>')
def detalhe_produtos(produto_id): # exibir detalhes responsavel
    
    produto = Produto.get_by_id(produto_id)
    return render_template('detalhe_produto.html', produto=produto)

@responsavel_route.route('/<int:produto_id>/edit')
def editar_form_produtos(produto_id): # editar detalhes do produto
    
    
    produto = Produto.get_by_id(produto_id)
    return render_template('form_produtos.html', produto=produto)

@responsavel_route.route('/<int:produto_id>/update', methods=['PUT'])
def atualizar_form_produtos(produto_id): # atualizar detalhes do produto
    
    
    
    #obtendo dados do form
    data = request.json
    
    produto_editado = Produto.get_by_id(produto_id)
    produto_editado.nome = data['nome']
    produto_editado.preco = data['preco']
    produto_editado.qtde = data['qtde']
    produto_editado.save()
    
    # editar usuário
    return render_template('item_produto_responsavel.html', produto=produto_editado)


@responsavel_route.route('/<int:produto_id>/delete', methods=['DELETE'])
def deletar_produto(produto_id): # deletar detalhes do produto
    
    produto = Produto.get_by_id(produto_id)
    produto.delete_instance()
    return {'deleted': 'ok'}

