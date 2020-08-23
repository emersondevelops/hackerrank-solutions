#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    char s[100];

    // ^\n stands for taking input until a newline isn't encountered
    // %*c, it reads the newline character and here, the used * indicates that this newline character is discarded
    scanf("%[^\n]%*c", &s);

    printf("Hello, World!\n");
    printf("%s", s);
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */

    return 0;
}