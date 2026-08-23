import pyfiglet
import sys
import random 

figlet = pyfiglet.Figlet()
figlet_fonts = figlet.getFonts()
random_font = random.choice(figlet_fonts)

if len(sys.argv) == 1:
    text = input("text: ")
    f = pyfiglet.figlet_format(text, font = random_font)
    print(f)

elif len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet_fonts:   
        text = input("text: ")
        f = pyfiglet.figlet_format(text, font = sys.argv[2])
        print(f)
    else:
        sys.exit("Error: invalid font ")
else:
    sys.exit()

