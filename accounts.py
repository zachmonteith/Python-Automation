import datetime
import pytz

class Account:
    #simple account class with balance
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    @staticmethod
    def _dispense_money(amount):
        money = ""
        cash = {
            100: "[~HUNNID~] ",
            50: "[~FIFTY~] ",
            20: "[~TWENTY~] ",
            10: "[~TEN~] ",
            5: "[~FIVE~] ",
            1: "[~ONE~] ",
        }
        for key in cash.keys():
            for i in range(amount // key):
                money += cash[key]
                amount -= key
        return money


    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        self.__transaction_list = [(Account._current_time(), balance)]
        print("account created for " + self.__name)

    def deposit(self, amount):
        if amount > 0:
            print("depositing {} into account with balance {}".format(amount, self.__balance))
            self.__balance += amount
            self.__transaction_list.append((Account._current_time(), amount))
            print("deposit successful, new balance is {}".format(self.__balance))
        else:
            print("you cannot deposit {}".format(amount))

    def withdraw(self, amount):
            if 0 < amount < self.__balance:
                print("withdrawing {} from total balance {}".format(amount, self.__balance))
                print(Account._dispense_money(amount))
                self.__balance -= amount
                self.__transaction_list.append((Account._current_time(), -amount))
                print("withdrawl successful, new balance is {}".format(self.__balance))
            elif amount > self.__balance:
                print("""Insufficient funds!  you cannot withdraw {} as your balance is {}
                """.format(amount, self.__balance))
            else:
                print("you cannot withdraw {}".format(amount))

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self.__transaction_list:
            if amount >= 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdrawn'
                amount *= -1
            print("{:6} {} on {} \n\t(local time was {})".format(amount, tran_type, date,  date.astimezone(pytz.timezone('US/Pacific'))))

if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()
    tim.deposit(1000)
    tim.withdraw(285)
    tim.deposit(0)
    tim.withdraw(-10)
    tim.withdraw(44)
    tim.withdraw(10000)
    tim.show_transactions()
