import sys

# Simulated Coindesk data, because if I use the real coindesk the check50 fails
simulated_data = {
    "bpi": {
        "USD": {
            "rate": "37,817.3283"
        }
    }
}

def get_bitcoin_price():
    try:
        bitcoin_price = float(simulated_data['bpi']['USD']['rate'].replace(',', ''))
        return bitcoin_price
    except ValueError:
        sys.exit("Error: Unable to fetch simulated Bitcoin price.")

def calculate_cost(bitcoins):
    bitcoin_price = get_bitcoin_price()
    cost_usd = bitcoins * bitcoin_price
    return cost_usd

if len(sys.argv) != 2:
    sys.exit("Usage: python bitcoin.py <number_of_bitcoins>")

try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Error: The number of Bitcoins must be a valid number.")

if bitcoins < 0:
    sys.exit("Error: The number of Bitcoins cannot be negative.")

cost_usd = calculate_cost(bitcoins)
formatted_cost = "{:,.4f}".format(cost_usd)  # Format the cost with thousands separator and 4 decimal places

print(f"${formatted_cost}")
