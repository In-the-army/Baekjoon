#       3가지 연산
# 1. X가 3으로 나누어 떨어지면 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.
# 연산 최소 횟수로 X를 1로 만들기
# --> Conversely, increase from 1 to X

# Use as many as possible in the order of 1, 2, 3 - 숫자를 최대한 키우기
# When I finally make X to 1, there are three previous steps.
# 1. plus 1
# 2. multiply 2
# 3. multiply 3

# n(x) = n(x - 1) + 1 or n(x / 2) + 1 or n(x / 3) + 1
# start 1, storing and computing
# Threfore, if n(x) was stored, cut that func
# --> operating less than X times ?

x = int(input())
oper_cnt = [0, 0, 1, 1]

for i in range(4, x+1):
    oper_cnt.append(oper_cnt[i-1]+1)

    if i%2 == 0:
        oper_cnt[i] = min(oper_cnt[i], oper_cnt[i//2]+1)
    if i%3 == 0:
        oper_cnt[i] = min(oper_cnt[i], oper_cnt[i//3]+1)
print(oper_cnt[x])

""" recursive method
def make1toX(n):
    oper_cnt.append(oper_cnt[n - 1] + 1)
    if n >= x:
        return oper_cnt[x]
    if n % 3 == 0:
        oper_cnt[n] = min(oper_cnt[n], oper_cnt[n//3] + 1)
    elif n % 2 == 0:
        oper_cnt[n] = min(oper_cnt[n], oper_cnt[n//2] + 1)
    make1toX(n + 1)
 """



