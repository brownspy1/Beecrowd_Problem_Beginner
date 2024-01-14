# Game Time
a, b = list(map(int, input().split()))
if a<b:
    total = b-a
    print(f'O JOGO DUROU {total} HORA(S)')
else:
    total = b+24-a
    print(f'O JOGO DUROU {total} HORA(S)')