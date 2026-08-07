"""
Módulo de medição de desempenho (benchmark) para os algoritmos de
criptografia (RSA e ElGamal). Mede tempo de execução e uso de memória
das etapas de geração de chaves, criptografia e descriptografia,
fazendo a média de várias execuções para reduzir ruído nas medições.
"""
class Benchmark:
    def __init__(self, algoritmo):
            self.algoritmo = algoritmo

    def medir_tempo_e_memoria(self, funcao, *args):
       
        # roda 5 vezes e tira a média, porque uma execução só pode variar bastante
        # (outros processos rodando, coleta de lixo no meio, etc) e distorcer a medição
        import time
        import tracemalloc
        import gc 

        tempos = []
        memorias = []
        for _ in range(5):
            gc.collect() # limpa o lixo antes de medir, pra não contar memória de execuções passadas
            tracemalloc.start()
            inicio = time.perf_counter()
            resultado = funcao(*args)
            fim = time.perf_counter()
            _, memoria = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            tempos.append(fim - inicio)
            memorias.append(memoria)

        media_tempo = sum(tempos) / len(tempos)
        media_memoria = sum(memorias) / len(memorias)
        return (media_tempo, media_memoria, resultado)

    def benchmark_geracao_chaves(self):
        return self.medir_tempo_e_memoria(self.algoritmo.gerar_chaves)

    def benchmark_criptografia(self, mensagem):
        return self.medir_tempo_e_memoria(self.algoritmo.criptografar_mensagem, mensagem)

    def benchmark_descriptografia(self, criptogramas):
        return self.medir_tempo_e_memoria(self.algoritmo.descriptografar_mensagem, criptogramas)