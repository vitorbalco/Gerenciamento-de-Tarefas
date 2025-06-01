# 🗂️ Gerenciador de Tarefas no Terminal com Python + SQLite

Projeto completo de terminal desenvolvido com **Python** e **SQLite** para **gerenciar usuários e tarefas**, com um **menu interativo** utilizando a biblioteca `rich`.

---

## 💡 Sobre o Projeto

Este sistema permite que usuários realizem:
- ✅ Cadastro com verificação de usuário único
- 🔐 Login com autenticação
- 📝 Criação de tarefas individuais
- 📋 Visualização de todas as suas tarefas

Cada tarefa é associada a um usuário específico, garantindo organização e controle total sobre os dados.

---

## 📌 Funcionalidades

| Função               | Descrição                                                                 |
|----------------------|--------------------------------------------------------------------------|
| Cadastro de Usuário  | Insere nome de usuário e senha no banco de dados                        |
| Login de Usuário     | Verifica credenciais e autentica o acesso                               |
| Cadastro de Tarefa   | Associa título e descrição de tarefas a usuários autenticados           |
| Listagem de Tarefas  | Exibe todas as tarefas cadastradas do usuário logado                    |
| Menu Interativo      | Interface de navegação no terminal com a biblioteca `rich`              |

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.13+**
- **SQLite3** (banco de dados local)
- **Rich** (menu animado no terminal)
- **VS Code** (ambiente de desenvolvimento)

---

## 🧱 Estrutura do Projeto

database.py
|
|--usuarios.py
|
|--tarefas.py
|
|--interface.py
|
|--teste_rich.py
|
|--menu.py
|
|-->main.py -- COM TODOS OS CÓDIGOS COMPLETOS.




