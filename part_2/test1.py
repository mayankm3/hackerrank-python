# with open('test1.txt') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(lines)

# Open the file in read mode
with open('test1.txt', 'r') as file:
    # Read line by line
    for line in file:
        print("||"+line.strip()+"^")  # Remove newline characters