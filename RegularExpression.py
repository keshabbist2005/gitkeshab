# 1. Create a dictionary with student names and their marks
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88
}

# 2. Ask the user to input a student's name
search_name = input("Enter the student's name: ")

# 3 & 4. Retrieve marks and handle cases where the student is not found
if search_name in student_marks:
    marks = student_marks[search_name]
    print(f"{search_name}'s marks: {marks}")
else:
    print("Student not found.")
    #task2: validate email address using regular expression
    # 1. Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Extract the first five elements using slicing [start:stop]
extracted_list = numbers[0:5]

# 3. Reverse the extracted elements using slicing [::-1]
reversed_list = extracted_list[::-1]

# 4. Print the results to match the expected output
print("Original list:", numbers)
print("Extracted first five elements:", extracted_list)
print("Reversed extracted elements:", reversed_list)