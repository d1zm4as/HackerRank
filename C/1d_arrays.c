int main() {
    int n,i,lol;
    int soma = 0;
    scanf("%d",&n);
    int *arr = (int*)malloc(n * sizeof(int));
    for(i =0; i<n;i++){
        scanf("%d",&lol);
        arr[i]=lol;
    
    }  
    for(i=0;i<n;i++){
        soma+= arr[i];
        
        
    }
    free(arr);
    printf("%d",soma);
    return 0;
}
