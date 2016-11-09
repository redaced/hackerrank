#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
int main(){
	int n;
	cin >> n;
	vector<int> v;
	queue<int> q;
	int stack;
	int q1,q2,q3;
	for (int i = 0; i < n; ++i){
		cin >> stack;
		v.push_back(stack);
	}
	cin >> q1;
    cin >> q2;
    cin >> q3;

    v.erase(v.begin() + (q1 - 1));
	v.erase(v.begin() + (q2 - 1), v.begin() + (q3 - 1));
	cout << v.size() << endl;
	for (vector<int>::iterator i = v.begin(); i != v.end(); ++i){
		cout << *i << " ";
	}
	return 0;
}