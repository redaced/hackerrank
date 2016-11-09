#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
struct myclass {
  bool operator() (int i,int j) { return (i<j);}
} myobject;
int main(){
	int n;
	cin >> n; 
	vector<int> table;
	for (int i = 0; i < n; ++i)
	{
		int stack;
		cin >> stack;
		table.push_back(stack);
	}
	sort (table.begin(), table.end(), myobject);
	for (vector<int>::iterator i = table.begin(); i != table.end(); ++i)
	{
		cout << *i << " ";
	}
	return 0;
}