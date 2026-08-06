from algoritmos.elgamal import ElGamal
from utils.math_utils import MathUtils

#menu 
#exibição do terminal
#chamadas das funções
Elgamal = ElGamal(bits=8)
Elgamal.gerar_chaves()
msgCrip = Elgamal.criptografar(10)
print(msgCrip)
print(Elgamal.descriptografar(msgCrip[0], msgCrip[1]))

