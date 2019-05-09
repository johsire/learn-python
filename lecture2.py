#Python Strings & String Formatting Using F-String Format:

# What is a string?

"""
- String: A set of characters, symbols, or numbers that have no meaning to the computer
- A string, is not something you'll want to do maths with (but you can still use it for other stuff).

- We use strings when we want to store and refer to specific letters and numbers.
- Strings in Python are represented as the characters we're interested in, surrounded by quotation
marks—such as "CodeJoh", "1990-06-10", or "07248571374" etc.

- When you have a number, that # represents quantity or a value, but a string doesn't represent anything, it's the digits or characters themselves.
- But they can be used, for things that make sense to a person, but not necessarily to a computer.
"""

#E.g, this string saved in this variable, doesn't make sense to the comp, but it says something to the user..& we can retrive it/print in by saving it in a variable.
my_string = "Hello, world"
print(my_string)


# You can use double or single quotes, but just keep it consistent in your code.
single_quote_string = 'Hello, word'


#If you have a quote in the middle of your string, make sure to use to opposite quotes for the outer quotes
string_with_double_quotes = "Hello, it's me."
print(string_with_double_quotes)


string_with_single_quotes = 'He said, "You are awesome" yesterday!'
print(string_with_single_quotes)


#This is a different way to escape quotes, not as recommended though.
escaped_quotes = "He said \"You are amazing!\" earlier."
print(escaped_quotes)


# ---------------------------------------------
#String Formatting

"""
- We made our string dynamic by concatenating it
"""
name = 'CoderJoh'
greeting = 'Hello, ' + name
print(greeting)


"""
- In f-strings, {name} gets replaced by the value of the variable name.
- The 'f' means format/ replace whatever variable that is in the carly braces- {name} in our example with the value that represents it- 'coderjoh'.
"""
# Use f-string only when working w/ Python 3.6 & above. It's the NEW way of formatting strings
ef_string_greeting = f'Good Morning , {name}'
print(ef_string_greeting)



"""
- This is the 2nd way to format our string
- Start with a normal string with empty carley braces & NO 'f' at the beginning.
- Then to format/ add our 'name' variable value in the empty carley braces, we use '.format(name)'
"""
# This way of formatting only works on Python 3.5 & below. It's the OLD way of formatting strings.
dot_format_greeting = 'Hey there , {}'
formatted_greeting = dot_format_greeting.format(name)
print(formatted_greeting)


# Extra resources

"""
Numeric types
https://docs.python.org/3.7/library/stdtypes.html#numeric-types-int-float-complex

String
https://docs.python.org/3.7/library/stdtypes.html#text-sequence-type-str
"""
