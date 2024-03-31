def main():
    user_input = input("Please enter an arithmetic expression (x y z): ")
    x, operator, z = user_input.split()

    x = int(x)
    z = int(z)

    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z

    print("{:.1f}".format(result))

main()