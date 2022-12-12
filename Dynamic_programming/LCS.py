# Longest Common Subsequence https://www.acmicpc.net/problem/9251
# LCS 이해하기 https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwj98oGlkfT7AhVOG4gKHfxvCzgQFnoECA4QAQ&url=https%3A%2F%2Fvelog.io%2F%40emplam27%2F%25EC%2595%258C%25EA%25B3%25A0%25EB%25A6%25AC%25EC%25A6%2598-%25EA%25B7%25B8%25EB%25A6%25BC%25EC%259C%25BC%25EB%25A1%259C-%25EC%2595%258C%25EC%2595%2584%25EB%25B3%25B4%25EB%258A%2594-LCS-%25EC%2595%258C%25EA%25B3%25A0%25EB%25A6%25AC%25EC%25A6%2598-Longest-Common-Substring%25EC%2599%2580-Longest-Common-Subsequence&usg=AOvVaw3ajptW_F6CTvvgt4Wr7rd9

# Time limit    : 2 sec
# Memory limit  : 256 MB

# Range of N : 1000
# Time Complexity : O(N^2) or less
##############################################################

str_1 = input()
str_2 = input()

len_1 = len(str_1)
len_2 = len(str_2)

LCS = [[0] * (len_1 + 1) for _ in range(len_2 + 1)]

for i in range(1, len_2 + 1):
	for j in range(1, len_1 + 1):
		if str_1[j - 1] == str_2[i - 1]:
			LCS[i][j] = LCS[i-1][j-1] + 1
		else:
			LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
print(LCS[len_2][len_1])

# O(N^2) 시간 복잡도를 가짐