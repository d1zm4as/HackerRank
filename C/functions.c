int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

int max_of_four(int a,int b,int c,int d){
    int valores[4] = {a,b,c,d};
    int i;
    int maior =  0; 
    
    for(i = 0;i<=4;i++){
        if(valores[i]>maior){
            maior = valores[i];
        }
    }
    
    return maior;
}
