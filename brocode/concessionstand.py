menu = {"icecream": 2.50,
        "milk": 3.00,
        "banana": 1.00,
        "apple": 1.00,
        "chips": 5.00}

cart = []
total = 0
print("---------- MENU ----------")
print(menu)
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("---------- YOUR ORDER ----------")

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")