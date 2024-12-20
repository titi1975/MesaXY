import pyautogui
import time
from pynput.mouse import Listener

file = open('coordenadas.txt','w')
file.write('lista de coordenadas: \n')
class Coordenada:  # Classe para armazenamento das coordenadas do mouse
    def __init__(self, coordenadaX, coordenadaY):
        self.coordenadas = (coordenadaX, coordenadaY)

    def Mostrar_cord(self):  # Função para mostrar a coord atual
        print(self.coordenadas)

# Lista para armazenar as coordenadas
lista_de_cord = []

# Variável para controlar o estado do clique
mouse_clicado = False

# Função chamada quando o mouse é clicado
def on_click(x, y, button, pressed):
    global mouse_clicado
    mouse_clicado = pressed  # Atualiza o estado do clique

# Configura o listener para monitorar cliques
listener = Listener(on_click=on_click)
listener.start()

# Loop para coletar coordenadas
i = 0
while i <= 10:
    if mouse_clicado:  # Executa apenas se o mouse estiver clicado
        currentMouseX, currentMouseY = pyautogui.position()
        mouse = Coordenada(currentMouseX, currentMouseY)
        lista_de_cord.append(mouse.coordenadas)
        file.write('cord '+ str(i) + ': ('+str(mouse.coordenadas[0]) +','+ str(mouse.coordenadas[1])+')')
        file.write('\n')
    time.sleep(1)  # Reduz a frequência do loop para evitar alto consumo de CPU
    i += 1
file.close()
# Exibe a lista de coordenadas capturadas
print(lista_de_cord)

