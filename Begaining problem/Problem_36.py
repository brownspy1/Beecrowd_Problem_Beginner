import math

a, b, c = list(map(float, input().split()))
d = (b ** 2) - (4 * a * c)

if d == 0:
    print(-b/(2*a))
elif d < 0 or a == 0:
    print('Impossivel calcular')

else:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print(f'R1 = {r1:.5f}\nR2 = {r2:.5f}')
