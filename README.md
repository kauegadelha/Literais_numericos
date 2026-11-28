# Literais Numéricos (AFD)

Reconhecedor de literais numéricos implementado como um autômato finito
determinístico. Para cada número, mostra se foi aceito ou rejeitado, o tipo
(inteiro, decimal ou expoente) e o caminho de estados percorrido.

## Requisitos

Python 3.9 ou mais recente. Não há dependências externas.

## Como compilar e rodar

Python é interpretado, então não há etapa de compilação. A partir da pasta
raiz do projeto:

```
python src/main.py testes/palavras.txt
```

Para rodar outro arquivo, troque o caminho. O arquivo deve ter um número por linha.