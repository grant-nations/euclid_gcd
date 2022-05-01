def euclid_gcd(a, b):
    if b == 0:
        return a
    else:
        return euclid_gcd(b, a % b)


if __name__ == '__main__':
    print("------------------------------------------------------------")
    print("Calculate the GCD of two values using Euclid's GCD algorithm")
    print("------------------------------------------------------------\n")

    a_input = int(input("Enter the first integer: "))
    b_input = int(input("Enter the second integer: "))
    print(f"\nGCD: {euclid_gcd(a_input, b_input)}\n")

