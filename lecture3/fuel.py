def main():
    percentage = 100 * get_fraction()
    if 1 < percentage < 99:
        print(f"{round(percentage)}%")
    elif 1 >= round(percentage):
        print ("E")
    else:
        print("F")

def get_fraction():
    while True:
        [x, y] = input("Fraction: ").split("/")
        try:
            if int(x) >= 0 and int(y) > 0 and int(x) <= int(y):
                return int(x)/int(y)
        except ValueError:
            pass
        

main()