from algoritmos.elgamal import ElGamal
from algoritmos.rsa import RSA
from benchmark.benchmark import Benchmark
from benchmark.comparison import Comparison
import time

def escolha_de_mensagem():
    print("Escolha uma opção para a mensagem:")
    print("[1] Digitar uma mensagem")
    print("[2] Mensagem aleatória da bibliteca")
    print("[0] Voltar ao menu principal")
    opcao = input("> ")
    if opcao == "1":
        mensagem = input("Digite a mensagem: ")
        return mensagem
    elif opcao == "2":
        return getMensagemAleatoria()
    elif opcao == "0":
        return
    else:
        print("Opção inválida! Tente novamente.")
        time.sleep(2)
        return escolha_de_mensagem()


def menu_configuracao():
    print("Escolha uma opção de exibição:")
    print("[1] Detalhada")
    print("[2] Simples")
    opcao = input("> ")

    if opcao == "1":
        return "detalhada"
    elif opcao == "2":
        return "simples"
    else:
        print("Opção inválida! Tente novamente.")
        time.sleep(2)
        return menu_configuracao()


def menu_rsa(configuracao):
    mensagem = escolha_de_mensagem()
    if mensagem is None:
        return

    rsa = RSA(128)

    if configuracao == "detalhada":
        benchmark_rsa = Benchmark(rsa)

        tempo, memoria, _ = benchmark_rsa.benchmark_geracao_chaves()
        print(f"Tempo de geração de chaves: {tempo:.6f}s")
        print(f"Memória utilizada na geração de chaves: {memoria / 1024:.2f} KB")
        
        
        tempo, memoria, msg_criptografada = benchmark_rsa.benchmark_criptografia(mensagem)
        print(f"Tempo de criptografia: {tempo:.6f}s")
        print(f"Memória utilizada na criptografia: {memoria / 1024:.2f} KB")
        print(f" Mensagem criptografada: {msg_criptografada}")
        

        tempo, memoria, msg_descriptografada = benchmark_rsa.benchmark_descriptografia(msg_criptografada)
        print(f"Tempo de descriptografia: {tempo:.6f}s")
        print(f"Memória utilizada na descriptografia: {memoria / 1024:.2f} KB")
        print(f"Mensagem descriptografada: {msg_descriptografada}")
        

        if(mensagem == msg_descriptografada):
            print("A mensagem descriptografada é igual à mensagem original.")
        time.sleep(2)
        

    else:
        rsa.gerar_chaves()
        msg_criptografada = rsa.criptografar_mensagem(mensagem)
        msg_descriptografada = rsa.descriptografar_mensagem(msg_criptografada)

        print(f"Mensagem criptografada: {msg_criptografada}")
        print(f"Mensagem descriptografada: {msg_descriptografada}")
        

        if(mensagem == msg_descriptografada):
            print("A mensagem descriptografada é igual à mensagem original.")
        time.sleep(2)

    

def menu_elgamal(configuracao):
    mensagem = escolha_de_mensagem()
    if mensagem is None:
        return

    elgamal = ElGamal(128)

    if configuracao == "detalhada":
        benchmark_elgamal = Benchmark(elgamal)

        tempo, memoria, _ = benchmark_elgamal.benchmark_geracao_chaves()
        print(f"Tempo de geração de chaves: {tempo:.6f}s")
        print(f"Memória utilizada na geração de chaves: {memoria / 1024:.2f} KB")
        

        tempo, memoria, msg_criptografada = benchmark_elgamal.benchmark_criptografia(mensagem)
        print(f"Tempo de criptografia: {tempo:.6f}s")
        print(f"Memória utilizada na criptografia: {memoria / 1024:.2f} KB")
        print(f" Mensagem criptografada: {msg_criptografada}")
        

        tempo, memoria, msg_descriptografada = benchmark_elgamal.benchmark_descriptografia(msg_criptografada)
        print(f"Tempo de descriptografia: {tempo:.6f}s")
        print(f"Memória utilizada na descriptografia: {memoria / 1024:.2f} KB")
        print(f"Mensagem descriptografada: {msg_descriptografada}")
        time.sleep(2)

    else:
        elgamal.gerar_chaves()
        msg_criptografada = elgamal.criptografar_mensagem(mensagem)
        msg_descriptografada = elgamal.descriptografar_mensagem(msg_criptografada)

        print(f"Mensagem criptografada: {msg_criptografada}")
        print(f"Mensagem descriptografada: {msg_descriptografada}")
        
        if(mensagem == msg_descriptografada):
            print("A mensagem descriptografada é igual à mensagem original.")
        time.sleep(2)

        

def comparar_algoritmos():
    mensagem = escolha_de_mensagem()
    if mensagem is None:
        return

    rsa = RSA(128)           #gera dois primos de 64 bits cada, p e q, para gerar n = p*q, que terá 128 bits
    elgamal = ElGamal(128)   #gera um primo seguro p de 128 bits, e q = (p-1)/2, que terá 127 bits, e g raiz primitiva de p

    comparacao = Comparison(rsa, elgamal)
    print(comparacao.comparar_geracao_chaves())
    time.sleep(3)
    print(comparacao.comparar_criptografia(mensagem))
    time.sleep(3)

    resposta, igual = comparacao.comparar_descriptografia()
    print(resposta)

    if(igual):
        print("As mensagens descriptogradas são iguais")
    
    time.sleep(3)


def main():
    configuracao = "detalhada"
    print(
    "\n"
    "███████╗██╗      ██████╗  █████╗ ███╗   ███╗ █████╗ ██╗\n"
    "██╔════╝██║     ██╔════╝ ██╔══██╗████╗ ████║██╔══██╗██║\n"
    "█████╗  ██║     ██║  ███╗███████║██╔████╔██║███████║██║\n"
    "██╔══╝  ██║     ██║   ██║██╔══██║██║╚██╔╝██║██╔══██║██║\n"
    "███████╗███████╗╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║███████╗\n"
    "╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝\n"
    "\n"
    "███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗ ██████╗ ███╗   ██╗\n"
    "██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║\n"
    "█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║\n"
    "██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║\n"
    "███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ██║╚██████╔╝██║ ╚████║\n"
    "╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n"
    "\n"
    "======================================================================================\n"
    "                    ElGamal Encryption Scheme & RSA Cryptosystem\n"
    "======================================================================================\n"
    )
    while True:

        print(
        "\n"
        "╔══════════════════════════════════════╗\n"
        "║              MENU                    ║\n"
        "╠══════════════════════════════════════╣\n"
        "║  Escolha uma opção:                  ║\n"
        "║  [1] RSA                             ║\n"
        "║  [2] ElGamal                         ║\n"
        "║  [3] Comparar RSA x ElGamal          ║\n"
        "║  [4] Configuração de Detalhes        ║\n"
        "║                                      ║\n"
        "║  [0] Sair                            ║\n"
        "╚══════════════════════════════════════╝\n"
        )
        opcao = input("> ")
        if opcao == "1":
            menu_rsa(configuracao)
        elif opcao == "2":
            menu_elgamal(configuracao)
        elif opcao == "3":
            comparar_algoritmos()
        elif opcao == "4":
            configuracao = menu_configuracao()
        elif opcao == "0":
            print("Saindo! Até logo!")
            exit()
        else:
            print("Opção inválida! Tente novamente.")
            time.sleep(2)
    
main()
