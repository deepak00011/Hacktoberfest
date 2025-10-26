import java.util.Scanner;

public class SumOfNumbers {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input two numbers from user
        System.out.print("Enter the first number: ");
        int n1 = sc.nextInt();

        System.out.print("Enter the second number: ");
        int n2 = sc.nextInt();

        // Calculate sum
        int sum = n1 + n2;

        // Display result
        System.out.println("The sum of the numbers " + n1 + " and " + n2 + " is: " + sum);

        sc.close();
    }
}
