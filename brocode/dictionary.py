# dictionary = a collection of {key:value} pairs
#              ordered and changeable, No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital does not exist")

# capitals.update({"Germany": "Berlin"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

keys = capitals.keys()

# for key in capitals.keys():
#     print(key)
#
# values = capitals.values()
# for value in capitals.items():
#     print(value)

for key, value in capitals.items():
    print(f"{key}: {value}")