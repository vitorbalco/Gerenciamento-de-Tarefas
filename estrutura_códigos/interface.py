from codigofinal import cadastrar_usuario
from codigofinal import verificar_usuario
from codigofinal import login_usuario
from codigofinal import cadastrar_tarefa
from codigofinal import listar_tarefa
from rich.prompt import Prompt


usuario_logado = {'id': None, 'Username': None}

def opcao_login():
    username = Prompt.ask("Usuário")
    senha = Prompt.ask("Senha", password=True)
    user_id = login_usuario(username, senha)
    if user_id:
        usuario_logado["id"] = user_id
        usuario_logado["username"] = username



def opcao_cadastrar():
    username = Prompt.ask("Novo Usuário")
    senha = Prompt.ask('Senha', password = True)
    cadastrar_usuario(username, senha)



def opcao_cadastrar_tarefa():
    if usuario_logado['id'] is None:
        print(' ⚠️ Faça login para cadastrar uma tarefa.')
        return
    
    titulo = Prompt.ask('Título da tarefa: ')
    descricao = Prompt.ask('Descrição da tarefa: ')
    cadastrar_tarefa(usuario_logado['id'], usuario_logado['username'], titulo, descricao)



def ver_tarefa():
    if usuario_logado:
        print(' ⚠️ Faça login para ver suas tarefas.')
        return
    
    listar_tarefa(usuario_logado['id'], usuario_logado['username'])


def opcao_sair():
    print('👋 Saindo do sistema. Até logo!')

            