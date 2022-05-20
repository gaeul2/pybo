import sys

# N = int(input())
# for _ in range(N):
#     input = sys.stdin.readline().rstrip()
#     A, B = map(int, input.split())
#     print(A+B)

# N = int(input())
#
# for i in range(1, N+1):
#     A, B = map(int, sys.stdin.readline().split())
#     print("Case #"+f'{i}:', f'{A} + {B} =', A+B)

# N, num = map(int,input().split())
# A = list(map(int, input().split()))
# for i in range(N):
#     if A[i] < num:
#         print(A[i], end= " ")

N = num = input()
if len(num) == 1:
    num = "0" + num  # 01
cnt = 0

while True:
    plus = str(int(num[0]) + int(num[1]))
    plus = plus[-1]
    num = num[-1] + plus  # str
    cnt += 1
    if N == num:
        print(cnt)
        break



