def most_frequent(string):
    # Create an empty dictionary to store the frequency of each letter
    frequency = {}

    # Count the frequency of each letter in the string
    for letter in string:
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1

    # Sort the letters based on their frequency in descending order
    sorted_letters = sorted(frequency, key=frequency.get, reverse=True)

    # Print the letters in decreasing order of frequency
    for letter in sorted_letters:
        print(letter, ":", frequency[letter])


# Prompt the user to enter a string
string = input("Enter a string: ")

# Call the most_frequent function with the provided string
most_frequent(string)
