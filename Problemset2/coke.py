amount_due = 50

while amount_due > 0:
    try:
        coin = int(input(f"Amount Due: {amount_due}\nInsert Coin (25, 10, or 5 cents): "))

        if coin in [25, 10, 5]:
            amount_due -= coin
        else:
            print("Invalid coin. It only accepts coins of 25, 10 or 5 cents.")
    except ValueError:
        print("Invalid entry. Give me an int.")

if amount_due == 0:
    print("Change Owed: 0")
else:
    print(f"Change Owed: {abs(amount_due)}")



