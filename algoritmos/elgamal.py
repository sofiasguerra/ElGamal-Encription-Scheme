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