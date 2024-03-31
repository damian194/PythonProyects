user_input = input("Input: ")
vowels = "AEIOUaeiou"
result = ""
for char in user_input:
    if char not in vowels:
        result += char
print("Output: ", result)
