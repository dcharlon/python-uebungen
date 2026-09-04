import sys
import os
from PIL import Image 
from PIL import ImageOps

def main():
    input_test()
    image_conversion(sys.argv[1])

def input_test():
    if len(sys.argv) != 3:
        sys.exit("Too few/too many arguments! ")
    name1, extension1 = os.path.splitext(sys.argv[1])
    name2, extension2 = os.path.splitext(sys.argv[2])
    if extension1.casefold() != ".jpeg" and extension1.casefold() != ".jpg" and extension1.casefold() != ".png":
        sys.exit("Invalid file format! ")
    elif extension1 != extension2:
        sys.exit("Both files must be in the same format! ")

def image_conversion(s):
    try: 
        person = Image.open(s) 
    except FileNotFoundError:
        sys.exit("Input file does not exist! ")
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size
    resized_person = ImageOps.fit(image= person, size= shirt_size)
    resized_person.paste(im=shirt, mask=shirt)
    resized_person.save(sys.argv[2])

if __name__ =="__main__":
    main()