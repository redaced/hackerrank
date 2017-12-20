#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int a = 5;
    long arr[5]; 
    for (int i = 0; i < a; i ++){
        cin >> arr[i];   
    }
    sort(arr,arr + a );
    long min = 0;
    for (int i = 0; i < a - 1; i ++){
        min = min + arr[i];
    }
    long max = 0;
    for (int i = 1; i < a; i ++){
        max = max + arr[i];
    }
    cout << min << " " << max;
    return 0;
}
