int main() 
{
    char ch,s[50],sen[100];
    
    scanf("%c",&ch);
    scanf("%s\n",&s);
    scanf("%[^\n]%s",&sen);
    
    printf("%c\n",ch);
    printf("%s\n",s);
    printf("%s",sen);
          
    return 0;
}
