def main():
    x = int(input("Enter mass in kilograms: "))
    print("The equivalent energy in Joule to your mass is... ",massenergyconversion(x))

def massenergyconversion(x):
    c = 300000000
    e = x*c**2
    return e
main()
