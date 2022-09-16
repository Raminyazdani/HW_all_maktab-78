class BankAccount:
    counts=0
    bank_poses = 50
    accounts = {}
    def __init__(self, account, initial_amount):
        self.account = account
        self.initial_amount = initial_amount
        self.balance = 0 + initial_amount
        BankAccount.counts+=1
        BankAccount.accounts[account]=self
        print(repr(self),"was succesfully initialized")
    @property
    def withdraw_amount(self):
        if (x:=self.balance - BankAccount.bank_poses)>0:
            return self.balance - BankAccount.bank_poses
        else:
            return 0

    def deposit(self, amount):
        self.balance += amount

    def transfer(self, other, amount):
        if self.withdraw_amount - amount >= 0:
            self.balance -= amount
            other.balance += amount
            print("\ntransfer successful")
            print(f"\t{amount} was transferred from {self.account} to {other.account}\n")
        else:
            print("transfer failed")
            print(f"can withdraw {self.withdraw_amount} from {self.account}\n")

    def __str__(self):
        return f"\t{self.account:10s}:\t{self.balance:10.1f}\t\tcan withdraw : {self.withdraw_amount:10.1f}"
    def __repr__(self):
        return f"{self.account}:{self.balance}"

    def __add__(self, other):
        print("this will join these two accounts together")
        print(f"\t{self.account:10s}:\t{self.balance:10.1f}")
        print(f"\t{other.account:10s}:\t{other.balance:10.1f}\n")
        new = BankAccount(self.account+"-"+other.account,self.balance+other.balance)
        del BankAccount.accounts[self.account]
        del BankAccount.accounts[other.account]
        del self
        del other
        BankAccount.counts-=2
        return new

    def __gt__(self, other):
        return self.balance > other.balance
    def __lt__(self, other):
        return self.balance<other.balance
    def __ge__(self, other):
        return self.balance>=other.balance
    def __le__(self, other):
        return self.balance<=other.balance

    def __int__(self):
        return int(self.balance)

if __name__ == '__main__':
    ramin = BankAccount("ramin", 50_000)
    ali = BankAccount("ali", 50_000)
    ghazal = BankAccount("ghazal", 0)
    print(ramin)
    print(ali)
    ramin.transfer(ali, 49_950)
    print(f"does ramin have more many tahn ali ? {ramin>ali}")
    # print(ramin)
    # print(ali)
    # print(ghazal)
    ramin_ali = ramin+ali
    # print(ali_ramin)
    w = BankAccount.accounts["ghazal"]
    w.deposit(50_000_000)
    # print(w)
    # print(BankAccount.accounts)
