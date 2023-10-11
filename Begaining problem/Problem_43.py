a, b, c = list(map(float, input().split()))
if a + b > c and b + c > a and a + c > b:
    Perimetro = a + b + c
    print(f'Perimetro = {Perimetro:.1f}')
else:
    Area = 1 / 2 * (a + b) * c
    print(f'Area = {Area:.1f}')
