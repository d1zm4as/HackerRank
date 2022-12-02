int main() {
    char *s[]={"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int a, b,i;
    scanf("%d\n%d", &a, &b);
  	for (int i=a; i<=b; i++) {
        if (i>=1 && i<=9) {
            printf("%s\n", s[i]);
        }
        else if(i%2 == 0) {
            printf("even\n");
        }
        else {
            printf("odd\n");
        }
    }

    return 0;
}
