# Take input from user
num = int(input("Enter a number: "))

# Check even or odd
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
    
#task2:create a personalize greeting
# Initialize sum
total = 0

# Loop from 1 to 50
for i in range(1, 51):
    total += i

# Display result
print("The sum of numbers from 1 to 50 is:", total)
