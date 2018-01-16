#include <stdio.h>
#include <cmath>

using namespace std;
void update(int *a,int *b) {
    int buffer;
    buffer = *a;
    *a = *a + *b;
    *b= abs(buffer - *b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
