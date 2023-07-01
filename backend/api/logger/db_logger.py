import logging
from sys import exc_info

from models.log_model import LogModel
from repositories.log_repository import LogRepository


class DbLogger:
    def __init__(self, repository: LogRepository):
        self.repository = repository

    def info(self, mensagem: str) -> None:
        logging.info(mensagem)

        self.repository.cria(LogModel(nivel='info', mensagem=mensagem))

    def erro(self, mensagem: str|Exception) -> None:
        logging.error(mensagem)

        if isinstance(mensagem, Exception):
            mensagem = str(exc_info())

        self.repository.cria(LogModel(nivel='erro', mensagem=mensagem))

    def debug(self, mensagem: str) -> None:
        logging.debug(mensagem)

        self.repository.cria(LogModel(nivel='debug', mensagem=mensagem))

    def aviso(self, mensagem: str) -> None:
        logging.warn(mensagem)

        self.repository.cria(LogModel(nivel='aviso', mensagem=mensagem))
