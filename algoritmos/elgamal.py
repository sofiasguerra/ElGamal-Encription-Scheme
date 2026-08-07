from algoritmos.asymmetric_cipher import AsymmetricCipher
from utils.math_utils import MathUtils
from utils.message_utils import MessageUtils
import random

class ElGamal(AsymmetricCipher):
    
    def __init__(self, tamanho_bits):
        self.bits = tamanho_bits
        self.p = None #primo grande
        self.g = None #gerador / raiz primitiva 
        self.a = None #chave pública calculada
        self.chave_publica = None
        self.chave_privada = None
        
    def gerar_chave_privada(self):
        self.chave_privada = random.randint(3, self.p-2)
    
    def calcular_a(self):
        self.a = pow(self.g, self.chave_privada, self.p) # g^x mod p
    
    def gerar_chaves(self):
        self.p, self.q = MathUtils.gerar_p_seguro(self.bits)
        self.g = MathUtils.encontrar_raiz_primitiva(self.p, self.q)
        self.gerar_chave_privada()
        self.calcular_a()
        self.chave_publica = (self.p, self.g, self.a)
        
    def criptografar(self, m):
        if not (0 < m < self.p):
            raise ValueError(f"Mensagem m={m} fora do intervalo válido (0, {self.p})")
        
        y = random.randint(1, self.p-2)
        c1 = pow(self.g, y, self.p)
        c2 = (m * pow(self.a, y, self.p)) % self.p
        
        return (c1, c2)
    
    def descriptografar(self, c1, c2):
        s = pow(c1, self.chave_privada, self.p)
        s_inverso = MathUtils.modular_inverse(s, self.p)
        
        m = (c2 * s_inverso) % self.p
        return m
    
    def criptografar_mensagem(self, texto):
        blocos = MessageUtils.mensagem_para_blocos(texto, self.p)
        criptogramas = []
        for bloco in blocos:
            c1, c2 = self.criptografar(bloco)
            criptogramas.append((c1, c2))
        return criptogramas
    
    def descriptografar_mensagem(self, criptogramas):
        blocos = []
        for c1, c2 in criptogramas:
            bloco = self.descriptografar(c1, c2)
            blocos.append(bloco)
        
        mensagem = MessageUtils.blocos_para_mensagem(blocos)
        return mensagem

    def get_chave_publica(self):
        return self.chave_publica

    def get_chave_privada(self):
        return self.chave_privada
    