# list comprehensions of functions in the current implementation of the function
def main():
    yell("this is a test", "take it or leave", "boy")


def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)





if __name__ == '__main__':
    main()
    