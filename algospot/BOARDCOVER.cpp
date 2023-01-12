#include <iostream>
#include <vector>

using namespace std;

// L판을 놓는 4가지의 경우에 대한 흰색 칸의 상대적 위치
// (y, x) 형태
const int dist[4][3][2] = {
	{{0, 0}, {1, 0}, {0, 1}},
	{{0, 0},{0, 1}, {1, 1}},
	{{0, 0},{1, -1}, {1, 0}},
	{{0, 0},{1, 1}, {1, 0}}
};


// 4가지 L판을 놓는 방법이 가능한지 판단
bool check(int type, int alpha, int x, int y, vector <vector <int>>& board)
{
	bool ret = true;

	for (int i = 0; i < 3; ++i){
		const int dx = x + dist[type][i][1];
		const int dy = y + dist[type][i][0];

		// index 벗어났으면 false
		if (dy < 0 || dy >= board.size() || dx < 0 || dx >= board[0].size())
			ret = false;
		// 검은색이면 false
		// 검은색이면 한 칸에 2개가 겹쳐지게 만들었다.
		// 나중에 L판을 뺄 때, 2로 해두지 않으면 1->0이 되어버려 원래 채워진 칸이 비워지기 때문
		else if ((board[dy][dx] += alpha) > 1)
			ret = false;
	}
	return ret;
}

// board 흰색칸 채우는 경우의 수 구하는 함수
int	fill_board(int n, int H, int W, vector <vector<int>>& board)
{
	// n은 0부터 H*W까지 증가하는 수
	// x, y를 가져옴
	const int x = n % W;	// 0 ~ W-1
	const int y = n / W;	// 0 ~ H-1
	int ret = 0;

	// 끝까지 탐색 끝날시 경우의 수를 하나 찾았음!
	if (n >= H * W - 1){
		int result = 1;
		for (int i = 0; i < board.size(); i++)
			for (int j = 0; j < board[0].size(); j++)
				result += board[i][j] - 1;
		return result == 1 ? 1 : 0;
	}
	// 검은색 칸이면 다음 칸으로 넘김
	else if (board[y][x] == 1)
		return fill_board(n + 1, H, W, board);

	// L판을 놓는 4가지 경우 확인
	for (int i = 0; i < 4; i++){
		// 가능하면 다음으로 넘김
		if (check(i, 1, x, y, board))
			ret += fill_board(n + 1, H, W, board);
		// -1을 넘겨 L판을 빼주는 과정
		check(i, -1, x, y, board);
	}
	return ret;
}


int	main()
{
	int		C, H, W, temp;
	char	space;
	vector	<vector<int>> board;

	// 흰색칸 갯수 세는 용도
	// 입력 처리
	cin >> C;
	while (C--){
		cin >> H >> W;
		temp = 0;
		// resize()
		// 2차원 vector로 선언한 board를 H * W로 만들어주는 함수
		board.resize(H, vector<int>(W));
		for (int i = 0; i < H; i++)
			for (int j = 0; j < W; j++){
				cin >> space;
				// '#' : 검은칸이면 1로 board에 저장
				if (space == '#')
					board[i][j] = 1;
				// '.' : 흰칸이면 0로 board에 저장
				else{
					board[i][j] = 0;
					temp++;
				}
			}
		// 만약 흰색 칸이 3의 배수가 아니라면 L판으로 다 덮을 수 없으니
		// 바로 0을 출력
 		if (temp % 3 != 0){
			cout << "0" << endl;
			continue;
		}
		// fill_board() 함수 호출하여, board 채우는 경우의 수 출력
		cout << fill_board(0, H, W, board) << endl;
		// 반드시 clear 한 번 해주기..!
		board.clear();
	}
}
