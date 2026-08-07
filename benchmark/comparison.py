from benchmark.benchmark import Benchmark

#Módulo que executa os mesmos testes para RSA e ElGamal e organiza os resultados para comparação.
class Comparison():
    def __init__(self, rsa, elgamal):
        self.rsa = rsa
        self.elgamal = elgamal
        self.benchmark_rsa = Benchmark(self.rsa)
        self.benchmark_elgamal = Benchmark(self.elgamal)
        self.msg_criptografada_rsa = None
        self.msg_criptografada_elgamal = None
        self.mensagem = None

    def comparar_geracao_chaves(self):
        rsa_tempo, rsa_memoria, _ = self.benchmark_rsa.benchmark_geracao_chaves()
        elgamal_tempo, elgamal_memoria, _ = self.benchmark_elgamal.benchmark_geracao_chaves()

        resposta = "Comparação de Geração de Chaves:\n"
        if rsa_tempo < elgamal_tempo:
            resposta += f"RSA foi mais rápido na geração de chaves ({rsa_tempo:.6f}s) do que ElGamal ({elgamal_tempo:.6f}s).\n"
        elif elgamal_tempo < rsa_tempo:
            resposta += f"ElGamal foi mais rápido na geração de chaves ({elgamal_tempo:.6f}s) do que RSA ({rsa_tempo:.6f}s).\n"
        else:
            resposta += f"RSA e ElGamal tiveram tempos similares na geração de chaves ({rsa_tempo:.6f}s).\n"

        if rsa_memoria < elgamal_memoria:
            resposta += f"RSA usou menos memória na geração de chaves ({rsa_memoria / 1024:.2f} KB) do que ElGamal ({elgamal_memoria / 1024:.2f} KB).\n"    
        elif elgamal_memoria < rsa_memoria:
            resposta += f"ElGamal usou menos memória na geração de chaves ({elgamal_memoria / 1024:.2f} KB) do que RSA ({rsa_memoria / 1024:.2f} KB).\n"    
        else:
            resposta += f"RSA e ElGamal usaram memória similar na geração de chaves ({rsa_memoria / 1024:.2f} KB).\n"
        return resposta

    def comparar_criptografia(self, mensagem):
        self.mensagem = mensagem

        rsa_tempo, rsa_memoria, self.msg_criptografada_rsa = self.benchmark_rsa.benchmark_criptografia(mensagem)
        elgamal_tempo, elgamal_memoria, self.msg_criptografada_elgamal = self.benchmark_elgamal.benchmark_criptografia(mensagem)

        resposta = "Comparação de Criptografia:\n"
        if rsa_tempo < elgamal_tempo:
            resposta += f"RSA foi mais rápido na criptografia ({rsa_tempo:.6f}s) do que ElGamal ({elgamal_tempo:.6f}s).\n"
        elif elgamal_tempo < rsa_tempo:
            resposta += f"ElGamal foi mais rápido na criptografia ({elgamal_tempo:.6f}s) do que RSA ({rsa_tempo:.6f}s).\n"
        else:
            resposta += f"RSA e ElGamal tiveram tempos similares na criptografia ({rsa_tempo:.6f}s).\n"

        if rsa_memoria < elgamal_memoria:
            resposta += f"RSA usou menos memória na criptografia ({rsa_memoria / 1024:.2f} KB) do que ElGamal ({elgamal_memoria / 1024:.2f} KB).\n"
        elif elgamal_memoria < rsa_memoria:
            resposta += f"ElGamal usou menos memória na criptografia ({elgamal_memoria / 1024:.2f} KB) do que RSA ({rsa_memoria / 1024:.2f} KB).\n" 
        else:
            resposta += f"RSA e ElGamal usaram memória similar na criptografia ({rsa_memoria / 1024:.2f} KB).\n"

        return resposta

    def comparar_descriptografia(self):
        rsa_tempo, rsa_memoria, mensagem_rsa = self.benchmark_rsa.benchmark_descriptografia(self.msg_criptografada_rsa)
        elgamal_tempo, elgamal_memoria, mensagem_elgamal = self.benchmark_elgamal.benchmark_descriptografia(self.msg_criptografada_elgamal)

        resposta = "Comparação de Descriptografia:\n"
        if rsa_tempo < elgamal_tempo:
            resposta += f"RSA foi mais rápido na descriptografia ({rsa_tempo:.6f}s) do que ElGamal ({elgamal_tempo:.6f}s).\n"
        elif elgamal_tempo < rsa_tempo:
            resposta += f"ElGamal foi mais rápido na descriptografia ({elgamal_tempo:.6f}s) do que RSA ({rsa_tempo:.6f}s).\n"
        else:
            resposta += f"RSA e ElGamal tiveram tempos similares na descriptografia ({rsa_tempo:.6f}s).\n"

        if rsa_memoria < elgamal_memoria:
            resposta += f"RSA usou menos memória na descriptografia ({rsa_memoria / 1024:.2f} KB) do que ElGamal ({elgamal_memoria / 1024:.2f} KB).\n"
        elif elgamal_memoria < rsa_memoria:
            resposta += f"ElGamal usou menos memória na descriptografia ({elgamal_memoria / 1024:.2f} KB) do que RSA ({rsa_memoria / 1024:.2f} KB).\n"
        else:
            resposta += f"RSA e ElGamal usaram memória similar na descriptografia ({rsa_memoria / 1024:.2f} KB).\n"

        if( self.mensagem == mensagem_elgamal and self.mensagem == mensagem_rsa):
            igual = True
        else: 
            igual = False
            
        return resposta, igual