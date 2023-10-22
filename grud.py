import mysql.connector

# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='crud'
)

# Criar um cursor para executar consultas
cursor = conexao.cursor()

# Operação de Criação (Create)
def criar_usuario(nome, email):
    sql = "INSERT INTO clientes (nome, email) VALUES (%s, %s)"
    valores = (nome, email)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Usuário criado com sucesso!")

# Operação de Leitura (Read)
def obter_usuarios():
    sql = "SELECT * FROM clientes"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for usuario in resultados:
        print(usuario)

# Operação de Atualização (Update)
def atualizar_usuario(idclientes, novo_nome):
    sql = "UPDATE clientes SET nome = %s WHERE idclientes = %s"
    valores = (novo_nome, idclientes)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Usuário atualizado com sucesso!")

# Operação de Exclusão (Delete)
def excluir_usuario(idclientes):
    sql = "DELETE FROM clientes WHERE idclientes = %s"
    valores = (idclientes,)
    cursor.execute(sql, valores)
    conexao.commit()
    print("Usuário excluído com sucesso!")

# Exemplo de uso
criar_usuario("João", "joao@email.com")
criar_usuario("Maria", "maria@email.com")

print("Listando clientes:")
obter_usuarios()

print("Atualizando clientes:")
atualizar_usuario(1, "João da Silva")

print("Listando usuários atualizados:")
obter_usuarios()

print("Excluindo clientes:")
excluir_usuario(2)

print("Listando clientes após exclusão:")
obter_usuarios()

# Fechar cursor e conexão
cursor.close()
conexao.close()
