class Bankaccount:
    def __init__(self,bank_name, account_number,account_opening_date,nomini_name):
        self.name=bank_name
        self.number = account_number
        self.date = account_opening_date
        self.nomini_name = nomini_name

class SavingAccount(Bankaccount):
    def __init__(self,bank_name, account_number,account_opening_date,nomini_name,account_holder_name,amount,pin):
        super().__init__(bank_name, account_number,account_opening_date,nomini_name)
        self.account_holder_name = account_holder_name
        self._balance = amount
        self.__pin = pin

    def deposite(self,amount):
        self._balance += amount
        print(f'{amount} your amount deposite suceesfully')

    def wihtdraw(self,amount,w_pin):
        if self.__pin == w_pin:
            if self._balance >= amount:
                self._balance -= amount
                print(f'Rs {amount} is debited sucessfully')

            else:
                print("insuficeinent balance")

        else:
            print("Enter valiid pin number")
    def check_balance(self):
        print("Current Balance:", self._balance)
    


class CurrentAccount(Bankaccount):
    def __init__(self,bank_name, account_number,account_opening_date,nomini_name,account_holder_name,amount,pin,over_draft):
        super().__init__(bank_name, account_number,account_opening_date,nomini_name)
        self.account_holder_name = account_holder_name
        self._balance = amount
        self.__pin = pin
        self.over_draft = over_draft


    def deposite(self,amount):
        self._balance += amount
        print(f'{amount} your amount deposite suceesfully')


    def wihtdraw(self,amount,w_pin):
        if self.__pin != w_pin:
            print("Invalid PIN")
            return

        available_amount = self._balance + self.over_draft

        if amount > available_amount:
            print("Insufficient funds including overdraft")
            return

        self._balance -= amount

        if self._balance < 0:
            print("Overdraft used")
            print("Remaining Overdraft:", self.over_draft + self._balance)

        print(f"Rs {amount} debited successfully")
        print("Current Balance:", self._balance)
    def check_balance(self):
        print("Current Balance:", self._balance)
        print("Overdraft Limit:", self.over_draft)

        if self._balance < 0:
            print("Used Overdraft:", abs(self._balance))
            print("Remaining Overdraft:", self.over_draft - abs(self._balance))

obj = CurrentAccount("sbi",12345678,"29-05-2026","mother","rohit",50000,1234,10000)
# obj.deposite(5000)
obj.wihtdraw(5000,1234)








