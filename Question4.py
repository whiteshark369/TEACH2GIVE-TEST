# Question 4: Capitalize Words.Write a program that accepts a string as input, capitalizes the first letter of each word in the string, and then returns the result string.Examples:"hi"=> returns "Hi","i love programming"=> returns "I Love Programming"

# Program to capitalize the first letter of each word in a string

# Get the input string
input_string = input("Please enter a string: ")

# Split the string into words
words_list = input_string.split()

# Iterate through each word, capitalizing the first letter
capitalized_words = [word.capitalize() for word in words_list]

# Join the words back together into a single string
result_string = " ".join(capitalized_words)

# Print the resulting string
print("Result string: ", result_string)
