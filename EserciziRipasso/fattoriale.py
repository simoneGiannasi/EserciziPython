# Trovo il fattoriale di un numero inserito in input

# Chiedo all'utente di inserire un numero
numero = int(input("Inserisci un numero: "))

# Inizializzo il fattoriale a 1
fattoriale = 1

# Controllo se il numero è negativo, zero o positivo
if numero < 0:
    print("Il fattoriale non esiste per i numeri negativi.")
elif numero == 0:
    print("Il fattoriale di 0 è 1.")
else:
    for i in range(1, numero + 1):
        fattoriale *= i
    print(f"Il fattoriale di {numero} è {fattoriale}.")
