taka = int(input())
print(taka)
note = [100, 50, 20, 10, 5, 2, 1]
for i in note:
    print(f'{taka // i} nota(s) de R$ {i},00')
    taka = taka % i
