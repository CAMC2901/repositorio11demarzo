acum=0
acum1=0
acum2=0
for i in range (5):

 nombre=str(input("ingrese su nombre: "))
 dias=int(input("cuantos dias asistio: "))
 minutos=int(input("cuantos minutos promedio entreno al dia: "))
 if dias<3:
  acum+=1
  print("bajo compromiso")
 elif dias>=3 and dias <=4:
  acum1+=1
  print("compromiso medio")
 elif dias>=5 and dias <=7:
  acum2+=1
  print("compromiso alto")
 else:
  print("numero incorrecto")
print(f"categoria 1: {acum}")
print(f"categoria 2: {acum1}")
print(f"categoria 3: {acum2}")