"""

Asking questions

Study drills:
1. Go online and find out what pyhons input does
2. can you find other ways to use it? try some of the samples you find
3. write another "form" like this to ask some other questions
"""


"""
print("How old are you?", end = ' ')
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

person = input('Enter your name: ')
print('Hello ', person, '!', sep = '**')

# Error in addition to output
x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))
print('The sum of ', x, ' and ', y, ' is ', x + y, '.', sep = '')


#Three numeric inputs, explicit sum
x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))
sum = x + y
sentence = 'The sum of {} and {} is {}'.format(x, y, sum)

print(sentence)


# Fancier format string with parameter identification numbers
x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))
format_string = '{0} + {1} = {2}; {0} * {1} = {3}; {0} ^ {1} = {4}.'
equations = format_string.format(x, y, x+y, x*y, x**y)
print(equations)

"""
x = int(input())

print (x * 10)
