import re


class Validador:
    # Valida o tamanho máximo de um campo de texto ou de uma lista
    @staticmethod
    def max(valor, campo, maximo):
        if len(valor) > maximo:
            raise ValueError(f'campo {campo} muito grande, máximo de {maximo} caracteres')

    # Valida se uma string é compatível com uma expresse regex
    @staticmethod
    def regex(valor, campo, expressao):
        if not re.match(expressao, valor):
            raise ValueError(f'campo {campo} não conforme com o formato {expressao}')

    # Valida se o campo é vazo ou nulo ou falso
    @staticmethod
    def filled(valor, campo):
        if not valor:
            raise ValueError(f'campo {campo} não pode ser falso, vazio ou nulo')

    @staticmethod
    def not_null(valor, campo):
        if valor is None:
            raise ValueError(f'campo {campo} não pode ser nulo')

    @staticmethod
    def existe_em(valor, campo, valores_validos):
        if not valor in valores_validos:
            raise ValueError(f'campo {campo} não é valido')

