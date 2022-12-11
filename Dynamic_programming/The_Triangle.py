# 정수 삼각형 https://www.acmicpc.net/problem/1932

# Time limit	: 2 sec
# base oper		: 40 mn

# Memory limit  : 128 MB
# list size : 3200 mn

# Range of N : 1 ~ 500
# Time Complexity : O(N^3) down
##############################################################

# Goal : 맨 위층부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때
#        이제까지 선택된 수의 합이 최대가 되는 경로 찾기

# 문제 분석
# 어느 곳에 엄청 큰 값이 존재할 수 있음
# --> 모든 값을 살펴봐야 함?
# 특정 부분까지의 경로를 볼 때 최대합을 가지는 상태들로 보면 좋을 듯
# 특정 부분에서 위 두 경로를 보고 더 큰 값을 가지는 경로를 선택하면 끝일 것 같음.
##############################################################

cnt = int(input())

tri = [list(map(int, input().split())) for _ in range(cnt)]
s = [[tri[0][0]]]

if cnt == 1:
	print(tri[0][0])
else:
	for i in range(1, cnt):
		s.append([])
		for j in range(0, i+1):
			if 0 < j and j < i:
				s[i].append(max(s[i-1][j-1], s[i-1][j]) + tri[i][j])
			elif j == 0:
				s[i].append(s[i-1][0] + tri[i][0])
			elif j == i:
				s[i].append(s[i-1][i-1] + tri[i][i])
	print(max(s[cnt-1]))

# 결론적으로 N(N+1)/2 정도의 연산을 수행했으므로
# 시간 복잡도 O(N^2) 이다.
# 걸린 시간 : 1 hour

