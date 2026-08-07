#classe para fazer a comparação
from utils.math_utils import MathUtils


class Benchmark:
    def __init__(self, algoritmo):
            self.algoritmo = algoritmo

    def medir_tempo_e_memoria(self, funcao, *args):
        import time
        import tracemalloc
        tracemalloc.start()
        start_time = time.perf_counter()

        resultado = funcao(*args)

        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return end_time - start_time, peak, resultado

    def benchmark_geracao_chaves(self):
        return self.medir_tempo_e_memoria(self.algoritmo.gerar_chaves)

    def benchmark_criptografia(self, mensagem):
        return self.medir_tempo_e_memoria(self.algoritmo.criptografar_mensagem, mensagem)

    def benchmark_descriptografia(self, criptogramas):
        return self.medir_tempo_e_memoria(self.algoritmo.descriptografar_mensagem, criptogramas)