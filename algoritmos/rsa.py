'''FUNÇÃO gerar_chaves(tamanho_bits):
    // Passo 1: escolher dois primos grandes e distintos
    p ← gerar_primo_aleatorio(tamanho_bits)
    q ← gerar_primo_aleatorio(tamanho_bits)
    ENQUANTO p == q:
        q ← gerar_primo_aleatorio(tamanho_bits)

    // Passo 2: calcular o módulo
    n ← p * q

    // Passo 3: calcular a função totiente de Euler
    φ(n) ← (p - 1) * (q - 1)

    // Passo 4: escolher o expoente público e
    // precisa satisfazer: 1 < e < φ(n)  e  mdc(e, φ(n)) = 1
    e ← 65537   // valor comum na prática (número primo de Fermat)
    VERIFICAR que mdc(e, φ(n)) == 1
    // se não for, escolher outro e ou outros p, q

    // Passo 5: calcular o expoente privado d
    // d é o inverso modular de e em relação a φ(n)
    d ← inverso_modular(e, φ(n))

    chave_publica ← (n, e)
    chave_privada ← (n, d)

FUNÇÃO cifrar(mensagem m, chave_publica (n, e)):
    // pré-condição: 0 ≤ m < n
    c ← exponenciacao_modular(m, e, n)   // c = m^e mod n
    RETORNAR c
    
FUNÇÃO decifrar(criptograma c, chave_privada (n, d)):
    m ← exponenciacao_modular(c, d, n)   // m = c^d mod n
    RETORNAR 
    
FUNÇÃO exponenciacao_modular(base, expoente, modulo):
    resultado ← 1
    base ← base mod modulo
    ENQUANTO expoente > 0:
        SE expoente é ímpar:
            resultado ← (resultado * base) mod modulo
        expoente ← expoente // 2
        base ← (base * base) mod modulo
    RETORNAR resultado
    
FUNÇÃO inverso_modular(e, phi):
    // resolve e*d ≡ 1 (mod phi) usando Euclides estendido
    (mdc, x, y) ← euclides_estendido(e, phi)
    SE mdc != 1:
        ERRO "e e phi não são coprimos"
    d ← x mod phi
    RETORNAR d

FUNÇÃO euclides_estendido(a, b):
    SE b == 0:
        RETORNAR (a, 1, 0)
    (mdc, x1, y1) ← euclides_estendido(b, a mod b)
    x ← y1
    y ← x1 - (a // b) * y1
    RETORNAR (mdc, x, y)
    
FUNÇÃO eh_primo(n, k_rodadas):
    SE n < 2: RETORNAR falso
    SE n == 2 OU n == 3: RETORNAR verdadeiro
    SE n é par: RETORNAR falso

    // escrever n-1 como 2^r * d
    r ← 0; d ← n - 1
    ENQUANTO d é par:
        r ← r + 1
        d ← d // 2

    REPETIR k_rodadas vezes:
        a ← número aleatório entre 2 e n-2
        x ← exponenciacao_modular(a, d, n)
        SE x == 1 OU x == n-1: CONTINUAR

        composto ← verdadeiro
        REPETIR r-1 vezes:
            x ← (x * x) mod n
            SE x == n-1:
                composto ← falso
                PARAR
        SE composto: RETORNAR falso

    RETORNAR verdadeiro
   '''