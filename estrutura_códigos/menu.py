
# Importa classes do rich para imprimir com estilo no terminal
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich import box

# Importa funções extras
from time import sleep
import os
import keyboard  # Biblioteca para detectar teclas pressionadas (instale com: pip install keyboard)

# Cria o console para imprimir no terminal usando rich
console = Console()

# Lista com as opções do menu
menu_options = ["🔒 Login", "📝 Cadastrar", "✅ Ver tarefas", "❌ Sair"]

# Índice que indica qual opção está selecionada no momento
selected_index = 0

# Função para limpar a tela, compatível com Windows e Linux/macOS
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Função que desenha o menu na tela
def draw_menu(selected):
    clear_screen()  # Limpa a tela antes de desenhar o novo menu
    # Mostra o título do menu com um painel estilizado
    console.print(Panel("📋 [bold cyan]Menu Principal[/bold cyan]", box=box.DOUBLE, width=40, style="bold"))
    
    # Para cada opção do menu, desenha com estilo diferente se for a selecionada
    for i, option in enumerate(menu_options):
        # Se for a opção selecionada, aplica estilo verde e invertido
        style = "reverse bold green" if i == selected else "white"
        # Mostra uma setinha "👉" na opção selecionada
        console.print(f"{'👉 ' if i == selected else '   '}{option}", style=style)

# Função para mostrar uma animação simples de carregando...
def animate_loading(msg="Carregando"):
    for i in range(3):
        console.print(f"{msg}{'.' * i}", end='\r')  # Mostra o texto com pontinhos
        sleep(0.3)  # Espera um pouco entre cada ponto

# Função principal onde tudo acontece
def main():
    global selected_index  # Usa a variável global para manter o índice selecionado
    
    draw_menu(selected_index)  # Desenha o menu pela primeira vez

    while True:
        # Se a tecla para cima for pressionada, move a seleção para cima
        if keyboard.is_pressed("up"):
            selected_index = (selected_index - 1) % len(menu_options)
            draw_menu(selected_index)  # Redesenha o menu com nova seleção
            sleep(0.2)  # Pequeno delay para evitar múltiplos cliques rápidos

        # Se a tecla para baixo for pressionada, move a seleção para baixo
        elif keyboard.is_pressed("down"):
            selected_index = (selected_index + 1) % len(menu_options)
            draw_menu(selected_index)
            sleep(0.2)

        # Se a tecla ENTER for pressionada, executa a opção selecionada
        elif keyboard.is_pressed("enter"):
            clear_screen()  # Limpa a tela
            animate_loading(f"Abrindo {menu_options[selected_index]}")  # Mostra "carregando..."
            # Mostra qual opção foi escolhida
            console.print(Panel(f"[green]Você escolheu:[/green] {menu_options[selected_index]}", style="bold"))
            break  # Sai do loop

        # Se a tecla ESC for pressionada, sai do menu
        elif keyboard.is_pressed("esc"):
            break

# Roda o programa principal
if __name__ == "__main__":
    main()
