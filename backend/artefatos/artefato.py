# Importando as bibliotecas necessárias
from time import sleep

import machine
import urequests
import network


# Dados do artefato
ARTEFATO_ID = 1

# Dados de conexão do wifi
WIFI_SSID = ''
WIFI_SENHA = ''

# Dados do access point
ACCESS_POINT_SSID = f'guia_me_artefato_{ARTEFATO_ID}'
ACCESS_POINT_SENHA = '12345678'

# Dados do Node MCU
# machine.unique_id() -> Obtém o identificador do Arduino
CLIENT_ID = machine.unique_id()


def conecta_wifi():
    # WLAN(...) -> Instancia um novo cliente de conexão WLAN (wifi)
    # STA_If -> Indica que o Node MCU está conectado no modo wifi e não como Access Point
    sta_if = network.WLAN(network.STA_IF)
    # <cliente sta_if>.active(...) -> Ativa o cliente, permitindo que ele se
    #                               conecte a internet
    sta_if.active(True)

    # <cliente sta_if>.isconnected() -> Verifica se o cliente está conectado
    #                                 com a internet
    if not sta_if.isconnected():
        print('Conectando a', WIFI_SSID, '...')

        # <cliente sta_if>.connect(...) -> Conecta o cliente na internet
        sta_if.connect(WIFI_SSID, WIFI_SENHA)

        # Aguarda até a internet estar conectada e respondendo
        while not sta_if.isconnected():
            print('Conectando a', WIFI_SSID, '...')
            sleep(1)

    print('Conectado!')


def abre_access_point():
    # AP_IF -> Indica que o Node MCU está conectado no modo access point
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(True)

    while not ap_if.active():
        print('Ativando access point', ACCESS_POINT_SSID, '...')
        sleep(1)

    ap_if.config(essid=ACCESS_POINT_SSID, password=ACCESS_POINT_SENHA)

    print('Access point ativado!')
    print(ap_if.ifconfig())


def obtem_comportamento():
    # TODO
    ...


def executa_comportamento(comportamento):
    # TODO
    ...


# Verifica se o MicroPython já começou a executar o script, e executa a
# função main
if __name__ == '__main__':
    conecta_wifi()
    abre_access_point()

    while True:
        res = urequests.get('http://193.123.106.232:8000/ping')
        print(res.text)
        res.close()

        sleep(15)
