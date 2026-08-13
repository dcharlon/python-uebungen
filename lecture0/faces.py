def main():
    x = input("Use the emoticons :) and :( ")
    print(convert(x))
def convert(x): 
    return x.replace(":)", "🙂").replace(":(", "🙁")
main()