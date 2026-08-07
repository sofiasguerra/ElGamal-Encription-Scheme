
from abc import ABC, abstractmethod
"""
Classe abstrata (interface) que define o contrato comum a qualquer
esquema de criptografia assimétrica implementado neste projeto (RSA,
ElGamal). Formaliza que os dois devem oferecer as mesmas operações
básicas — gerar chaves, cifrar/decifrar um bloco numérico, e
cifrar/decifrar uma mensagem de texto completa — o que permite tratá-los
de forma intercambiável (ex: no módulo de benchmark/comparação, que
opera sobre qualquer objeto que implemente essa interface, sem precisar
saber se é RSA ou ElGamal por trás).
"""
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