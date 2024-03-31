import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level)
        problem = f"{x} + {y} = "
        answer = x + y

        tries = 0
        while tries < 3:
            user_answer = input(problem)

            try:
                user_answer = int(user_answer)
                if user_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"The correct answer is {answer}")

    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level (1, 2 or 3): ")
        if level in ['1', '2', '3']:
            return int(level)
        else:
            print("")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999), random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

if __name__ == "__main__":
    main()
