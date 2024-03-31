grocery_list = {}

while True:
    try:
        item = input().strip()
        # Check if the user has pressed Ctrl-D (EOF)
        if not item:
            break

        # Case-insensitive count of items
        item_lower = item.lower()
        if item_lower in grocery_list:
            grocery_list[item_lower] += 1
        else:
            grocery_list[item_lower] = 1

    except EOFError:
        break

if grocery_list:
    # Sort the grocery list alphabetically
    sorted_items = sorted(grocery_list.keys())

    # Display the grocery list with counts and in uppercase
    print()
    for item in sorted_items:
        count = grocery_list[item.lower()]
        print(f"{count} {item.upper()}")

else:
    print("No items were added to the grocery list. Have a nice day!")
