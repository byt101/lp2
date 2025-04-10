#include <stdio.h>
#include <string.h>

int main(void){
    char str[] = "Hello, World!";
    int i,length;
    length = strlen(str);
    for(i = 0; i < length; i++){
        printf("%c", str[i]&127);
    }
    printf("\n");
    for ( i = 0; i < length; i++)
    {
        printf("%c", str[i]^127);
    }
    printf("\n");
    for ( i = 0; i < length; i++)
    {
        printf("%c", str[i]|127);
    }
    
    
}