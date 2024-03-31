def main():
    user_response = input("Please give me the name of the file and its extension: ")
    normalized_response = user_response.lower().replace(" ", "")

    if ".gif" in normalized_response:
        print("image/gif")
    elif ".jpg" in normalized_response:
        print("image/jpeg")
    elif ".jpeg" in normalized_response:
        print("image/jpeg")
    elif ".png" in normalized_response:
        print("image/png")
    elif ".pdf" in normalized_response:
        print("application/pdf")
    elif ".txt" in normalized_response:
        print("text/plain")
    elif ".zip" in normalized_response:
        print("application/zip")
    else:
        print("application/octet-stream")

main()