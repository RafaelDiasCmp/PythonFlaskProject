# Sistema de Comandas

Este é um projeto de um sistema de comanda desenvolvido em Python utilizando o framework Flask, SQL para banco de dados e serviços do Google Cloud Platform (GCP). O sistema permite cadastrar responsáveis, criar produtos e barracas para os produtos.

## Funcionalidades

- Cadastro de responsáveis pela barraca.
- Criação e gerenciamento de produtos.
- Criação e gerenciamento de barracas.
- Interface web intuitiva para gerenciamento das comandas.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento do sistema.
- **Flask**: Framework web utilizado para criar a interface do sistema.
- **SQL**: Utilizado para armazenar os dados de usuários, produtos e barracas.
- **Google Cloud Platform (GCP)**: Serviços de nuvem para deploy, autenticação e banco de dados.

## Pré-requisitos

- Python 3.x
- Conta no Google Cloud Platform (GCP)
- Serviço de banco de dados SQL no GCP (por exemplo, Cloud SQL)
- Google Cloud SDK instalado e configurado

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/sistema-de-comanda.git
    cd sistema-de-comanda
    ```

2. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente necessárias para o Flask e GCP:
    ```sh
    export FLASK_APP=app.py
    export GOOGLE_CLOUD_PROJECT=seu-projeto-id
    export GOOGLE_APPLICATION_CREDENTIALS="caminho/para/seu/arquivo-de-credenciais.json"
    export DATABASE_URL="url-do-banco-de-dados"
    ```

5. Inicialize o banco de dados:
    ```sh
    flask db upgrade
    ```

6. Execute a aplicação:
    ```sh
    flask run
    ```

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask.
- `models.py`: Definição dos modelos de dados (Responsáveis, Produtos, Barracas).
- `routes.py`: Definição das rotas e lógica da aplicação.
- `templates/`: Diretório contendo os templates HTML para as páginas da web.
- `static/`: Diretório para arquivos estáticos (CSS, JavaScript, imagens).
- `migrations/`: Diretório para arquivos de migração do banco de dados.

## Configuração do GCP

1. Crie um projeto no Google Cloud Platform.
2. Ative as APIs necessárias (Cloud SQL, Cloud Storage, etc.).
3. Configure um banco de dados SQL (MySQL, PostgreSQL, etc.).
4. Crie e baixe um arquivo de credenciais JSON para autenticação.
5. Configure as variáveis de ambiente conforme indicado acima.

## Contribuição

1. Fork o projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/sua-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Push para a branch (`git push origin feature/sua-feature`).
5. Abra um Pull Request.
