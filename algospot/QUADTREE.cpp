#include <iostream>
#include <vector>
#include <string>

using namespace std;

// 문자열로 압축된 그림을 상하로 뒤집은 결과 출력하는 함수
string flip_upside_down(string::iterator& iter)
{
	char head = *iter;

	iter++;
	if (head != 'x')
		// string으로 char 1크기 만큼 복사
		return string(1, head);
	// 각 위치를 순회
	string left_up = flip_upside_down(iter);
	string right_up = flip_upside_down(iter);
	string left_down = flip_upside_down(iter);
	string right_down = flip_upside_down(iter);

	return "x" + left_down + right_down + left_up + right_up;
}

int main()
{
	int C;
	string press;
	string::iterator iter;

	cin >> C;
	while (C--){
		cin >> press;
		iter = press.begin();
		string result = flip_upside_down(iter);
		cout << result << endl;
	}
}
