
#Getting User Input in Python

"""
- We use input() function to present the user with a prompt.
- They can then type, & when they press Enter everything they typed gets returned.
- We can capture their response by assign it to a variable.
"""

#Maths with user input
"""
- All the user input that we get via the input() function is a string.
- That means we can't do maths on it, unless we convert it to a number first.
"""


my_name = 'CoderJoh'
users_name = input('What is your name? ')

#print('Hey there ' + my_name) # This is correct, but not necessarily proffered way to format strings.

#print(f'Good day to you {users_name}') # This is the preferred way, using F-String to format strings.


"""
We DON'T using strings to do math, ths is why we end up with the wrong ans on this instance.
"""
#age = input('How young are you? ')

#print(f'You have lived for {age * 12} months!')


"""
Since we changed the age variable we get back into an integer/number, we got the right answer.
"""
#age = input('How young are you? ')
#age_num = int(age)

#print(f'You have lived for {age_num * 12} months!')


# Code Refactoring Version 1
"""
- Since we will never need to use the age as a string, it's cleaner/more logical to convert it to a int/num right off the bat.
"""
#age = int(input('How young are you? '))

#print(f'You have lived for {age * 12} months!')


# Code Refactoring Version 2
"""
- This avoids doing the math in our carley braces, passing a variable with the math already done is cleaner & good practise.
"""
#age = int(input('How young are you? '))
#months = age * 12

#print(f'You have lived for {months} months!')



"""
EXERCISE: Calculate the number of Seconds, instead of Months
"""
age = int(input('How young are you? '))
seconds = age * 31536000
secs = age * 365 * 24 * 60 * 60

print(f'You have lived for {seconds} seconds!')
print(f'You have lived for {secs} secs!')
