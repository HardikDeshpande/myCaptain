import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius**2

print("The area of the circle is:", area)


filename = input("Enter a filename: ")

# Split the filename into base name and extension
basename, extension = filename.split(".")

print("The extension of the file is:", extension)
