def main():
    while True:
        user_date = input("date: ")
        if only_digit_date(user_date) == True:
            break
        elif month_name_date(user_date) == True:
            break
        else:
            pass

def only_digit_date(s):
    try:
        [m, d, y] = s.split("/")
        if 0 <= int(y) < 10000 and 9 < int(m) < 13 and 9 < int(d) < 32:
            print(f"{y}-{m}-{d}")
            return True
        elif 0 <= int(y) < 10000 and 0 < int(m) < 10 and 9 < int(d) < 32:
            print(f"{y}-0{m}-{d}")
            return True
        elif 0 <= int(y) < 10000 and 9 < int(m) < 13 and 0 < int(d) < 10:
            print(f"{y}-{m}-0{d}")
            return True 
        elif 0 <= int(y) < 10000 and 0 < int(m) < 10 and 0 < int(d) < 10:
            print(f"{y}-0{m}-0{d}")
            return True
        else: 
            return False  
    except ValueError:
        return False
      
def month_name_date(s):
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    try:
        [m, d, y] = s.split(" ")
        number_of_month = month_names.index(m) + 1
        d_no_comma = d.removesuffix(",")
        if 0 <= int(y) < 10000 and 9 < number_of_month < 13 and 9 < int(d_no_comma) < 32:
            print(f"{y}-{number_of_month}-{d_no_comma}")
            return True
        elif 0 <= int(y) < 10000 and 0 < number_of_month < 10 and 9 < int(d_no_comma) < 32:
            print(f"{y}-0{number_of_month}-{d_no_comma}")
            return True
        elif 0 <= int(y) < 10000 and 9 < number_of_month < 13 and 0 < int(d_no_comma) < 10:
            print(f"{y}-{number_of_month}-0{d_no_comma}")
            return True 
        elif 0 <= int(y) < 10000 and 0 < number_of_month < 10 and 0 < int(d_no_comma) < 10:
            print(f"{y}-0{number_of_month}-0{d_no_comma}")
            return True
        else: 
            return False                   
    except ValueError:
        return False

main()