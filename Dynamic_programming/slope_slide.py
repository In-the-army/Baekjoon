# DP로 해보자
# 재귀로 쭉 가면 될거 같은데
# DFS 사용

# 1. 작은 값으로 간다
# 2. 오른쪽 아래가 목표

# 4가지 방향 - 
# 임의의 점에서 목표 지점까지 가짓수 --> DP 사용한 것
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

M, N = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def find(x, y):

	if x == M - 1 and y == N - 1:
		return 1
	if dp[x][y] != -1:
		return dp[x][y]
	ways = 0
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		if 0 <= nx < M and 0 <= ny < N and maps[nx][ny] < maps[x][y]:
			ways += find(nx, ny)

	dp[x][y] = ways
	return ways


print(find(0,0))


Prob_URL = https://www.acmicpc.net/problem/1520