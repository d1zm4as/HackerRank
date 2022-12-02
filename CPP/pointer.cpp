#include <stdio.h>
#include <cstdlib>
#include <iostream>

void update(int *pa,int *pb) {
        int soma = *pa+*pb;
        int diff = abs(*pa-*pb);
        printf("%d\n%d", soma, diff);
        
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    
    

    return 0;
}
