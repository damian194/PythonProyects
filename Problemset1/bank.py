def main():
    user_response = input("Please give me a greeting: ")
    normalized_response = user_response.lower().replace(" ", "")

    if "hello" in normalized_response:
        print("$0")
    elif normalized_response.startswith ("h"):
        print("$20")
    else:
        print("$100")

main()