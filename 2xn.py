# DP
# recursive func : top-down

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def tiles(n):
	if dp[n] != -1:
		return dp[n]
	dp[n] = tiles(n - 2) + tiles(n -1)
	return dp[n]

n = int(input())
dp = [-1 for _ in range(n)]
dp[0] = 1
if n != 1:
	dp[1] = 2

print(tiles(n-1) % 10007)
