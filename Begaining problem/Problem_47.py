# Game Time with Minutes
sh, sm, eh, em = map(int, input().split())

start = sh*60+sm
end = eh*60+em

time = end - start
if time <=0:
    time = time + 24*60
hour = time // 60
minute = time % 60

print(f'O JOGO DUROU {hour} HORA(S) E {minute} MINUTO(S)')
