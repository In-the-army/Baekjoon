#include <iostream>
#include <vector>

using namespace std;

// 짝 찾아보는 함수 (Brute Force)
int find_friend(int k, int n, vector<vector <bool>>& pairs)
{
	int cnt_case = 0;

	// n까지 왔다면 짝을 다 지은 상태!!
	if (k == n - 1)
		return 1;
	// k자신이 짝이 있다면 다음으로 넘기는 과정
	else if (pairs[k][n] == 1){
		cnt_case += find_friend(k + 1, n, pairs);
	}
	else{
		// k 자기 자신이 짝이 있음을 명시
		pairs[k][n] = 1;
		// k + 1부터 n까지 짝을 하나씩 찾아보는 것
		for (int i = k + 1; i < n; i++){
			// i가 짝이 없고, k와 친구라면 짝을 맺는다
			if (pairs[i][n] == 0 && pairs[k][i] == 1 ){
				// i는 짝이 생겼음을 명시
				pairs[i][n] = 1;
				cnt_case += find_friend(k + 1, n, pairs);
				pairs[i][n] = 0;
			}
		}
		pairs[k][n] = 0;
	}
	return cnt_case;
}

int main()
{
	int C, n, m, temp_n;
	int temp1, temp2;
	// vector는 2차원 bool 형으로 선언
	vector <vector <bool>> pairs;

	cin >> C;
	while (C--){
		cin >> n >> m;
		temp_n = n;
		// 학생 수 만큼 할당하며 vector를 n * n 형태로 만들 것이고
		// n+1로 할당하여 n index는 find_friend 함수에서 각 학생이 짝을 맺었는지 판단하는 용도로 사용
		while (temp_n--)
			pairs.push_back(vector<bool>(n + 1, 0));

 		while (m--){
			cin >> temp1 >> temp2;
			pairs[temp1][temp2] = 1;
			pairs[temp2][temp1] = 1;
		}
		cout << find_friend(0, n, pairs) << endl;
		pairs.clear();
	}
	return 0;
}
d
// summary : https://brain-melting.tistory.com/8