from database import criar_conexao

# Verifica se um usuário com determinado ID e username existe na tabela 'users'
def verificar_usuario(id, username):
    conexao = criar_conexao()  # Conecta ao banco de dados
    cursor = conexao.cursor()  # Cria o cursor para executar comandos SQL

    # Executa a busca no banco
    cursor.execute("SELECT * FROM users WHERE id = ? AND username = ?", (id, username))
    resultado = cursor.fetchone()  # Retorna o primeiro resultado encontrado

    conexao.close()  # Fecha a conexão com o banco
    return resultado is not None  # Retorna True se o usuário existe, False se não


# Cadastra uma tarefa ligada a um usuário já existente no banco
def cadastrar_tarefa(id, username, titulo, descricao):
    # Primeiro verifica se o usuário existe
    if not verificar_usuario(id, username):
        print("Usuário não encontrado. Cadastre-se primeiro.")
        return  # Interrompe a função se o usuário não existir

    conexao = criar_conexao()  # Conecta ao banco
    cursor = conexao.cursor()

    # Insere uma nova tarefa no banco, ligada ao user_id correspondente
    cursor.execute('''
        INSERT INTO tarefas (user_id, titulo, descricao)
        VALUES (?, ?, ?)
    ''', (id, titulo, descricao))

    print("Tarefa cadastrada com sucesso!")

    conexao.commit()  # Salva as alterações no banco
    conexao.close()   # Fecha a conexão


def listar_tarefa(user_id, username):
    conexao = criar_conexao()
    cursor = conexao.cursor()

    # Primeiro valida se o usuário existe
    if verificar_usuario(user_id, username):
        # Busca todas as tarefas que pertencem ao usuário pelo ID
        cursor.execute(
            'SELECT titulo, descricao FROM tarefas WHERE user_id = ?', 
            (user_id,)
        )
        tarefas = cursor.fetchall()  # Pega todas as tarefas encontradas

        # Verifica se encontrou alguma tarefa
        if tarefas:
            print(f'Lista de tarefas do usuário: {username}, dono do ID: {user_id}')
            for titulo, descricao in tarefas:
                print(f'- {titulo}: {descricao}')  # Exibe cada tarefa
        else:
            print("Nenhuma tarefa encontrada.")
    else:
        print('Acesso inválido.')  # Caso o usuário não exista

    conexao.close()  # Fecha a conexão com o banco