from bcrypt import hashpw, checkpw, gensalt

from exceptions.registro_nao_encontrado import RegistroNaoEncontradoException
from models.usuario_model import UsuarioModel
from repositories.base_repository import BaseRepository


class UsuarioRepository(BaseRepository):
    def __init__(self, pool):
        super().__init__(pool)

    def criptografa_senha(self, senha: str) -> str:
        senha_criptografada = hashpw(bytes(senha, 'utf-8'), gensalt(14))

        return senha_criptografada.decode('utf-8')

    def autoriza(self, email: str, senha: str) -> bool:
        query = '''
            SELECT
                email, senha
            FROM
                usuarios
            WHERE
                email = %s
        '''
        resultado = self.executa(query, argumentos=[email],
                                 retorna_resultados=True)
        if not resultado:
            return False

        usuario = dict(resultado[0])

        return checkpw(bytes(senha, 'utf-8'), bytes(usuario['senha'], 'utf-8'))

    def cria(self, usuario: UsuarioModel) -> dict:
        query = '''
            INSERT INTO usuarios
                (id_google, nome, email, senha, foto)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING
                id, id_google, nome, email, foto, criado_em, atualizado_em
        '''

        # Criptografa senha ao salvar no banco
        senha = self.criptografa_senha(usuario.senha)
        resultado = self.executa(query, argumentos=[usuario.id_google,
                                                    usuario.nome,
                                                    usuario.email,
                                                    senha,
                                                    usuario.foto],
                                 retorna_resultados=True)
        return dict(resultado[0])

    def obtem(self, id: int) -> dict:
        query = '''
            SELECT
                id, id_google, nome, email, foto, criado_em, atualizado_em
            FROM
                usuarios
            WHERE
                id = %s
        '''
        resultado = self.executa(
            query, argumentos=[id], retorna_resultados=True)

        return dict(resultado[0])

    def lista(self) -> list[dict]:
        query = '''
            SELECT
                id, id_google, nome, email, foto, criado_em, atualizado_em
            FROM
                usuarios
            ORDER BY criado_em DESC
        '''
        resultado = self.executa(query, retorna_resultados=True)

        return resultado

    def atualiza(self, usuario: UsuarioModel, id: int) -> dict:
        query = '''
            UPDATE
                usuarios
            SET
                id_google = %s,
                nome = %s,
                email = %s,
                senha = %s,
                foto = %s
            WHERE
                id = %s
            RETURNING
                id, id_google, nome, email, foto, criado_em, atualizado_em
        '''

        senha = self.criptografa_senha(usuario.senha)
        resultado = self.executa(query, argumentos=[usuario.id_google,
                                                    usuario.nome,
                                                    usuario.email,
                                                    senha,
                                                    usuario.foto,
                                                    id],
                                 retorna_resultados=True)

        return dict(resultado[0])

    def deleta(self, id: int) -> None:
        query = 'DELETE FROM usuarios WHERE id = %s'

        self.executa(query, argumentos=[id])
