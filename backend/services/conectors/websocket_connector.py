from json import dumps

from fastapi.websockets import WebSocket


class WebsocketConnector:
    def __init__(self):
        self.conexoes_ativas = []

    async def conecta(self, websocket):
        await websocket.accept()

        self.conexoes_ativas.append(websocket)

    def desconecta(self, websocket):
        self.conexoes_ativas.remove(websocket)

    async def envia_mensagem_para_todos(self, mensagem):
        for connection in self.conexoes_ativas:
            mensagem_json = dumps(mensagem, default=str)

            await connection.send_text(mensagem_json)
