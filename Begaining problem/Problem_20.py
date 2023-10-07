#Age in Days
age = int(input())


year = age//365
munth = (age%365)//30
day = (age%365)%30

print(f'{year} ano(s)\n{munth} mes(es)\n{day} dia(s)')