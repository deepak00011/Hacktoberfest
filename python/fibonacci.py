def fibonacci_sequence(nterms):
    # Check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer.")
    # If there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence up to", nterms, ":")
        print(0)
    # Generate the Fibonacci sequence
    else:
        print("Fibonacci sequence:")
        n1, n2 = 0, 1
        count = 0
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1, n2 = n2, nth
            count += 1

def main():
    nterms = int(input("How many terms? "))
    fibonacci_sequence(nterms)

if __name__ == "__main__":
    main()
