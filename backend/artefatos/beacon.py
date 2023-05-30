# Importando as bibliotecas necessárias
from time import sleep

import network


# Dados do artefato
ARTEFATO_ID = 1

# Dados do access point
ACCESS_POINT_SSID = f'guia_me_artefato_{ARTEFATO_ID}'
ACCESS_POINT_SENHA = '12345678'


def abre_access_point():
    # AP_IF -> Indica que o Node MCU está conectado no modo access point
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True)

    while not ap_if.active():
        print('Ativando access point', ACCESS_POINT_SSID, '...')
        sleep(1)

    ap_if.config(essid=ACCESS_POINT_SSID, password=ACCESS_POINT_SENHA)

    print('Access point ativado!')


# Verifica se o MicroPython já começou a executar o script, e executa a
# função main
if __name__ == '__main__':
    abre_access_point()

    while True:
        ...
