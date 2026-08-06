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

elTest2 = ElGamal(bits=8)
elTest2.gerar_chaves()
msg_cripto = elTest2.criptografar_mensagem("Ola, mundo! 123")
print(msg_cripto)
msg_original = elTest2.descriptografar_mensagem(msg_cripto)    
print(msg_original)