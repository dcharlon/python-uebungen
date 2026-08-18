def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if alnum(s) == True and length(s) == True and twoletfirst(s) == True and corrnum(s) == True:
        return True
    else: 
        return False

def alnum(s):
    if s.isalnum():
        return True

def length(s):
    if 1 < len(s) < 7:
        return True

def twoletfirst(s):
    if s[0:2].isalpha():
        return True

def corrnum(plate):
    seen_digit = False
    for i, c in enumerate(plate):
        if c.isnumeric():
            if not seen_digit and c == "0":
                return False 
            seen_digit = True
        else:
            if seen_digit:
                return False  
    return True


main()

