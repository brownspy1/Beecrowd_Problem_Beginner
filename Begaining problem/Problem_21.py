bdt = float(input())
print('NOTAS:')
note_list = [100, 50, 20, 10, 5, 2]
for i in note_list:
    print(f'{bdt // i:.0f} nota(s) de R$ {i}.00')
    bdt = float(f'{bdt % i:.2f}')
print('MOEDAS:')
coins_list = [1, .50, .25, .10, .05, .01]
for i in coins_list:
    print(f'{int(bdt / i)} moeda(s) de R$ {i:.2f}')
    bdt = bdt % i
    bdt = float(f'{bdt:.2f}')
