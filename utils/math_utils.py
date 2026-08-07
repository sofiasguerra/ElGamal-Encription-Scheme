import random 

#Módulo para operações matemáticas, incluindo aritmética modular, primalidade e conversão entre grupos de bytes e números inteiros.
class MathUtils:
#========================================================================================================================================================#
        #Operações aritméticas modulares (RSA e ElGamal)
#========================================================================================================================================================#
    @staticmethod
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return abs(a)

    @staticmethod
    def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
        if b == 0:
            return a, 1, 0
        else:
            gcd, x1, y1 = MathUtils.extended_gcd(b, a % b)
            x = y1
            y = x1 - (a // b) * y1
            return gcd, x, y

    @staticmethod
    def modular_inverse(a: int, m: int) -> int:
        gcd, x, _ = MathUtils.extended_gcd(a, m)
        if gcd != 1:
            raise ValueError(f"Modular inverse does not exist for a={a} and m={m}")
        return x % m

#========================================================================================================================================================#
        # Primalidade e geração de números primos (RSA e ElGamal)   
#========================================================================================================================================================# 
    @staticmethod
    def eh_primo(n, k=4): #Miller-Rabin
        # k = numero de rodadas teste de primalidade, quanto maior k, maior a confiabilidade do teste
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        
        pequenos_primos = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
        for p in pequenos_primos:
            if n == p:
                return True
            if n % p == 0:
                return False
        
        d = n - 1 
        s = 0
        while d % 2 == 0:
            d = d // 2
            s += 1
            
        for i in range(k):
            a = random.randint(2, n-2)
            x = pow(a, d, n)   # a^d mod n
            
            if x == 1 or x == n-1:
                continue
        
            eh_composto = True
            for j in range (s-1):
                x = pow(x, 2, n)
                if x == n-1:
                    eh_composto = False
                    break
                
            if eh_composto:
                return False
        return True
    
    @staticmethod
    def gerar_primo(bits):
        while True:
            numero = random.getrandbits(bits)
            numero = numero | (1 << (bits - 1))
            numero = numero | 1
            if MathUtils.eh_primo(numero):
                return numero
            
#========================================================================================================================================================#
        #ElGamal
#========================================================================================================================================================#
    @staticmethod
    def gerar_p_seguro(bits):  
        while True:
            candidatoQ = MathUtils.gerar_primo(bits - 1)    
            candidatoP = 2 * candidatoQ + 1
        
            if MathUtils.eh_primo(candidatoP):
                return candidatoP, candidatoQ

    @staticmethod
    def encontrar_raiz_primitiva(p, q):
        while True:
            candidatoG = random.randint(2, p-2)
            
            if (pow(candidatoG, 2, p)) != 1 and (pow(candidatoG, q, p)) != 1:
                return candidatoG
            
#========================================================================================================================================================#
        # Conversão entre grupos de bytes e números inteiros (RSA e ElGamal)
#========================================================================================================================================================#
    @staticmethod
    def calcular_tamanho_bloco(p):
        k = 1
        while (256 ** (k + 1)) < p:
            k += 1
        return k
    
    @staticmethod
    def grupo_para_256(grupo):
        numero = 0
        for i, valor in enumerate(grupo):
            numero += valor * (256 ** (len(grupo) - 1 - i))
        return numero
    
    @staticmethod
    def base256_para_grupo(numero):
        grupo = []
        while numero > 0:
            grupo.append(numero % 256)
            numero //= 256
        grupo.reverse()
        return grupo
    