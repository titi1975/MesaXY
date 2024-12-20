from pynput.mouse import Listener
import threading

# Variável global para controlar o estado do clique
mouse_pressed = False

# Função chamada quando o mouse é clicado
def on_click(x, y, button, pressed):
    global mouse_pressed
    mouse_pressed = pressed  # Atualiza o estado do clique

# Função que roda enquanto o mouse está clicado
def monitor_mouse():
    global mouse_pressed
    print("Pressione o botão do mouse para iniciar o loop...")
    while True:
        if mouse_pressed:
            print("Mouse pressionado!")
            while mouse_pressed:
                print("Ainda pressionando...")
            print("Mouse liberado!")

# Configurando o listener do mouse em uma thread separada
listener = Listener(on_click=on_click)
listener.start()

# Inicia o monitoramento do mouse
monitor_mouse()
