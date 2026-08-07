from algoritmos.elgamal import ElGamal
from algoritmos.rsa import RSA


#menu 
#exibição do terminal
#chamadas das funções

msg = "TerMInei ess4 b0mbbb4, e s4mu3l aind4 quuuerr complicar XD!"

print("Mensagem Original: ", msg)

print("---------------------------------------------------")
print("Criptografia RSA")
rsaTest = RSA(tamanho_bits=8)
rsaTest.gerar_chaves()  
msg_cripto_rsa = rsaTest.criptografar_mensagem(msg)
print(msg_cripto_rsa)
msg_original_rsa = rsaTest.descriptografar_mensagem(msg_cripto_rsa)
print(msg_original_rsa)

print("---------------------------------------------------")
print("Criptografia ElGamal")
elTest2 = ElGamal(tamanho_bits=8)
elTest2.gerar_chaves()
msg_cripto = elTest2.criptografar_mensagem(msg)
print(msg_cripto)
msg_original = elTest2.descriptografar_mensagem(msg_cripto)    
print(msg_original)