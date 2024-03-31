import emoji

def main():
    user_input = input("Enter a string in English: ")

    def custom_replace(match):
        emoji_alias = match.group()
        emoji_unicode = emoji.emojize(emoji_alias)
        return emoji_unicode

    emojized_text = emoji.demojize(user_input, delimiters=(":", ":"))
    emojized_text = emoji.emojize(emojized_text, delimiters=(":", ":"))
    print("Emojized version:")
    print(emojized_text)

if __name__ == "__main__":
    main()



