# Input sat i variabler der skal bestemme hvordan andengradsfunktionen ser ud
# Samtidig er der også variabler for hvad de 2 intervaller er på hver side a nulpunkte
inta = float(input("Hvad er dit interval a? "))
intb = float(input("Hvad er dit interval b? "))
a = float(input("Hvad er din a værdi? "))
b = float(input("Hvad er din b værdi? "))
c = float(input("Hvad er din c værdi? "))
potens = int(input("I hvilken potens er funktionen? "))

loop = True
# Så mange gange bisektion bliver lavet
# for i in range(15):
while loop:
    # Udregningen af bisektion og bliver gemt i variablerne dette vil blive erstattet hver gang den gentager
    m = (inta + intb) / 2
    f_m = ((a * (m ** potens)) + b * m + c)

    # Bestemmer om det er enten f(a) eller f(b) der skal udskiftet og printer de nye værdier
    if f_m < 0:
        inta = m
        print(inta, "||", intb)
        if intb - inta < 0.00001:
            loop = False

    elif f_m > 0:
        intb = m
        print(inta, "||", intb)
        if intb - inta < 0.00001:
            loop = False
