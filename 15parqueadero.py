carro=4000
moto=2000
acum_carro=0
acum_moto=0
recaudo_carro=0
recaudo_moto=0
mayor_pago=0
placa_mayor_pago=""
for i in range(8):
    placa=input("ingrese su placa: ")
    tipo=int(input("1. carro, 2. moto: "))
    horas=int(input("horas de parqueo: "))
    if tipo == 1:
        acum_carro+=1
        total=horas*carro
        recaudo_carro+=total
        print(total)
    else:
        acum_moto+=1
        total=horas*moto
        recaudo_moto+=total
        print(total)
    if total > mayor_pago:
     mayor_pago = total
     placa_mayor_pago = placa
print("el total recaudado es: ", recaudo_carro + recaudo_moto)
print("el total recaudado por carros es: ", recaudo_carro)
print("el total recaudado por motos es: ", recaudo_moto)
print("la placa del vehiculo que mas pago es: ", placa_mayor_pago, "con un pago de: ", mayor_pago)




