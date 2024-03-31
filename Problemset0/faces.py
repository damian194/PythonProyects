def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    input_text = input("Please give me an emoji: ")
    converted_text = convert(input_text)
    print("Here is your emoji but in a graphic mode: ", converted_text)

main()
