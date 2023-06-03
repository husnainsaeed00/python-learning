
def main():
    yell("OOOy","where are you going?", "stop")
    
def yell(*words):
    upercased = []
    for word in words:
        upercased.append(word.upper())
    print(*upercased)

if __name__ == "__main__":
    main()