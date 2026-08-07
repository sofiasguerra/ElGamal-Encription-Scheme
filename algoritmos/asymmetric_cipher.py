
from abc import ABC, abstractmethod

class AsymmetricCipher(ABC):

    @abstractmethod
    def gerar_chaves(self):
        pass

    @abstractmethod
    def criptografar(self, bloco):
        pass

    @abstractmethod
    def descriptografar(self, criptograma):
        pass

    @abstractmethod
    def criptografar_mensagem(self, mensagem):
        pass

    @abstractmethod
    def descriptografar_mensagem(self, criptograma):
        pass

    @abstractmethod
    def get_chave_publica(self):
        pass

    @abstractmethod
    def get_chave_privada(self):
        pass