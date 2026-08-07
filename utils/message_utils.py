from utils.math_utils import MathUtils


class MessageUtils:
    @staticmethod
    def texto_para_bytes(texto):
        lista = [ord(car) for car in texto]
        return lista
    
    @staticmethod
    def criar_blocos(numero, p):
        numero = str(numero)
        blocos = []
        i = 0

        while i < len(numero):
            bloco = numero[i]
            j = i + 1

            while j < len(numero):
                candidato = bloco + numero[j]

                if int(candidato) < p:
                    bloco = candidato
                    j += 1
                else:
                    break

            blocos.append(int(bloco))
            i += len(bloco)

        return blocos
    
    @staticmethod
    def mensagem_para_blocos(mensagem, p):
        lista = MessageUtils.texto_para_bytes(mensagem)
        numero = "".join(map(str, lista))
        blocos = MessageUtils.criar_blocos(numero, p)
        return blocos

    @staticmethod
    def blocos_para_numero(blocos):
        return "".join(str(bloco) for bloco in blocos)
    
    @staticmethod
    def numero_para_bytes(numero):
        bytes = []
        codigo = ""

        for digito in numero:
            codigo += digito
            valor = int(codigo)

            if 32 <= valor <= 126:
                bytes.append(valor)
                codigo = ""

        return bytes
    
    @staticmethod
    def bytes_para_texto(bytes):
        texto = "".join(chr(byte) for byte in bytes)
        return texto
    
    @staticmethod
    def blocos_para_mensagem(blocos):
        numero = MessageUtils.blocos_para_numero(blocos)
        bytes = MessageUtils.numero_para_bytes(numero)
        mensagem = MessageUtils.bytes_para_texto(bytes)
        return mensagem

    @staticmethod
    def texto_para_blocos(mensagem, p):
        letras = list(mensagem.encode("utf-8"))
        blocos = []

        # Agrupar os códigos ASCII em blocos menores que p
        k = 1
        while (256 ** (k + 1)) < p:
            k += 1

        #separar em blocos e transformar para base 256
        n_em_bloco = 0
        lista_auxiliar = []
        for letra in letras:
            lista_auxiliar.append(letra)
            n_em_bloco += 1

            if n_em_bloco == k:
                blocos.append(MathUtils.grupo_para_256(lista_auxiliar))
                lista_auxiliar = []
                n_em_bloco = 0

        # Tratar o último bloco se não estiver completo
        if lista_auxiliar:
            blocos.append(MathUtils.grupo_para_256(lista_auxiliar))

        return blocos

    @staticmethod
    def base256_para_texto(lista_base_256):
        lista_bytes = []

        for bloco in lista_base_256:
            lista_auxiliar = MathUtils._256_para_grupo(bloco)
            lista_bytes.extend(lista_auxiliar)

        return bytes(lista_bytes).decode("utf-8")