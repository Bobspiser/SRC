# Starts værdi af x
x = float(input("Indtast x-værdi: "))

# Inputs af brugerens valg
a = float(input("Indtast din a-værdi: "))

# a's potens
n = int(input("Indtast din n-værdi: "))

b = float(input("Indtast din b-værdi: "))

# b's potens
n_1 = int(input("Indtast din anden n-værdi: "))

c = float(input("Indtast din c-værdi: "))

# Differentiering af formelen ud fra brugerens valg af værdier
diff_a = a * n

diff_b = b * n_1

diff_n = n - 1

diff_n_1 = n_1 - 1

# Formel på diskriminanten
d = b ** 2 - 4 * a * c

if d<0:
    print("Intet nulpunkt")

else:
# Et loop for newtons metode
    for i in range(10):
    
# potenserne løftet op i x-værdien udregner både fra den normale funktion og den differentieret funktion

        x_diff_n = x ** diff_n
        x_diff_n_1 = x ** diff_n_1
        x_n = x ** n
        x_n_1 = x ** n_1

# Formel for Newtons metoden
        N = x - (a * x_n + b * x_n_1 + c) / (diff_a * x_diff_n + diff_b * x_diff_n_1)

        print(N)
# x Sættes til ans af N
        x = N
