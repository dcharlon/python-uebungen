import sys
import csv

def main():
    file_names = cla_checker()
    list_of_data = (get_input(file_names))
    get_output(file_names[1], list_of_data)

def cla_checker():
    if len(sys.argv) != 3:
        sys.exit("Not enough/too many arguments ")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("both file names must end in '.csv' ")
    elif not sys.argv[2].endswith(".csv"):
        sys.exit("both file names must end in '.csv' ")
    else: 
        return sys.argv[1:3]


def get_input(s):
    data_list = []
    try:
        with open(s[0]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                student_data = {}
                name = row.get("name")
                house = row.get("house")
                last_name, first_name = name.split(", ")
                student_data["first"] = first_name
                student_data["last"] = last_name
                student_data["house"] = house
                data_list.append(student_data)
    except FileNotFoundError:
        sys.exit("First file did not exist! ")
    return data_list

def get_output(s, t):
    with open(s, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames= ["first", "last", "house"])
        writer.writeheader()
        writer.writerows(t)
        

if __name__ =="__main__":
    main()

