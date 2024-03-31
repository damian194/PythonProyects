def main():
    camel_case = input("Please enter a camel case variable name: ")
    snake_case = convert_camel_to_snake(camel_case)
    print("Snake case:", snake_case)

def convert_camel_to_snake(camel):
    snake = ''.join(['_' + c.lower() if c.isupper() else c for c in camel])
    return snake.lstrip('_')

if __name__ == "__main__":
    main()
