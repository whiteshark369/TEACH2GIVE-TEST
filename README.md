# pyhton programing language
# Question 1: FizzBuzz Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Question 2: Fibonacci Sequence.Write a program to generate the Fibonacci sequence up to 100.


# Initialize the first two numbers of the sequence
x, y = 0, 1

# keep on generating the numbers while the last number generated is less than or equal to 100
while y <= 100:
    # Print the current number
    print(y)
    
    # Update the values of x and y to generate the next Fibonacci number
    x, y = y, x + y

# Question 3: Power of Two.Write a program that takes an integer as input and returns true if the input is a power of two.Examples:8=> returns true 6=> returns false  

# Program to check if an input integer is a power of two

# Get the integer from the user
number = int(input("Enter an integer: "))

# Check if the number is a power of two
if (number != 0) and (number & (number - 1)) == 0:
    print(f"{number} True")
else:
    print(f"{number} False")


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

# Question 5: Reverse Integer.Write a program that takes an integer as input and returns an integer with reversed digit ordering.Examples:For input 500, the program should return 5.For input -56, the program should return -65.For input -90, the program should return -9.For input 91, the program should return 19.

# Program to reverse the digits in an integer

# Get the integer from the user
number = int(input("Please enter an integer: "))

# Initialize the reversed number as 0
reversed_number = 0

# Loop until the original number is zero
while number != 0:
    # Get the last digit of the number
    digit = number % 10

    # Reverse the digits by adding the last digit to the reversed number
    reversed_number = reversed_number * 10 + digit

    # Remove the last digit from the number
    number = number // 10

# Print the reversed number
print("Reversed integer: ", reversed_number)

# Question 6: Count Vowels.Write a program that counts the number of vowels in a sentence. eg " Hello World " => returns 2

# Program to count the number of vowels in a sentence

# Get the sentence from the user
sentence = input("Enter a sentence: ")

# Define the set of vowels
vowels = "aeiouAEIOU"

# Initialize the count of vowels
vowel_count = 0

# Iterate through each character in the sentence
for char in sentence:
    # If the character is a vowel, increment the count
    if char in vowels:
        vowel_count += 1

# Print the total number of vowels
print("Number of vowels in the sentence: ", vowel_count)





    


    
