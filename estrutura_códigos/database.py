import sqlite3
    #Importa o banco de dados para o python 
def criar_conexao():
    conexao = sqlite3.connect('database.db')
    return conexao    #Criação da conexão para o banco de dados

def criar_tabela():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    # Criação da tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')

    # Criação da tabela de tarefas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            titulo TEXT NOT NULL,
            descricao TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    conexao.commit()
    conexao.close()
    print("Tabelas criadas com sucesso.")
    







 