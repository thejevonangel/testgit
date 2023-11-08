grocery_list = ["apple", "banana", "orange", "spinach", "kale", "curry", "potatoes"]


# letter_to_check = input("What letter should we check? ")

# for item in grocery_list:
#     if item[0] == letter_to_check:
#         print(item)
#     else:
#         print("Nothing with that letter here")
#         break

grocery_length = len(grocery_list)

for i in range(grocery_length):
    print(grocery_list[i])
