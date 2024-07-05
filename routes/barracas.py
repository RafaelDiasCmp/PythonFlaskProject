from flask import Blueprint, render_template, request, redirect, url_for
from database.models.barraca import Barraca, ProdutoBarraca
from database.models.responsavel import Produto

barraca_route = Blueprint('barraca', __name__)

@barraca_route.route('/')
def lista_barracas(): # Lista de Barracas
    barracas = Barraca.select()
    return render_template('lista_barracas.html', barracas=barracas)

@barraca_route.route('/', methods=['POST'])
def inserir_barraca(): # Inserir os dados da barraca
    
    data = request.form
    
    nova_barraca = Barraca.create(
        nome=data['nome'],
        responsavel=data['responsavel']
    )

    return redirect(url_for('barraca.lista_barracas'))

@barraca_route.route('/new')
def form_barraca(): # Formulário para cadastrar uma barraca
    return render_template('form_barraca.html')

@barraca_route.route('/<int:barraca_id>')
def detalhe_barraca(barraca_id): # Exibir detalhes da barraca e produtos
    
    barraca = Barraca.get_by_id(barraca_id)
    produtos = ProdutoBarraca.select().where(ProdutoBarraca.barraca == barraca_id)
    return render_template('detalhe_barraca.html', barraca=barraca, produtos=produtos)
