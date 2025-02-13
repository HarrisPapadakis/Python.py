class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        """Initialize an account with the holder's name and an optional balance."""
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Deposits an amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}€. New balance: {self.balance}€.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws an amount from the account if there is sufficient balance."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}€. New balance: {self.balance}€.")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        """Returns the current balance of the account."""
        return self.balance

    def display_info(self):
        """Displays account information."""
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}€")

# Example usage
if __name__ == "__main__":
    account = BankAccount("Giorgos Papadopoulos", 1000)
    account.display_info()
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)  # Attempt to withdraw more than available balance
    print("Final balance:", account.get_balance(), "€")
