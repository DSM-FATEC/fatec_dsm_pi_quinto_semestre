from asyncio import run
from json import dumps


class WebsocketConnector:
    def __init__(self):
        self.conexoes_ativas = []

    async def conecta(self, websocket):
        await websocket.accept()

        self.conexoes_ativas.append(websocket)

    def desconecta(self, websocket):
        self.conexoes_ativas.remove(websocket)

    def envia_mensagem_para_todos(self, mensagem: str|dict):
        if not self.conexoes_ativas:
            return

        if mensagem.__class__ not in (str, dict):
            return

        if isinstance(mensagem, dict):
            mensagem = dumps(mensagem)

        for connection in self.conexoes_ativas:
            run(connection.send_text(mensagem))
