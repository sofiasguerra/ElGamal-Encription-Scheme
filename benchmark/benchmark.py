import gc
import time

from utils.math_utils import MathUtils


class Benchmark:
    def __init__(self, algoritmo):
            self.algoritmo = algoritmo

    def medir_tempo_e_memoria(self, funcao, *args):
        import time
        import tracemalloc
        import gc 

        tempos = []
        memorias = []
        for _ in range(5):
            gc.collect()
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