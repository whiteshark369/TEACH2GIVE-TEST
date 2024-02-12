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


# Initialize the first two numbers of the Fibonacci sequence
x, y = 0, 1

# keep on generating the numbers while the last number generated is less than or equal to 100
while y <= 100:
    # Print the current number
    print(y)
    
    # Update the values of x and y to generate the next Fibonacci number
    x, y = y, x + y


    
