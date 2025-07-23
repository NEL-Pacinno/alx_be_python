def print_multiplication_table(number):
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Get user input
num = int(input("Enter a number to see its multiplication table: "))
print_multiplication_table(num)