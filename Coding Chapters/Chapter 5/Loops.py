grocery_list = ["apple", "banana", "orange", "spinach", "kale", "curry", "potatoes"]


letter_to_check = input("What letter should we check? ")

for item in grocery_list:
    if item[0] == letter_to_check:
        print(item)
    else:
        print("Nothing with that letter here")

