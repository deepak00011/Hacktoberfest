#include <stdio.h>

int main() {
    int n, i, flag = 0;
    
    printf("Enter a positive integer: ");
    scanf("%d", &n);

    if (n <= 1) {
        flag = 1; // 0 and 1 are not prime
    }

    for (i = 2; i <= n / 2; ++i) {
        if (n % i == 0) {
            flag = 1; // divisible => not prime
            break;
        }
    }

    if (flag == 0)
        printf("%d is a prime number.\n", n);
    else
        printf("%d is not a prime number.\n", n);

    return 0;
}
