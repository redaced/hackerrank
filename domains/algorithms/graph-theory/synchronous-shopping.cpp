#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int n,m,k;
	cin >> n >> m >>k;
	int a[n][2];
	for (int i = 0;i < n; i ++){
		cin >> a [i][0] >> a[i][1];
	}
	int mapi[m][3];
	for (int i = 0;i < m; i ++){
		cin >> mapi[i][0] >> mapi[i][1] >> mapi[i][2];
	}
	int graph_array[m][m];
	for (int i = 0;i < m; i ++){
		graph_array[mapi[i][0]-1][mapi[i][1]-1] = mapi[i][2];
		for (int j = 0;j < m; j ++){
			graph_array[i][j] = -1;
			if(i == j){
				graph_array[i][j] = 0;
			}
		}
	}
	int count = 0;
	int point_x = 0;
	while(true){
		for (int i = 0;i < m; i ++){
			cout << "=" << graph_array[point_x][i] << endl;
			if(graph_array[point_x][i] > 0){
				point_x = i;
				count+=graph_array[point_x][i];
				break;
			}
		}
	}
	cout << count << endl;
	// for (int i = 0;i < m; i ++){
	// 	for (int j = 0;j < m; j ++){
	// 		cout <<	graph_array[i][j] << "  ";	
	// 	}
	// 	cout << endl;
	// }
	return 0;
}
