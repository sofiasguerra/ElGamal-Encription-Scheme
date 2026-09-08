# RSA e ElGamal

Implementação em Python de dois algoritmos clássicos de criptografia assimétrica, **RSA** e **ElGamal**, com um módulo de benchmark para comparar o desempenho dos dois em tempo de execução e consumo de memória.

Projeto desenvolvido para a disciplina de Fundamentos de Matemática para Ciências da Computação II (FMCC2) — UFCG.

## Estrutura do projeto

- **algoritmos/**: implementação dos algoritmos RSA e ElGamal.
- **benchmark/**: funções responsáveis por medir e comparar o desempenho dos algoritmos.
- **utils/**: funções auxiliares para operações matemáticas, manipulação de mensagens e arquivos.
- **main.py**: arquivo principal para executar o programa.

## Funcionalidades

- Geração de números primos seguros, com teste de primalidade de Miller-Rabin.
- Geração de chaves pública e privada para RSA e ElGamal.
- Criptografia e descriptografia de mensagens.
- Conversão de mensagens em blocos numéricos (codificação base-256).
- Medição de tempo de execução e consumo de memória.
- Comparação de desempenho entre RSA e ElGamal via benchmark.

## Como executar

```bash
python main.py
```

## Objetivo

O projeto foi desenvolvido com fins acadêmicos, para estudar o funcionamento do algoritmo ElGamal e compará-lo, por meio de benchmarks, com o algoritmo RSA — incluindo a implementação dos fundamentos matemáticos por trás de ambos (geração de primos seguros, teste de primalidade, aritmética modular).

## Autoria

Projeto desenvolvido em dupla por [Samuel Feitosa](https://github.com/S-Feitosa) e [Sofia Guerra](https://github.com/sofiasguerra).
