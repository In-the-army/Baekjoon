#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
#define INF 9999

// 스위치와 연결된 시계 목록
const int switch_clock[10][5] = {
	{0, 1, 2, -1, -1},
	{3, 7, 9, 11, -1},
	{4, 10, 14, 15, -1},
	{0, 4, 5, 6, 7},
	{6, 7, 8, 10, 12},
	{0, 2, 14, 15, -1},
	{3, 14, 15, -1, -1},
	{4, 5, 7, 14, 15},
	{1, 2, 3, 4, 5},
	{3, 4, 5, 9, 13}
};

// clock 시간 변경 함수
void change_clock(int clock_num, int cnt, vector <int>& clock)
{
	for (int i = 0; i < 5; i++)
		clock[switch_clock[clock_num][i]] = (clock[switch_clock[clock_num][i]] + (cnt * 3)) % 12;
}

// 완전 탐색을 통한 최소 누르는 횟수 찾는 함수
int least_click(int clock_num, vector <int>& clock)
{
	if (clock_num >= 10)
	{
		for (int i = 0; i < 16; i++)
			// 시계가 12를 가리키고 있는 것을 0으로 표현함.
			if (clock[i] != 0)
				// 하나라도 12를 가리키지 않으면 INF를 보냄.
				return INF;
		return 0;
	}

	// ret을 INF로 설정해놓음.
	int ret = INF;

	// clock 돌리는 횟수, swithch 누르는 횟수를 각 경우마다 체크하는 반복문
	for (int cnt = 0; cnt < 4; cnt++){
		// clock_num 	: clock 번호
		// cnt 			: switch 몇 번 누르는지
		change_clock(clock_num, cnt, clock);
		// 각각의 cnt에 따라 모든 시계가 12인지를 확인하고
		// 맞다면 cnt를 가져옴.
		ret = min(ret, least_click(clock_num + 1, clock) + cnt);
		change_clock(clock_num, (4 - cnt) % 4, clock);
	}
	return ret;
}

int main()
{
	int C, temp;
	vector <int> clock(16);

	cin >> C;
	while (C--){
		for (int i = 0; i < 16; i++)
			cin >> clock[i];
		temp = least_click(0, clock);
		cout << (temp == INF ? -1 : temp) << endl;
	}
}
