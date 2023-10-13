# print গুণিতক using for loop
n = int(input())
gunitok = []
for i in range(1, n + 1):
    if n % i == 0:
        gunitok.append(i)
print(f'The factors of the {n} are:{gunitok}')

# printing gunoniok using looping
n = int(input())
hi = []
num = []
for x in range(n):
    ver = n
    num.append(ver)
    if x >= 1:
        break
    for j in range(1, n + 1):
        sonkha = num[x] * j
        hi.append(sonkha)
print(f'{n} ar gunitok : {hi}')
