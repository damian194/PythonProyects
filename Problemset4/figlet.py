import sys
from pyfiglet import Figlet

def get_random_font():
    figlet = Figlet()
    return figlet

def get_specific_font(font_name):
    try:
        figlet = Figlet(font=font_name)
        return figlet
    except Exception as e:
        print(f"Error: Font '{font_name}' not found.")
        sys.exit(1)

def main():
    if len(sys.argv) == 1:
        figlet = get_random_font()
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font_name = sys.argv[2]
        figlet = get_specific_font(font_name)
    else:
        print("Usage: figlet.py [OPTION]... [TEXT]")
        print("Options:")
        print("  -f, --font FONT_NAME   Specify the font to use")
        sys.exit(1)

    text = input("Enter text: ")
    output = figlet.renderText(text)
    print(output)

if __name__ == "__main__":
    main()
