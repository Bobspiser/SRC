inta = float(input("Hvad er dit interval a? "))
intb = float(input("Hvad er dit interval b? "))
a = float(input("Hvad er din a værdi? "))
b = float(input("Hvad er din b værdi? "))
c = float(input("Hvad er din c værdi? "))
potens = int(input("I hvilken potens er funktionen ?"))

for i in range(15):
    m = (inta + intb) / 2
    f_m = ((a * (m ** potens)) + b * m + c)

    if f_m < 0:
        inta = m
        print(inta, "..", intb)

    elif f_m > 0:
        intb = m
        print(inta, "..", intb)