def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from the user
number = int(input("Enter a number: "))

# Calculate the factorial
result = factorial(number)

# Print the result
if result is None:
    print("Error: Factorial is undefined for negative numbers.")
else:
    print(f"The factorial of {number} is {result}.")
