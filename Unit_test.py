from calculater import square


def main():
    test_square()

def test_square():
""" if square(2) !=4:
        print("2 squared was not 4")
    if square(3):
        print("3 square was not 9")
"""try:
        assert square(2) = 4
    except AssertionError:
        print("2 square was not 4")

if __name__ == "__main__":
    main() 