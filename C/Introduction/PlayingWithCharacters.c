#include <stdio.h>

int main()
{
    char ch;
    char s[100];
    char sen[100];

    scanf("%c%*c", &ch);
    scanf("%[^\n]%*c", &s);
    scanf("%[^\n]%*c", &sen);

    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sen);

    return 0;
}
