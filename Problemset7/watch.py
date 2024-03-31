import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Define a regular expression pattern to match YouTube URLs in src attributes
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'

    # Use re.search to find the first match in the input string
    match = re.search(pattern, s)

    # If a match is found, extract the video ID and create the youtu.be URL
    if match:
        video_id = match.group(1)
        youtu_be_url = f"https://youtu.be/{video_id}"
        return youtu_be_url
    else:
        return None

if __name__ == "__main__":
    main()
