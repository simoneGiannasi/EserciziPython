# Dizionario: {"a": 1, "b": 2, "c": 3}, scambio la posizione tra chiave e valore
dizionario = {"a": 1, "b": 2, "c": 3}

# Scambio chiavi e valori
dizionario_inverso = {valore: chiave for chiave, valore in dizionario.items()}

print(dizionario_inverso)
