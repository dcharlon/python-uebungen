def main():
    time = convert(input("Give me a time in the 24h format: "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <=19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    time = int(hours) + float(int(minutes) / 60)
    return time

if __name__ == "__main__":
    main()