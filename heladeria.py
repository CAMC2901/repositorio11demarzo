sum_vainilla=0
sum_fresa=0
sum_choco=0
for i in range(5):
    sabor=int(input("que sabor quiere: 1. vainilla, 2. fresa , 3. chocolate: "))
    if sabor==1:
        sum_vainilla+=1
    elif sabor== 2:
        sum_fresa+=1
    elif sabor== 3:
        sum_choco+=1
print(f"vainilla: {sum_vainilla},fresa: {sum_fresa}, chocolate: {sum_choco}")
