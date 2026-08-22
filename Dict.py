# Dictionary in which we will store a restaurat menu

menu = {
    "pizza":200,
    "burger":150,
    "hot_burgrt":180
}

# To add iten in menu
menu["non-veg"] = 250

# modify the menu price of the particular item
menu["pizza"] = 220

# If we want ot double the current price
menu["burger"] = menu["burger"] * 2

# To remove the item
menu.pop("non-veg")

print(menu)

# To print key and value all together.
# K is stand for "Key"
# v is stanf for "values"

for k, v in menu.items():
    print(k, v)