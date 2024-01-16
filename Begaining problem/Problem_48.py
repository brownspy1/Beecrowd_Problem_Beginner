#Salary Increase
Taka = float(input(""))

if 0<=Taka<=400.00:
    parcent = Taka/100*15
    salary = Taka+parcent
    rate = 15
    print(f'Novo salario: {salary:.2f}\nReajuste ganho: {parcent:.2f}\nEm percentual: {rate} %')
elif 400.01<=Taka<=800.00:
    parcent = Taka / 100 * 12
    salary = Taka + parcent
    rate = 12
    print(f'Novo salario: {salary:.2f}\nReajuste ganho: {parcent:.2f}\nEm percentual: {rate} %')
elif 800.01<=Taka<=1200.00:
    parcent = Taka / 100 * 10
    salary = Taka + parcent
    rate = 10
    print(f'Novo salario: {salary:.2f}\nReajuste ganho: {parcent:.2f}\nEm percentual: {rate} %')
elif 1200.01<=Taka<=20000.00:
    parcent = Taka / 100 * 7
    salary = Taka + parcent
    rate = 7
    print(f'Novo salario: {salary:.2f}\nReajuste ganho: {parcent:.2f}\nEm percentual: {rate} %')
else:
    parcent = Taka / 100 * 4
    salary = Taka + parcent
    rate = 4
    print(f'Novo salario: {salary:.2f}\nReajuste ganho: {parcent:.2f}\nEm percentual: {rate} %')

