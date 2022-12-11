# R이 출구를 찾을 거임
# 최소한의 방법으로 출구 찾는 것 -> BFS

# idea
# 막히지 않은 곳으로 가는데 /// 왔던 방향만 제외
# 위치로 구분해도 될듯

# python List에 대해 제대로 알아보는 시간...

from collections import deque
import copy


rx, ry, bx, by = 0, 0, 0, 0
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dirx, diry = [1, -1, 0, 0], [0, 0, 1, -1]
queue = deque()

for i in range(1, n):
	for j in range(1, m):
		if board[i][j] == 'R':
			rx, ry = i, j
		elif board[i][j] == 'B':
			bx, by = i, j

visited = []

def move_ball(info_a, dirx, diry):			# 더 긴 거리로 위치 재조정 해주는 알고리즘이 더 나은듯
	if info_a[0][0] + dirx == info_a[1][0] and info_a[0][1] + diry == info_a[1][1]:
		while board[info_a[1][0] + dirx][info_a[1][1] + diry] != '#':
			if board[info_a[1][0] + dirx][info_a[1][1] + diry] == 'O':
				return -1
			info_a[1][0] += dirx
			info_a[1][1] += diry
		while board[info_a[0][0] + dirx][info_a[0][1] + diry] != '#' and [info_a[0][0] + dirx, info_a[0][1] + diry] != info_a[1]:
			info_a[0][0] += dirx
			info_a[0][1] += diry
		return 1
	else:
		while board[info_a[0][0] + dirx][info_a[0][1] + diry] != '#':
			if board[info_a[0][0] + dirx][info_a[0][1] + diry] == 'O':
				info_a[0][0] = 'O'
				break
			if info_a[1] == [info_a[0][0] + dirx, info_a[0][1] + diry]:
				move_ball(info_a, dirx, diry)
				return 1
			info_a[0][0] += dirx
			info_a[0][1] += diry
		while board[info_a[1][0] + dirx][info_a[1][1] + diry] != '#' and info_a[0] != [info_a[1][0] + dirx, info_a[1][1] + diry]:
			if board[info_a[1][0] + dirx][info_a[1][1] + diry] == 'O':
				info_a[1][0] = 'O'
				break
			info_a[1][0] += dirx
			info_a[1][1] += diry
		return 1

def find_dir(info):		# move ball에서 info 값을 바꿔서 여기서 영향이 미침?
	for i in range(4):
		info_a = copy.deepcopy(info)
		if dirx[i] == info[2][0] * -1 and diry[i] == info[2][1] * -1:
			continue
		#print(dirx[i], diry[i])
		a = move_ball(info_a, dirx[i], diry[i])
		if  a == -1:		# R이 B로 인해 #이 아니어서 움직이는 걸 제거해줌
			#print(info_a[0], info[0])
			continue
		#print(info_a[0], info[0])
		queue.append([info_a[0], info_a[1], [dirx[i], diry[i]], info[3] + 1])

def find_route():
	queue.append([[rx, ry],[bx, by], [0, 0],0])

	while queue:
		#print(visited)
		#print(queue, end = '\n\n')
		info = queue.popleft()
		if info[0][0] == 'O' and info[1][0] != 'O':
			return info[3]
		if info[1][0] == 'O' or info[3] == 10:
			continue
		if [info[0][0], info[0][1], info[1][0], info[1][1]] not in visited:
			visited.append([info[0][0], info[0][1], info[1][0], info[1][1]])
		else:
			continue
		find_dir(info)
	return -1

print(find_route())
""" 
10 10
##########
#.BR.....#
#.#####..#
#.#...#..#
#.#.#.O..#
#.#.#....#
#.#....#.#
#.#..#...#
#.#......#
##########

10 10
##########
#.......O#
#.##....B#
#.#......#
#.#......#
#.#......#
#.#...#.R#
#.#.##...#
#.#......#
##########
"""