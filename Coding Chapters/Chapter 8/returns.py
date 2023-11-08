def addTwo(num):
    return num + 2

def addThree(num):
    return num + 3

# print(addThree(addTwo(5)))

def namePrinter(first, middle, last=''):
    return f"The name's {last}, {first} {middle} {last}."

# print(namePrinter("James", "Bond"))

def giveMeMySports(name_to_add):
    grocery_list = ['grapes', 'oranges', 'bananas']
    grocery_list.append(name_to_add)
    return grocery_list

print(giveMeMyGroceries('spaghetti'))
                    