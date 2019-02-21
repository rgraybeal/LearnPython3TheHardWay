"""

Loops and lists

"""


the_count = range(1,5)
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This is the first kind of for-llooop goes through a list

for number in the_count:
    print(f"This is count {number}")

# Same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also, we can go through mixed lists too
# notice we have yo use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")
print(">>>> change = : ", repr(change))
print(">>>> after range, i =: ", i)


# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts

for i in range(0,6):
    print(f"Here are the numbers: {i}")
    elements.append(i)

print(">>> after range: i=", i)

print(">>>> elements", repr(elements))



#print(f"Adding {i} to the list")
    # append is a function that lists understand
#elements.append(i)




# now we can print them out too
#for i in elements:
    #print(f"Element was: {i}")
#print(elements)
