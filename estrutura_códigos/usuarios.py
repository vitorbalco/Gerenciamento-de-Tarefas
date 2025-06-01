from database import criar_conexao  # Importa a função que conecta ao banco de dados SQLite

# Função para cadastrar um novo usuário
def cadastrar_usuario(username, senha):
    # Conecta ao banco de dados
    conexao = criar_conexao()
    cursor = conexao.cursor()

    # Verifica se já existe um usuário com esse nome
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    if cursor.fetchone():
        # Se encontrar algum usuário, avisa que já existe
        print('Erro: Usuário já existe.')
    else:
        # Caso contrário, insere o novo usuário na tabela
        cursor.execute('INSERT INTO users (username, senha) VALUES (?, ?)', (username, senha))
        conexao.commit()  # Confirma a inserção no banco
        print('Usuário cadastrado com sucesso.')

    # Fecha a conexão com o banco
    conexao.close()


# Função para verificar se um usuário existe com username e senha fornecidos
def verificar_usuario(username, senha):
    # Conecta ao banco de dados
    conexao = criar_conexao()
    cursor = conexao.cursor()

    # Busca por um usuário com o username e senha informados
    cursor.execute('SELECT * FROM users WHERE username = ? AND senha = ?', (username, senha))
    user = cursor.fetchone()  # Retorna a primeira correspondência encontrada, ou None

    conexao.close()  # Fecha a conexão

    if user:
        print(f'{username}, está no banco de dados.')
        return user[0]  # Retorna o ID do usuário encontrado
    else:
        print('Usuário não existente.')
        return None  # Retorna None caso o usuário não seja encontrado


# Função de login, semelhante à verificação, mas com mensagem de boas-vindas
def login_usuario(username, senha):
    # Conecta ao banco
    conexao = criar_conexao()
    cursor = conexao.cursor()

    # Busca pelo usuário com os dados informados
    cursor.execute('SELECT * FROM users WHERE username = ? AND senha = ?', (username, senha))
    user = cursor.fetchone()  # Retorna a linha do usuário encontrado

    conexao.close()  # Fecha a conexão

    if user:
        print(f'Bem-vindo, {username}!')
        return user[0]  # Retorna o ID do usuário
    else:
        print('Usuário inválido.')
        return None  # Retorna None se não encontrar
