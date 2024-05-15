from flask import Blueprint, render_template
from database.resp import RESPONSAVEL

responsavel_route = Blueprint('responsavel', __name__)

@responsavel_route.route('/')
def lista_responsavel():
    return render_template('lista_responsavel.html', responsavel=RESPONSAVEL)

@responsavel_route.route('/', methods=['POST'])
def inserir_responsavel(): #inserir os dados do responsavel
    pass

@responsavel_route.route('/new')
def form_responsavel(): #cadastrar um responsavel
    return render_template('criar_produto_responsavel.html')

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
def deletar_form_responsavel(cliente_id): # deletar detalhes responsavel
    pass


