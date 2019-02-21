"""

Else and If

If statements create a branch in the code

"""

people = 29
cars = 30
trucks = 27

if cars > people:
    print(">> cars > people", cars, people)
    print("We should take the cars")
elif cars < people:
    print(">> cars < people: ", cars, people)
    print("We should not take the cars")
else:
    print(">> cars == people: ", cars, people)
    print("we can't decide.")

if trucks > cars:
    print(">> trucks > cars: ", trucks, cars)
    print("That's too many trucks.")

elif trucks < cars:
    print(">> trucks < cars: ", trucks, cars)
    print("Maybe we could take the trucks.")
else:
    print(">> trucks == cars: ", trucks, cars)
    print("We still can't decide.")

if people > trucks:
    print(">> people > trucks", people, trucks)
    print("Alright, let's just take the trucks.")
else:
    print(">> people <= trucks", people, trucks)
    print("Fine, let's stay home then.")

print("Boolean practice+++++++++++++")
if cars > people or trucks < cars:
    print("Cars are greater than people OR trucks are less than cars")
    if cars > people and trucks < cars:
        print("Cars are more than people and trucks are less than cars")
        if trucks < people:
            print("And trucks are less than people!")
