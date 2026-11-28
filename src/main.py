import sys
from automato import processar

def main():
    if len(sys.argv) != 2:
        print("Uso: python src/main.py <arquivo>")
        sys.exit(1)

    with open(sys.argv[1], encoding="utf-8-sig") as arquivo:
        for linha in arquivo:
            palavra = linha.rstrip("\r\n")
            aceita, tipo, caminho = processar(palavra)
            resultado = f"ACEITA ({tipo})" if aceita else "REJEITA"
            print(f"{palavra!r}: {resultado}")
            print("  caminho: " + " -> ".join(caminho))

if __name__ == "__main__":
    main()
