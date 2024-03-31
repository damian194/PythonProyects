def main():
    user_response = input("Please enter the answer to the Great Question of Life, the Universe and Everything: ")
    normalized_response = user_response.lower().replace(" ", "")

    if "42" in normalized_response or "fortytwo" in normalized_response or "forty-two" in normalized_response:
        print("Yes")
    else:
        print("No")

main()