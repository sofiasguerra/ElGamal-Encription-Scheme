from algoritmos.asymmetric_cipher import AsymmetricCipher
from utils.math_utils import MathUtils
from utils.message_utils import MessageUtils
import random

class RSA(AsymmetricCipher):
    
    def __init__(self, tamanho_bits):
        self.bits = tamanho_bits 
        self.p = None #primo grande
        self.q = None #primo grande
        self.n = None #modulo n = p*q
        self.e = None  #exponente público
        self.phi_n = None #função totiente de n, phi(n) = (p-1)*(q-1)
        self.d = None #exponente privado, d = e^(-1) mod phi(n)
        self.chave_publica = None #(n, e)
        self.chave_privada = None #(n, d)

    def gerar_chaves(self):
        self.p = MathUtils.gerar_primo(self.bits//2)
        self.q = MathUtils.gerar_primo(self.bits//2)
        while self.p == self.q:
            self.q = MathUtils.gerar_primo(self.bits//2)
        self.calcular_n_phi()
        self.escolher_e()
        self.d = MathUtils.modular_inverse(self.e, self.phi_n)
        self.chave_publica = (self.n, self.e)
        self.chave_privada = (self.n, self.d)

    def escolher_e(self):
        while True:
            candidato = random.randint(2, self.phi_n-1)
            if MathUtils.extended_gcd(candidato, self.phi_n)[0] == 1:
                self.e = candidato
                break
    
    def calcular_n_phi(self):
        self.n = self.p * self.q
        self.phi_n = (self.p - 1) * (self.q - 1)
            
    def criptografar(self, m):
        if not (0 <= m < self.n):
            raise ValueError(f"Mensagem m={m} fora do intervalo válido (0, {self.n})")
        
        c = pow(m, self.e, self.n)
        return c
    
    def descriptografar(self, c):
        m = pow(c, self.d, self.n)
        return m
    
    def criptografar_mensagem(self, mensagem):
        blocos = MessageUtils.mensagem_para_blocos(mensagem, self.n)
        criptogramas = []
        for bloco in blocos:
            c = self.criptografar(bloco)
            criptogramas.append(c)
        return criptogramas

    def descriptografar_mensagem(self, criptogramas):
        blocos = []
        for c in criptogramas:
            m = self.descriptografar(c)
            blocos.append(m)
        
        mensagem = MessageUtils.blocos_para_mensagem(blocos)
        return mensagem

    def get_chave_publica(self):
        return self.chave_publica

    def get_chave_privada(self):
        return self.chave_privada 