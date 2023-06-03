"""balance = 0

def main():
    print("balance:", balance)
    deposit(1000)
    withdraw(300)
    print("balace:", balance)
    
    

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()    
    """
class Account:
    def __init__(self):
        self._balance =0
    @property
    def balance(self):
        return self._balance

    def deposit(self,n):
        self._balance+=n

    def withdraw(self,n):
        self._balance-=n 

def main():
    account = Account()
    print("balance:", account.balance)
    account.deposit(100)
    account.withdraw(40)
    print("balance:", account.balance)


if __name__ == "__main__":
    main()