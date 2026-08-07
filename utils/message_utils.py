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