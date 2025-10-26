import java.util.Scanner;
import java.util.Arrays;

public class CheckPairSum {

    // Function to check if a pair exists with sum equal to x
    static boolean chkPair(int[] A, int size, int x) {
        for (int i = 0; i < size - 1; i++) {
            for (int j = i + 1; j < size; j++) {
                if (A[i] + A[j] == x) {
                    return true; // Pair found
                }
            }
        }
        return false; // Pair not found
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // User input for array size
        System.out.print("Enter the number of elements: ");
        int size = sc.nextInt();
        int[] A = new int[size];

        // Input array elements
        System.out.println("Enter " + size + " elements:");
        for (int i = 0; i < size; i++) {
            A[i] = sc.nextInt();
        }

        // Input target sum
        System.out.print("Enter target sum: ");
        int x = sc.nextInt();

        System.out.println("Array: " + Arrays.toString(A));
        System.out.println("Target sum: " + x);

        // Check if pair exists
        if (chkPair(A, size, x)) {
            System.out.println("Yes, a pair with the given sum exists.");
        } else {
            System.out.println("No, no pair with the given sum exists.");
        }

        sc.close();
    }
}
