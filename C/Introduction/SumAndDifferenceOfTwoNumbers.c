#include <stdio.h>

int main()
{
    int m, n;
    float x, y;

    scanf("%d %d", &m, &n);
    scanf("%f %f", &x, &y);

    printf("%d %d\n", m + n, m - n);

    printf("%.1f %.1f\n", x + y, x - y);

    return 0;
}