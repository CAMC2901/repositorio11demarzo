clase=int(input("clases asistidas al mes: "))
if clase < 5:
    print("asitencia baja")
elif clase>=5 and clase<=8:
    print("asitencia media")
elif clase>=9:
    print("asistencia alta")