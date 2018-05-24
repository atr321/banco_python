#importar bibliotecas
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

#instanciar a app
banco = Flask(__name__)

#configurar db
banco.config['MYSQL_DATABASE_USER'] = 'root'
banco.config['MYSQL_DATABASE_PASSWORD'] = 'root'
banco.config['MYSQL_DATABASE_DB'] = 'banco'

#instanciar db
mysql = MySQL()
mysql.init_app(banco)

#rota para /
@banco.route('/')
#metodo
def index():
    return render_template('form_login.html')

#rota para /login
@banco.route('/login')
#metodo que responde /login
def login():
    cpf_cliente = request.args.get('cpf_cliente')
    senha_cliente = request.args.get('senha_cliente')

    #criar uma conexao com o db
    cursor = mysql.connect().cursor()
    #submeter o comando SQL
    cursor.execute(f'SELECT nomecliente FROM cliente where cpfcliente = {cpf_cliente} and senhacliente = {senha_cliente}')
    #recuperar dados
    dados = cursor.fetchone()
    mysql.connect().close()

    #imprimir nome
    return render_template('logado.html',nome_cliente=str(dados[0]))


    #executar
banco.run()