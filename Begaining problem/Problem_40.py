n1, n2, n3, n4 = list(map(float, input().split()))
ag = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / (2 + 3 + 4 + 1)
print(f'Media: {ag:.1f}')

if ag >= 7.0:
    print('Aluno aprovado.')
elif ag <= 4.9:
    print('Aluno reprovado.')
elif 5.0 <= ag <= 6.9:
    print('Aluno em exame.')
    n5 = float(input())
    print(f'Nota do exame: {n5:.1f}')
    avg = (ag + n5) / 2
    if avg >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {avg:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {avg:.1f}')
