def main():
    word = input("Give me some text: ")
    print(shorten(word))


def shorten(word):
    result = ""
    vocals = ["a", "e", "i", "o", "u"]
    for c in word:
        if c.casefold() not in vocals:
            result += c
    return result

if __name__ == "__main__":
    main()