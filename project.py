class Transaction:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def display(self):
        print(f"Amount: ${self.amount}, Category: {self.category}, Description: {self.description}")


class IncomeTransaction(Transaction):
    def __init__(self, amount, category, description, source):
        super().__init__(amount, category, description)
        self.source = source

    def display(self):
        super().display()
        print(f"Source: {self.source}")


class ExpenseTransaction(Transaction):
    def __init__(self, amount, category, description, payment_method):
        super().__init__(amount, category, description)
        self.payment_method = payment_method

    def display(self):
        super().display()
        print(f"Payment Method: {self.payment_method}")


class PersonalFinanceTracker:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.balance += transaction.amount

    def show_balance(self):
        print(f"Current Balance: ${self.balance}")

    def show_transactions(self):
        print("Transactions:")
        for transaction in self.transactions:
            transaction.display()


# Example usage:
if __name__ == "__main__":
    finance_tracker = PersonalFinanceTracker()

    # Adding transactions
    income_transaction = IncomeTransaction(1000, "Income", "Salary", "XYZ Company")
    expense_transaction = ExpenseTransaction(-50, "Food", "Groceries", "Credit Card")

    finance_tracker.add_transaction(income_transaction)
    finance_tracker.add_transaction(expense_transaction)

    # Displaying balance and transactions
    finance_tracker.show_balance()
    finance_tracker.show_transactions()