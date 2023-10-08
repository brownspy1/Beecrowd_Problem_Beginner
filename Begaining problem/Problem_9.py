name = input()
salary = float(input())
sold = float(input())

recevd = (sold / 100)*15
TOTAL = salary + recevd
print(f'TOTAL = R$ {TOTAL:.2f}')