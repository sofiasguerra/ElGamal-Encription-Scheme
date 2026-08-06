#modulo de funções matematicas
import random

class MathUtils:

    # Implement the Euclidean algorithm to find the greatest common divisor (GCD) of two integers a and b
    # Implement a simple iterative function that returns the GCD of a and b
    @staticmethod
    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return abs(a)

    # Implement the Extended Euclidean algorithm to find the GCD of two integers a and b, as well as the coefficients x and y such that ax + by = gcd(a, b)
    # Implement a recursive function that returns a tuple containing the GCD and the coefficients x and y
    @staticmethod
    def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
        if b == 0:
            return a, 1, 0
        else:
            gcd, x1, y1 = MathUtils.extended_gcd(b, a % b)
            x = y1
            y = x1 - (a // b) * y1
            return gcd, x, y


    #Implement a function to compute the modular inverse of a number a modulo m using the Extended Euclidean algorithm
    @staticmethod
    def modular_inverse(a: int, m: int) -> int:
        gcd, x, _ = MathUtils.extended_gcd(a, m)
        if gcd != 1:
            raise ValueError(f"Modular inverse does not exist for a={a} and m={m}")
        return x % m

    #Implement a function to compute the modular exponentiation of a number base raised to the power of exponent modulo modulus using the method of exponentiation by squaring
    @staticmethod
    def mod_pow(base: int, exponent: int, modulus: int) -> int:
        result = 1
        base = base % modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent = exponent // 2
            base = (base * base) % modulus
        return result
    
    @staticmethod
    def eh_primo(n, k=20): #Miller-Rabin
        # k = numero de rodadas teste
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
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