
food_items = [("Burger", 120), ("Pizza", 250), ("Pasta", 180), ("Sandwich", 90), ("Fries", 70)]
sorted_food_items = sorted(food_items, key=lambda item: item[1], reverse=True)

print(sorted_food_items)
