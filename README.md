# TaskNexus 🚀

> Gerenciador de tarefas de alta performance com arquitetura modular, persistência em SQLite3 e sistema de autenticação segura via terminal.

---

## 🎯 Objetivo do Projeto
O TaskNexus foi concebido como um marco de transição entre scripts de automação isolados e aplicações de backend estruturadas e escaláveis. O foco central é aplicar conceitos avançados de Lógica de Programação e Banco de Dados Relacionais para gerenciar o ciclo de vida completo de tarefas (CRUD), garantindo a integridade absoluta dos dados e a individualidade de cada usuário em um ecossistema multiusuário.

Este projeto demonstra maturidade técnica em:

* **Persistência com SQLite3:** Transição de dados voláteis para um modelo relacional robusto e permanente.
* **Segurança e Autenticação:** Implementação de camadas de validação que garantem que cada usuário acesse apenas seu próprio "nexo" de informações.
* **Arquitetura de Sistemas:** Organização modular focada na separação de responsabilidades, facilitando futuras manutenções e integrações.

## 🧠 Pensamento Computacional e Engenharia
Como desenvolvedor focado em Backend, estruturei este software sob quatro pilares:

* **Decomposição:** Separação clara de responsabilidades entre as camadas de interface (`Rich`), lógica de negócios e persistência (`SQLite3`).
* **Abstração Relacional:** Modelagem de dados utilizando chaves estrangeiras (Foreign Keys) para criar um vínculo indissociável entre tarefas e seus respectivos autores.
* **Segurança Lógica:** Implementação de fluxos de autenticação que validam a identidade antes de permitir qualquer manipulação de dados.
* **Escalabilidade:** Uso de gerenciadores de contexto (`with`) para manipulação do banco de dados, evitando vazamentos de memória e travamentos (deadlocks).

## 🚀 Funcionalidades Chave
- [x] **Auth System:** Login e cadastro com validação de duplicidade de usuários.
- [x] **Relational CRUD:** Gerenciamento completo de tarefas associadas ao ID do usuário logado.
- [x] **Persistence:** Armazenamento local em arquivo `.db`, garantindo que as informações sobrevivam ao encerramento da sessão.
- [x] **Rich UI:** Interface dinâmica com tratamento de entradas (inputs) para evitar falhas de execução.

## 🛠️ Stack Técnica
* **Linguagem:** Python 3.13+
* **Database:** SQLite3 (Motor relacional local)
* **Interface:** Rich (UX/UI via CLI)
* **Padrão de Commit:** Conventional Commits

## 💻 Guia de Execução
1. Certifique-se de ter o Python instalado.
2. Clone o repositório:
   ```bash
   git clone [https://github.com/vitorbalco/TaskNexus.git](https://github.com/vitorbalco/TaskNexus.git)

## Instale as dependências necessárias:
```Bash
 pip install -r requirements.txt
```
---
**Desenvolvido por Vitor Cardoso Balco | Estudante de Sistemas de Informação | Desenvolvedor Back-end.**


