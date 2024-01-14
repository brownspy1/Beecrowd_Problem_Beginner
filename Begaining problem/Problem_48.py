#Salary Increase
Taka = float(input(""))
if 0<=Taka<=400.00:
    print('salario: 460.00 Reajuste ganho: 60.00')

    percentual: 15 %
    rate = 15
elif 400.01<=Taka<=800.00:
    rate = 12
elif 800.01<=Taka<=1200.00:
    rate = 10
elif 1200.01<=Taka<=20000.00:
    rate = 7
else:
    rate = 4
