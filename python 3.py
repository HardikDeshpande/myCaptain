start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Positive numbers in the range", start, "to", end, ":")

for num in range(start, end + 1):
    if num > 0:
        print(num)
