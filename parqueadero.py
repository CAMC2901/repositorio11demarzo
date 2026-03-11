horas=int(input("cuantas horas estuvo: "))
if horas == 1:
    print(" total a pagar es de 5000: ")
elif horas >1:
    horas-=1
    total=(5000)+horas*3000
    print(total)