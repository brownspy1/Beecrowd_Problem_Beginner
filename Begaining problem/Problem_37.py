
value = float(input())
if 0 <= value <= 25:
    print('Intervalo [0,25]')
elif 25 <= value <= 50:
    print('Intervalo (25,50]')
elif 50 <= value <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')

'''Wrong code '''
# value = float(input())
# if 0 < value <= 25:
#     print('Intervalo [0,25]')
# elif 25.0 > value <= 50:
#     print('Intervalo (25,50]')
# elif 50 > value <= 100:
#     print('Intervalo (75,100]')
# elif value < 0:
#     print('Fora de intervalo')
