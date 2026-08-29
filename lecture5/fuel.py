import sys
def main():
    fraction = input("Fraction: ")
    try:
        percentage = convert(fraction)
    except ValueError:
        sys.exit("Invalid fraction! ")
    except ZeroDivisionError:
        sys.exit("Invalid fraction! ")
    print(gauge(percentage))

def convert(fraction):
    [x, y] = fraction.split("/")
    if int(x) >= 0 and int(y) >= 0:
        if int(y) == 0:
            raise ZeroDivisionError
        elif int(x) > int(y):
            raise ValueError
        percentage = int(x)/int(y) * 100
        return round(percentage)
    else:
        raise ValueError

def gauge(percentage):
    if 0 <= percentage < 2:
        return "E"
    elif 98 < percentage < 101:
        return "F"
    elif 1 < percentage < 99 : 
        return f"{percentage}%"


if __name__ == "__main__":
    main()