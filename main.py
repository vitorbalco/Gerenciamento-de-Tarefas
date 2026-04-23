# Projeto completo com menu, login, cadastro e tarefas
# Esse projeto é ideal para aprender como construir um sistema simples de usuários com persistência de dados.
# Você pode aplicar esse tipo de projeto em sistemas de controle pessoal, aplicativos simples de tarefas,
# pequenos ERPs, apps escolares e qualquer sistema que precise registrar usuários e dados relacionados.

import sqlite3      # Permite usar banco de dados local (SQLite)
import os           # Para comandos de sistema como limpar a tela
from time import sleep
from rich.console import Console   # Usado para deixar o menu mais bonito
from rich.panel import Panel       # Painel visual no terminal
from rich import box               # Estilo de bordas para painéis

# ========== BANCO DE DADOS ==========

# Função que conecta ao banco de dados SQLite
def criar_conexao():
    return sqlite3.connect("database.db")

# Cria as tabelas no banco de dados (apenas se não existirem)
def criar_tabelas():
    conexao = criar_conexao()
    cursor = conexao.cursor()

    # Tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')

    # Tabela de tarefas associada ao usuário
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

# ========== FUNÇÕES DE USUÁRIO ==========

# Cadastra um novo usuário no banco
def cadastrar_usuario():
    username = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")

    conexao = criar_conexao()
    cursor = conexao.cursor()

    # Verifica se o usuário já existe
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print("Usuário já existe.")
    else:
        cursor.execute("INSERT INTO users (username, senha) VALUES (?, ?)", (username, senha))
        conexao.commit()
        print("Usuário cadastrado com sucesso.")
    conexao.close()

# Tenta fazer login e retorna ID e username se válido
def login_usuario():
    username = input("Usuário: ")
    senha = input("Senha: ")

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND senha = ?", (username, senha))
    user = cursor.fetchone()
    conexao.close()

    if user:
        print(f"Login bem-sucedido! Bem-vindo, {username}!")
        return user[0], username
    else:
        print("Usuário ou senha incorretos.")
        return None, None

# ========== FUNÇÕES DE TAREFA ==========

# Permite o usuário cadastrar uma nova tarefa
def cadastrar_tarefa(user_id, username):
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição: ")

    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO tarefas (user_id, titulo, descricao) VALUES (?, ?, ?)", (user_id, titulo, descricao))
    conexao.commit()
    conexao.close()
    print("Tarefa cadastrada com sucesso!")

# Lista todas as tarefas de um usuário específico
def listar_tarefas(user_id, username):
    conexao = criar_conexao()
    cursor = conexao.cursor()
    cursor.execute("SELECT titulo, descricao FROM tarefas WHERE user_id = ?", (user_id,))
    tarefas = cursor.fetchall()
    conexao.close()

    if tarefas:
        print(f"Tarefas de {username}:")
        for i, (titulo, descricao) in enumerate(tarefas, start=1):
            print(f"{i}. {titulo} - {descricao}")
    else:
        print("Nenhuma tarefa encontrada.")

# ========== MENU INTERATIVO ==========

# Inicializa o console do Rich para exibir menus com estilo
console = Console()

# Limpa a tela (funciona no Windows e Linux/macOS)
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Mostra o menu principal com opções de login e cadastro
def mostrar_menu():
    while True:
        limpar_tela()
        console.print(Panel("📋 [bold cyan]Menu Principal[/bold cyan]", box=box.DOUBLE, width=50))
        print("1. 🔐 Login")
        print("2. 📝 Cadastrar")
        print("3. ❌ Sair")
        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == "1":
            user_id, username = login_usuario()
            if user_id:
                menu_usuario_logado(user_id, username)
        elif opcao == "2":
            cadastrar_usuario()
            input("Pressione ENTER para continuar...")
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
            sleep(1)

# Menu que aparece após o login, com opções de tarefas
def menu_usuario_logado(user_id, username):
    while True:
        limpar_tela()
        console.print(Panel(f"✅ [green]Bem-vindo, {username}[/green]", box=box.ROUNDED, width=50))
        print("1. ➕ Cadastrar tarefa")
        print("2. 📋 Ver tarefas")
        print("3. 🔙 Logout")
        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == "1":
            cadastrar_tarefa(user_id, username)
            input("Pressione ENTER para continuar...")
        elif opcao == "2":
            listar_tarefas(user_id, username)
            input("Pressione ENTER para continuar...")
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")
            sleep(1)

# ========== EXECUÇÃO PRINCIPAL ==========

# Ao rodar o programa, cria as tabelas e inicia o menu
if __name__ == "__main__":
    criar_tabelas()
    mostrar_menu()
