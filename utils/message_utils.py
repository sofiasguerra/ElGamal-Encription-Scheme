from utils.math_utils import MathUtils


class MessageUtils:
    @staticmethod
    def texto_para_bytes(texto):
        lista = [ord(car) for car in texto]
        return MathUtils.grupo_para_256(lista)
