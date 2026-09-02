import sys
def main():
    s = cla_checker()
    print(line_counter(s))

def cla_checker():
    if len(sys.argv) != 2:
        sys.exit("Not enough/too many arguments ")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("argument must end in '.py' ")
    else: 
        return sys.argv[1]

def line_counter(s):
    content = []
    try:
        with open(s) as file:
            for row in file:
                if not row.strip() =="" and not row.strip().startswith("#"):
                    content.append(row)
            return len(content)
    except FileNotFoundError:
        sys.exit("File does not exist! ")

if __name__ == "__main__":
    main()