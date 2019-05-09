#Variables, Numbers, Printing & Comments in Python

a = 1
b = 2
c = 3

my_sum = a + b
another_sum = 5 + 10

"""
- Letters, Numbers & Underscores
- Cannot start variables w/ a number
- Compound words have an underscore & lowercased

- Variables can be called anything you like, although there are a few reserved keywords
- And a few other names you should avoid.
- Reserved keywords are those that are part of the language.
- Words you should avoid are those which they themselves are variables.

- In Python we normally use "snake_case" for names. Other languages use "camelCase".
- If you want your code to look more like Python code, use "snake_case"!
"""

math_operators = 1 + 3 * 4 / 2 - 2 #5
print(math_operators)

float_division = 12 / 3
print(float_division)

"""
Python converts integers(whole #s) into floating point #s every time you use the divide operator
"""

integer_division = 12 // 3
print(integer_division)

"""
When you want Python to perform a division & return integers(whole #s), then you use 2 division signs '//' as shown above (it drops the decimal point).
"""

division_with_remainder = 12 // 5 #should be 2.4
print(division_with_remainder)

"""
When we divide an integer w/ a remainder, it gets 'rounded down or up' & Pythong gives you an integer back, NOT a floating point #.
"""
# 5 goes into 12 two times. (5 * 2 is 10). The reminder is 2.
# Getting the reminder of a division is such a popular operation, that Python gives us a way to do it really easily.

remainder = 12 % 5 # prints 2
print(remainder)


# Why is it so popular?
# What would the reminder be in these divisions?
#
# 10 / 2 - prints 0
# 14 / 2 - prints 0
# 6 / 2 - prints 0
# 340 / 2 - prints 0
#
# What about these?
#
# 11 / 2 - prints 1
# 27 / 2 - prints 1
# 3 / 2 - prints 1


# For every even number, the reminder when divided by 2 is always 0.
# For every odd number, the reminder when divided by 2 is always 1.

# We can check whether a number is odd or even just by checking the reminder!


x = 37
reminder = x % 2
print(reminder)  # should print 1, therefore it is odd


"""
When you want to get a reminder back of an integer, we use the MODULUS Operator '%'

The Modulus Operator also helps us to check if two integers have an ODD or EVEN remainder.

When the Modulus of two integers is ODD - it always returns 1

When the Modulus of two integers is EVEN - it always returns 0
"""


#QUIZ

"""
Question 1:
What would the value of x  be at the end of this segment?
"""
a = 17.5
b = 5
x = a + b - 9
print(x) # 13.5


"""
Question 2:
What would the value of div  be at the end of this segment?
"""
my_variable = 7
div = my_variable / 2
print(div) # 3.5


"""
Question 3:
What would the output be (i.e. what would the user see) from this code sample?
"""
friends = 9
near = 3
friends_away = friends - near
print(friends_away) # 6


"""
Question 4:
Which of these two is correct in Python 3? (that is the version the videos are using)
"""
#1: print('Hello, world!')
#Correct Ans- Whenever we us print, we must include WHAT we want to print inside the brackets.

#Or

#2: print 'Hello, world!' Wrong ans- No brackets

"""
Question 5:
What would the user see as output after this code segment?
"""
row_number = 235
result = row_number % 2
print(result) # 1 - Odd Number/Integer


#Exercise: Variables & Numbers

"""
1. Create two variables, var1 and var2, both with the same value.
"""
var1 = 2
var2 = 2

"""
2. Create two variables, num1 and num2, the multiply together to give 16.
"""
num1 = 2
num2 = 8

print(num1 * num2)
