from utils.math_utils import MathUtils
import random

class ElGamal:
    def __init__(self, bits=256):
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
    
    


#GERAÇÃO DAS CHAVES
p = int(input("Digite um primo grande para ser número do múdulo (p):"))
r = int(input("Digite uma raiz primitiva qualquer de p (r):"))
x = int(input("Digite um número natural 2 < x < p-2 aleatoriamente:"))

a = pow(r,x,p)


def gerar_chaves(p, r, x):
    a = pow(r,x,p)
    publica = (p,r,a)
    privada = x
    return publica, privada

chave_publica, chave_privada = gerar_chaves(p,r,x)

print("Chave pública:", chave_publica)
print("Chave privada:", chave_privada)

def converter_mensagem(mensagem):
    numeros = []

    for caractere in mensagem:
        numeros.append(ord(caractere))

    return numeros

mensagem = input(("Digite a mensagem que você quer criptografar:"))

msg_convertida = converter_mensagem(mensagem)

print(msg_convertida)