import sys
from tabulate import tabulate

def main():
    s = cla_checker()
    print(table_conversion(s))

def cla_checker():
    if len(sys.argv) != 2:
        sys.exit("Not enough/too many arguments ")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("argument must end in '.csv' ")
    else: 
        return sys.argv[1]

def table_conversion(s):
    table_list = []
    try:
        with open(s) as file:
            for row in file:
                table_list.append(row.rstrip().split(","))
            return tabulate(table_list, headers="firstrow", tablefmt="grid")
    except FileNotFoundError:
        sys.exit("Invalid file name! ")

if __name__ == "__main__":
    main()

