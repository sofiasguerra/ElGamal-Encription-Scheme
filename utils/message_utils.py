from utils.math_utils import MathUtils

"""
Módulo de conversão entre texto e blocos numéricos cifráveis, usado tanto
por RSA quanto por ElGamal. Uma mensagem de texto é convertida para bytes 
(UTF-8), agrupada em blocos de tamanho fixo (menor que o módulo p/n usado
na cifragem), e cada bloco é representado como um único inteiro em base
256 — pronto para ser passado à função de cifragem de cada esquema.
"""
class MessageUtils:
    @staticmethod
    def mensagem_para_blocos(mensagem, p):
        letras = list(mensagem.encode("utf-8"))
        blocos = []

        # Agrupar os códigos ASCII em blocos menores que p
        k = MathUtils.calcular_tamanho_bloco(p)

        # Separar em blocos e transformar para base 256
        n_em_bloco = 0
        lista_auxiliar = []
        for letra in letras:
            lista_auxiliar.append(letra)
            n_em_bloco += 1

            if n_em_bloco == k:
                 # Bloco completo (k bytes), converte pra número e reseta pro próximo
                blocos.append(MathUtils.grupo_para_256(lista_auxiliar))
                lista_auxiliar = []
                n_em_bloco = 0

        # Tratar o último bloco se não estiver completo
        if lista_auxiliar:
            blocos.append(MathUtils.grupo_para_256(lista_auxiliar))

        return blocos

    @staticmethod
    def blocos_para_mensagem(lista_base_256):
         # Caminho inverso: cada bloco (número) volta a ser uma lista de bytes
        lista_bytes = []

        for bloco in lista_base_256:
            lista_auxiliar = MathUtils.base256_para_grupo(bloco)
            lista_bytes.extend(lista_auxiliar)

         # Junta todos os bytes e decodifica de volta pra texto
        return bytes(lista_bytes).decode("utf-8")
