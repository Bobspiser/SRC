import math

#Starts værdi af x
x = float(input("Indtast x-værdi: "))

#Inputs af brugerens valg
a = float(input("Indtast din a-værdi: "))

n = int(input("Indtast din n-værdi: "))

b = float(input("Indtast din b-værdi: "))

n1 = int(input("Indtast din anden n-værdi: "))

c = float(input("Indtast din c-værdi: "))

n2 = int(input("indtast din tredje n-værdi: "))


da = a*n

db = b*n1

dc = c*n2

dn = n-1

dn1 = n1-1

dn2 = n2-1


#Differenceret ligning som der bliver skrevet ud
if n2>=2:
        y = print(da, "x^", dn
                ,db, "x^", dn1
                 ,dc, "x^", dn2)

    
elif n2==1:
        y = print(da, "x^", dn
                ,db, "x^", dn1
                 ,dc)

elif n2==0:
        y = print(da, "x^", dn
                ,db, "x^", dn1)

#Et loop for newtons metode
for i in range(10):
    
#If, else statements for potenserne op løftet i x-værdien
    if n2>=2:
        xdn=x**dn
        xdn1=x**dn1
        xdn2=x**dn2
        xn=x**n
        xn1=x**n1
        xn2=x**n2
    elif n2>=1:
        xdn=x**dn
        xdn1=x**dn1
        xdn2=x**dn2
        xn=x**n
        xn1=x**n1
        xn2=x**n2
    elif n2==0:
        xdn=x**dn
        xdn1=x**dn1
        xdn2=x**dn2
        xn=x**n
        xn1=x**n1
#Formel for Newtons metoden
    N = x-(a*xn+b*xn1+c*xn2)/(da*xdn+db*xdn1+dc*xdn2)

    print(N)
    
    x=N
