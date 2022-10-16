# subin move two method
# 1. walking        : after 1 sec, moving X-1 or X+1
# 2. teleportation  : after 1 sec, moving 2*X

# goal : find the fastest time in seconds
# --> using BFS

# cases
# 1. walk           X-1
# 2. walk           X+1
# 3. teleportation  2*X

# 시간초과 뜸
# --> visited를 리스트로 append 함수로 만드니까 오래걸림

from collections import deque

N, K = map(int, input().split())

queue = deque([[N, 0]])
visited = [0]*1000001
visited[N] = 1
def where_brother():

	if N > K:
		return N-K
	while queue:
		pos = queue.popleft()
		if pos[0] == K:
			return pos[1]
		pos[1] += 1
		if pos[0]*2 < 1000001 and not visited[pos[0]*2]:
			queue.append([pos[0]*2, pos[1]])
			visited[pos[0]*2] = 1
		if pos[0] + 1 < 1000001 and not visited[pos[0] + 1]:
			queue.append([pos[0] + 1, pos[1]])
			visited[pos[0] + 1] = 1
		if pos[0] - 1 >= 0  and not visited[pos[0] - 1]:
			queue.append([pos[0] - 1, pos[1]])
			visited[pos[0] - 1] = 1

print(where_brother())