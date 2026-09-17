import pickle
import os

FILE_NAME = "ATMData.pkl"


class Account:
    def __init__(self, account_number, holder_name, balance):  
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance


def create_accounts():
    try:
        with open(FILE_NAME, "wb") as out:
            accounts = [
                Account(1000 + i, f"Holder{i}", 1000.0 * i)
                for i in range(1, 11)
            ]
            pickle.dump(accounts, out)
        print("10 Accounts created.")  
    except IOError as e:
        print(e)


def read_accounts():
    accounts = []
    if not os.path.exists(FILE_NAME):
        return accounts
    try:
        with open(FILE_NAME, "rb") as f:
            accounts = pickle.load(f)
    except (EOFError, pickle.UnpicklingError):
        pass
    except Exception as e:
        print(e)
    return accounts


def save_accounts(accounts):
    try:
        with open(FILE_NAME, "wb") as out:
            pickle.dump(accounts, out)
    except IOError as e:
        print(e)


def find_account(accounts, acc_no):
    for acc in accounts:
        if acc.account_number == acc_no:
            return acc
    return None


def withdraw(acc_no, amount):
    accounts = read_accounts()
    acc = find_account(accounts, acc_no)
    if acc is not None and acc.balance >= amount:
        acc.balance -= amount
        save_accounts(accounts)
        print(f"Withdrawal successful. New Balance: {acc.balance}")
    else:
        print("Insufficient funds or account not found.")


def deposit(acc_no, amount):
    accounts = read_accounts()
    acc = find_account(accounts, acc_no)
    if acc is not None:
        acc.balance += amount
        save_accounts(accounts)
        print(f"Deposit successful. New Balance: {acc.balance}")
    else:
        print("Account not found.")


def transfer(from_acc, to_acc, amount):
    accounts = read_accounts()
    sender = find_account(accounts, from_acc)
    receiver = find_account(accounts, to_acc)

    if sender is not None and receiver is not None and sender.balance >= amount:
        sender.balance -= amount
        receiver.balance += amount
        save_accounts(accounts)
        print("Transfer successful.")
    else:
        print("Transfer failed. Check account numbers and balance.")


def balance_inquiry(acc_no):
    accounts = read_accounts()
    acc = find_account(accounts, acc_no)
    if acc is not None:
        print(f"Account No: {acc.account_number}")
        print(f"Holder Name: {acc.holder_name}")
        print(f"Balance: {acc.balance}")
    else:
        print("Account not found.")


def main():
    # Initialize 10 accounts the first time the program runs
    if not os.path.exists(FILE_NAME):
        create_accounts()

    while True:
        print("\nATM Menu")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Transfer")
        print("4. Balance Inquiry")
        print("5. Exit")
        option = int(input("Choose an option: "))

        if option == 5:
            break

        acc_no = int(input("Enter account number: "))

        if option == 1:
            w_amt = float(input("Enter amount to withdraw: "))
            withdraw(acc_no, w_amt)
        elif option == 2:
            d_amt = float(input("Enter amount to deposit: "))
            deposit(acc_no, d_amt)
        elif option == 3:
            to_acc = int(input("Enter receiver account number: "))
            t_amt = float(input("Enter amount to transfer: "))
            transfer(acc_no, to_acc, t_amt)
        elif option == 4:
            balance_inquiry(acc_no)
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()