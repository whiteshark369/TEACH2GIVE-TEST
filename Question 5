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
