import math
import re

# Exercise 1:
# Define a function called add_numbers that takes two parameters a and b, and returns the sum of a and b.
def add_numbers(a, b):
    return a + b;


#Exercise 2:
# Define a function called calculate_area_circle that takes one parameter radius 
# (which represents the radius of a circle) and returns the area of the circle. 
# The formula to calculate the area of a circle is: area = π * radius^2
def calculate_area_circle(radius):
    return math.pi * (radius ** 2)


# Exercise 3:
# Define a function called is_even that takes one parameter number and returns True if the number is even, and False otherwise.
def is_even(number):
    return number % 2 == 0


# Exercise 4:
# Define a function called maximum_of_three that takes three parameters a, b, and c, and returns the maximum of the three numbers.
def maximum_of_three(a, b, c):
    return max(a, b, c)

# Exercise 5:
# Define a function called calculate_factorial that takes one parameter n (a non-negative integer) and returns the factorial of n. 
# The factorial of a non-negative integer n, denoted as n!, is the product of all positive integers less than or equal to n.
def calculate_factorial(n):
    number = 0;
    for i in range(n):
        number *= i;
    return number

# Exercise 6:
# Define a function called reverse_string that takes one parameter s (a string) and returns the reverse of the input string.
def reverse_string(string):
    return string[::-1]


# Exercise 7:
# Define a function called is_palindrome that takes one parameter s (a string) 
# and returns True if the input string is a palindrome, and False otherwise.
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, 
# ignoring spaces, punctuation, and capitalization.
def is_palindrome(string):
    reversed_string = re.sub("[^a-z]", "", string[::-1].lower())
    return re.sub("[^a-z]", "", string) == reversed_string

# Exercise 8:
# Define a function called count_vowels that takes one parameter s (a string) and returns the number of vowels 
# (i.e., 'a', 'e', 'i', 'o', 'u') in the input string. Ignore case sensitivity when counting vowels.
def count_vowels(string):
    count = 0
    vowels = "aeiouy"
    for char in string.lower():
        if char in vowels:
            count += 1
    return count
