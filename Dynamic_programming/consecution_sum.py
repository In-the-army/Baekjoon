# sequence
# select several consecutive nums and find the largest sum
# x(n) : the largest sum from 0 to n

# cases
# 가장 큰 양수 양 옆의 음수에 다음 양수들을 더할 때 값이 높아질 것인가
# 

# idea
# 가장 큰 값을 저장하며 살펴봄
# --> 음수는 자기 앞의 양수들의 합에 자기 자신을 더해 저장
# --> 다음 양수들은 전에 양, 음수들을 더하면 값이 커질지 판단 가능

import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

for i in range(1, n):
    seq[i] = max(seq[i], seq[i-1]+seq[i])
print(max(seq))
