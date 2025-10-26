#include <stdio.h>

int main() {
    int rows, cols, i, j, count = 0;
    int matrix[10][10];

    // Input matrix dimensions
    printf("Enter the number of rows and columns: ");
    scanf("%d%d", &rows, &cols);

    // Input matrix elements
    printf("Enter the elements of the matrix:\n");
    for(i = 0; i < rows; i++) {
        for(j = 0; j < cols; j++) {
            printf("Element at [%d][%d]: ", i, j);
            scanf("%d", &matrix[i][j]);
        }
    }

    // Display the matrix
    printf("\nThe matrix is:\n");
    for(i = 0; i < rows; i++) {
        for(j = 0; j < cols; j++) {
            printf("%d\t", matrix[i][j]);
        }
        printf("\n");
    }

    // Count zero elements
    for(i = 0; i < rows; i++) {
        for(j = 0; j < cols; j++) {
            if(matrix[i][j] == 0) {
                count++;
            }
        }
    }

    // Check if the matrix is sparse
    if(count > (rows * cols) / 2) {
        printf("\nThe matrix is a sparse matrix.\n");
    } else {
        printf("\nThe matrix is not a sparse matrix.\n");
    }

    return 0;
}
