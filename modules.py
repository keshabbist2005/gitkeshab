def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# taking input from user
num = int(input("Enter a number: "))

# calling the function
result = factorial(num)

# printing the output
print(f"Factorial of {num} is: {result}")

#Task 2: Math Module Program (Square root, Log, Sine)
import math

# taking input
num = int(input("Enter a number: "))

# calculations using math module
square_root = math.sqrt(num)
log_value = math.log(num)
sine_value = math.sin(num)

# displaying results
print("Square root:", square_root)
print("Logarithm:", log_value)
print("Sine:", sine_value)
