# DP 안 씀

N = int(input())

if (not(N % 5)):
	print(N // 5)
elif (N % 5 == 1):
	print(N // 5 + 1)
elif (N % 5 == 2):
	if (N == 7):
		print(-1)
	else:
		print(N // 5 + 2)
elif (N % 5 == 3):
	print(N // 5 + 1)
else :
	if (N == 4):
		print(-1)
	else:
		print(N // 5 + 2)
