# def cal(a, b, c):
#     if a > b and a > c:
#         print(f'{a} eh o maior')
#     elif b > a and b > c:
#         print(f'{b} eh o maior')
#     else:
#         print(f'{c} eh o maior')
#
#
# D = list(map(int, input().split()))
# A, B, C = D[0], D[1], D[2]
# cal(A, B, C)

# Accepted way
A = list(map(int, input().split()))
MAX = max(A)
print(f'{MAX} eh o maior')