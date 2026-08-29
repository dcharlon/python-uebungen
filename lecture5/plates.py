def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s.isalnum() and 1 < len(s) and len(s) < 7 and s[0:2].isalpha():
        seen_digit = False
        for i, c in enumerate(s):
            if c.isnumeric():
                if not seen_digit and c == "0":
                    return False 
                seen_digit = True
            else:
                if seen_digit:
                    return False  
        return True
    else:
        return False


if __name__ == "__main__":
    main()

