int main() {
	int num;
    scanf("%d", &num);
    
    int sum = 0;
   
    while(num != 0){
        sum += num % 10;
        num = num/10;
        
        
    }
    
    printf("%d",sum);
    return 0;
}
