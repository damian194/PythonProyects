menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize
order = []
total_cost = 0.00

print("Welcome to Felipe's Taqueria!")

while True:
    try:
        item = input("Please enter your order (Ctrl-D to finish): ").strip()
        # Check if the user has pressed Ctrl-D (EOF)
        if not item:
            break

        # Case-insensitive search for the menu item
        matched_item = None
        for menu_item in menu:
            if menu_item.lower() == item.lower():
                matched_item = menu_item
                break

        if matched_item:
            order.append(matched_item)
            total_cost += menu[matched_item]
            print(f"Added {matched_item} to your order. Your total is ${total_cost:.2f}")
        else:
            print("Sorry, that's not on the menu. Please enter a valid item.")

    except EOFError:
        break

# Display the final order and total cost
if order:
    print("\nYour order:")
    for item in order:
        print(item)
    print(f"Total cost: ${total_cost:.2f}")
else:
    print("No items were ordered. Have a nice day!")
