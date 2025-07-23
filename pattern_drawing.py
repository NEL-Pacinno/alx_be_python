pattern = input("Enter the size of the pattern (e.g., *, #, @): ")
rows = int(input("Enter the number of rows: "))

for i in range(rows):
    print(pattern * rows)
