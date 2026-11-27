ALFABETO = set("0123456789+-.eE")
INICIAL = "qInicial"
POCO = "qPoco"

automato = {
    "qInicial": {   # ponto de partida
        "final": False, "tipo": None,
        "transicoes": {"+": "qSinal", "-": "qSinal", "0": "q0"}
                      | {d: "q1" for d in "123456789"},
    },

    "qSinal": {     # leu '+' ou '-'
        "final": False, "tipo": None,
        "transicoes": {"0": "q0"} | {d: "q1" for d in "123456789"},
    },

    "q0": {         # leu um único 0
        "final": True, "tipo": "inteiro",
        "transicoes": {".": "q.", "e": "qE", "E": "qE"},
    },

    "q1": {         # parte inteira começando com 1-9
        "final": True, "tipo": "inteiro",
        "transicoes": {d: "q1" for d in "0123456789"}
                      | {".": "q.", "e": "qE", "E": "qE"},
    },

    "q.": {         # leu o ponto, falta dígito
        "final": False, "tipo": None,
        "transicoes": {d: "qDecimal" for d in "0123456789"},
    },

    "qDecimal": {   # dígitos depois do ponto
        "final": True, "tipo": "decimal",
        "transicoes": {d: "qDecimal" for d in "0123456789"}
                      | {"e": "qE", "E": "qE"},
    },

    "qE": {       # leu 'E' ou 'e'
        "final": False, "tipo": None,
        "transicoes": {"+": "qSinalExp", "-": "qSinalExp"}
                      | {d: "qDigitosExp" for d in "0123456789"},
    },

    "qSinalExp": {  # sinal do expoente
        "final": False, "tipo": None,
        "transicoes": {d: "qDigitosExp" for d in "0123456789"},
    },

    "qDigitosExp": {  # dígitos do expoente
        "final": True, "tipo": "expoente",
        "transicoes": {d: "qDigitosExp" for d in "0123456789"},
    },

    "qPoco": {      # estado de erro
        "final": False, "tipo": None,
        "transicoes": {},
    },
}

ESTADOS = set(automato)

FINAIS = set()
for nome, dados in automato.items():
    if dados["final"]:
        FINAIS.add(nome)