import math

#Starts værdi af x
x = float(input("Indtast x-værdi: "))

#Inputs af brugerens valg
a = float(input("Indtast din a-værdi: "))

n_1 = int(input("Indtast din n-værdi: "))

b = float(input("Indtast din b-værdi: "))

n_2 = int(input("Indtast din anden n-værdi: "))

c = float(input("Indtast din c-værdi: "))

n_3 = int(input("indtast din tredje n-værdi: "))


diff_a = a * n_1

diff_b = b * n_2

diff_c = c * n_3

diff_n = n_1 - 1

diff_n_1 = n_2 - 1

diff_n_2 = n_3 - 1


#Differenceret ligning som der bliver skrevet ud
if n_3 >= 2:
        y = print(diff_a, "x^", diff_n
                ,diff_b, "x^", diff_n_1
                 ,diff_c, "x^", diff_n_2)

    
elif n_3 == 1:
        y = print(diff_a, "x^", diff_n
                ,diff_b, "x^", diff_n_1
                 ,diff_c)

elif n_3 == 0:
        y = print(diff_a, "x^", diff_n
                ,diff_b, "x^", diff_n_1)

#Et loop for newtons metode
for i in range(10):
    
#If, else statements for potenserne op løftet i x-værdien
    if n_3 >= 2:
        x_diff_n = x ** diff_n
        x_diff_n_1 = x ** diff_n_1
        x_diff_n_2 = x ** diff_n_2
        x_n = x ** n_1
        x_n_1 = x ** n_2
        x_n_2 = x ** n_3
    elif n_3 >= 1:
        x_diff_n = x ** diff_n
        x_diff_n_1 = x ** diff_n_1
        x_diff_n_2 = x ** diff_n_2
        x_n = x ** n_1
        x_n_1 = x ** n_2
        x_n_2 = x ** n_3
    elif n_3 == 0:
        x_diff_n = x ** diff_n
        x_diff_n_1 = x ** diff_n_1
        x_diff_n_2 = x ** diff_n_2
        x_n = x ** n_1
        x_n_1 = x ** n_2
#Formel for Newtons metoden
    N = x - (a * x_n + b * x_n_1 + c * x_n_2) / (diff_a * x_d_n + diff_b * x_diff_n_1 + diff_c * x_diff_n_2)

    print(N)
    
    x = N
