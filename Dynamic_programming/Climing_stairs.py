# 계단 오르기 https://www.acmicpc.net/problem/2579
# Problem Solving time : 4 hour

# Time limit : 1 sec
# base oper : 2000 million times

# Memory limit : 128 MB
# list size : 3200 million

# Range of N : 1 ~ 300
# Time complexity : O(n^3) down
##############################################################

# Goal : How to get maximum score?

# !dea
# 최대한 점수를 얻으며 n번째 계단에 올랐을 때 가지는 점수 : X(n)
# 1. 연속으로 두 번 오른 상태
# 2. 연속으로 두 번 오르지 않은 상태

# 1의 경우
# X(n) = X(n-1) + (n 계단 점수)

# 2의 경우
# X(n) = X(n-2) + (n 계단 점수)

# 따라서 X(n) = max((1의 경우), (2의 경우))
# X(1) = (1 계단 점수), X(2) = (1, 2 계단 점수 합)
##############################################################

# 구현 과정 (!dea 오류 잡기 및 정교화)
# 위와 같이 진행할 경우 1의 경우에서 막힌다.
# 1의 경우 2번 연속인지 아닌지 판단해야 하는 경우가 발생함.

# 그냥 단순히 
# 1. 2칸 오르지 않았던 X(n-1)에서 1칸 오르는 경우
# --> X(n-3)에서 2칸 올라 n-1번째 계단으로 오른 것으로 생각
# 2. X(n-2)에서 2칸 오르는 경우

# 이렇게 해버리면 X(n)으로 오르는 모든 경우를 생각한 것이 된다.

# 마지막으로 1, 2, 3 계단이 올 경우를 생각해서 예외처리를 해주면 된다.
##############################################################

cnt = int(input())
s = [int(input()) for _ in range(cnt)]

if cnt == 1:
    print(s[0])
elif cnt == 2:
    print(s[1] + s[0])
elif cnt == 3:
    print(max(s[0] + s[2], s[1] + s[2]))
else:
    score = [s[0], s[1] + s[0], max(s[0] + s[2], s[1] + s[2])]
    for i in range(3, cnt):
        score.append(max(score[i-3] + s[i-1], score[i - 2]) + s[i])
    print(score[cnt-1])
