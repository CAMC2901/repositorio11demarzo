edad=int(input("ingrese su edad: "))
if edad < 13:
    print("no puede ingresar al gym")
elif edad >=13 and edad<=17:
    print("clase juvenil")
elif edad >=18 and edad<=59:
    print("clase general")
else:
    print("clase senior")