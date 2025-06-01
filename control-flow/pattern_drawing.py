# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop: handle rows using while loop
while row < size:
    # Inner loop: handle columns using for loop
    for col in range(size):
        print("*", end="")  # Print star without newline
    print()  # Move to next line after each row
    row += 1
