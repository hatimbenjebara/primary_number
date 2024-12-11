def checkPrime(i):
    if i <= 1:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True

def findPrimesInRange(start, end):
    primes = []
    for num in range(start, end + 1):
        if checkPrime(num):
            primes.append(num)
    return primes

# Main program
print("Do you want to:")
print("a. Check if a number is prime.")
print("b. Find all prime numbers in a range.")
choice = input("Enter a or b: ").strip()

if choice == 'a':  # Option to check a single number
    print("Enter a number to check if it is prime:")
    try:
        a = int(input())
        if checkPrime(a):
            print(f"{a} is a prime number.")
        else:
            print(f"{a} is not a prime number.")
    except ValueError:
        print("Invalid input! Please enter an integer.")
elif choice == 'b':  # Option to find prime numbers in a range
    print("Enter the start of the range:")
    try:
        start = int(input())
        print("Enter the end of the range:")
        end = int(input())
        if start > end:
            print("Invalid range! Start should be less than or equal to end.")
        else:
            primes = findPrimesInRange(start, end)
            print(f"Primes in the range {start} to {end}: {primes}")
    except ValueError:
        print("Invalid input! Please enter valid integers for the range.")
else:
    print("Invalid choice. Please restart the program and enter 1 or 2.")
