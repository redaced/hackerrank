#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){

    int temp,n,height = -1,res = 0;
    vector<int> candles;

    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> temp;
        if(temp >= height)candles.push_back(height = temp);
    }

    for(int i = 0; i < candles.size(); i++){
        if(candles[i] == height)res++;
    }
    cout << res << endl;
}