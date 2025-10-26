#include <stdio.h>

// Function to check if a pair exists with sum equal to x
int chkPair(int A[], int size, int x) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = i + 1; j < size; j++) {
            if (A[i] + A[j] == x) {
                return 1; // Pair found
            }
        }
    }
    return 0; // Pair not found
}

int main(void) {
    int A[] = {0, -1, 2, -3, 1};
    int x = -2;
    int size = sizeof(A) / sizeof(A[0]);

    printf("Array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", A[i]);
    }
    printf("\nTarget sum: %d\n", x);

    if (chkPair(A, size, x)) {
        printf("Yes, a pair with the given sum exists.\n");
    } else {
        printf("No, no pair with the given sum exists.\n");
    }

    return 0;
}
