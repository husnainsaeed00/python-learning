
def main():
    yell("OOOy","where are you going?", "stop")
    
def yell(*words):
    upercased = map(str.upper, words)
    print(*upercased)

if __name__ == "__main__":
    main()