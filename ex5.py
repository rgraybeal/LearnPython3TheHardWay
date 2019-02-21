"""
PTHW Exercise 5 More variables and printing

format string with double quotes
Embedding variables in strings with {} sequence
Must start the string with f for 'format'
as in f"Hello {somevar}

1/4/18
"""
name = 'Randy R. Graybeal'
age = 48
height = 70 #inches
weight = 168 #lbs
eyes = 'blue'
teeth = 'white'
hair = 'missing'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are unusually {teeth} depending on coffee.")

#This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")

height_in_cm = round(height * 2.54)
weight_in_kg = round(weight/2.2)
print(f"{name}'s height in centimeters is {height_in_cm}")
print(f"{name}'s weight in kilograms is {weight_in_kg}")
