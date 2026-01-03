try:
    file = open("sample.txt", "r")
    print("Reading file content:")
    
    line_no = 1
    for line in file:
        print(f"Line {line_no}: {line.strip()}")
        line_no += 1

    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

 # Task 2: Write and Append Data to a File
# Writing data to file
text = input("Enter text to write to the file: ")

file = open("output.txt", "w")
file.write(text + "\n")
file.close()

print("Data successfully written to output.txt")

# Appending data
append_text = input("Enter additional text to append: ")

file = open("output.txt", "a")
file.write(append_text + "\n")
file.close()

print("Data successfully appended.")

# Reading final content
print("\nFinal content of output.txt:")
file = open("output.txt", "r")
print(file.read())
file.close()
