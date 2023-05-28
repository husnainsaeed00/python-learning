#for _ in range(4):
 #   print("#")

"""def main():
    print_row(4)
    print_column(3)


def print_row(width):
    print("#"*width)
def print_column(height):
        print("#\n" *height, end="")..."""

"""def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

main()"""

def main():
    height= int(input("whats is the height:"))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * (i+1))

if __name__ == "__main__":
    main()