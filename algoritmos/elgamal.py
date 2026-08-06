from utils.math_utils import MathUtils
import random

class ElGamal:
    def __init__(self, bits):
        self.bits = bits
        self.p = None #primo grande
        self.g = None #gerador / raiz primitiva
        self.x = None #chave privada
        self.a = None #chave pública calculada

    def gerar_p_seguro(self, bits):
        while True:
            candidatoQ = MathUtils.gerar_primo(bits-1)
            candidatoP = 2 * candidatoQ + 1
            
            if MathUtils.eh_primo(candidatoP):
                self.p = candidatoP
                self.q = candidatoQ
                break
        
    def encontrar_raiz_primitiva(self):
        while True:
            candidatoG = random.randint(2, self.p-2)
            
            if (pow(candidatoG, 2, self.p)) != 1 and (pow(candidatoG, self.q, self.p)) != 1:
                self.g = candidatoG
                break
    
    def gerar_chave_privada(self):
        self.x = random.randint(3, self.p-2)
    
    def calcular_a(self):
        self.a = pow(self.g, self.x, self.p) # g^x mod p
    
    def gerar_chaves(self):
        self.gerar_p_seguro(self.bits)
        self.encontrar_raiz_primitiva()
        self.gerar_chave_privada()
        self.calcular_a()
        
    def criptografar(self, m):
        if not (0 < m < self.p):
            raise ValueError(f"Mensagem m={m} fora do intervalo válido (0, {self.p})")
        
        y = random.randint(1, self.p-2)
        c1 = pow(self.g, y, self.p)
        c2 = (m * pow(self.a, y, self.p)) % self.p
        
        return (c1, c2)
    
    def descriptografar(self, c1, c2):
        s = pow(c1, self.x, self.p)
        s_inverso = MathUtils.modular_inverse(s, self.p)
        
        m = (c2 * s_inverso) % self.p
        return m
    
    


#GERAÇÃO DAS CHAVES


def converter_mensagem(mensagem):
    numeros = []

    for caractere in mensagem:
        numeros.append(ord(caractere))

    return numeros
