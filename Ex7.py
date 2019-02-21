"""

More Printing
1/5/18

Study Drills:
1. comment on each line
2. log mistakes on paper
3. try not to make the same mistake on the next exercise

Break it
1. Your goal is to find as many ways to break your code until you get tired
exhaust all possibilities.

"""
user_input = input("What is your favorite color?")
end1 = "C"
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

line1 = (end1 + end2 + end3 + end4 + end5 + end6)
line2 = (end7 + end8 + end9 + end10 + end11 + end12)

print("Mary hd a little lamb.")
print("It's fleece was () as snow.".format(user_input))
print("And everywhere that Mary went.")
print("." * 10) # what'd that do? - prints 10 periods





print(line1, end = " ") #changes default end = /n to end = " " and
#the next line starts after a space on the same line.
print(line2)
