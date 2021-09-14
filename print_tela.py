from datetime import datetime, time
import pyscreenshot as ImageGrab
import keyboard
import time

time.sleep(3)
print("Iniciando...")

while True:

    time.sleep(3)

    # Pega a data e hora
    today = datetime.now()

    # Converte para o formato desejado
    tempo = today.strftime("%d_%m_%Y %I_%M_%S")

    # Diretorio que será salvo o arquivo
    diretorio = "C:\\Users\\Breno\\Desktop\\Code\\Arquivos_Python\\visao_computacional\\printScreen\\data_img\\NW_" + tempo + ".tif"

    # Captura tela
    imagem = ImageGrab.grab()

    # Salava no formato desejado e qualidade atribuída
    imagem.save(diretorio, 'tiff', quality=100)
    print('Imagem Salva.')

    # Para o programa se tecla for pressionada
    if keyboard.is_pressed('9'):
        print("Programa Fechou.")
        break

# schedule.every(3).seconds.do(tela)
# if keyboard.is_pressed('q'):
