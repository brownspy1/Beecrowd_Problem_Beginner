inpute = input().split()
A = int(inpute[0])
B = int(inpute[1])
C = int(inpute[2])
D = int(inpute[3])

if B > C and D > A and (C + D) > (A + B) and (C > 0) and (D > 0) and A % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
