import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import pandas as pd

class Transaction:
    """
    A class representing a transaction
    
    :param amount: The amount of money of the transaction
    :param category: The category the transaction belongs to
    :param description: A short description of the transaction
    """
    def __init__(self, amount, category, description):
        """
        Initialize a new instance of Transaction

        :param amount: The amount of money of the transaction
        :param category: The category the transaction belongs to
        :param description: A short description of the transaction 
        """
        self.amount = amount
        self.category = category
        self.description = description

    def display(self):
        """Returns the attributes of a transaction"""
        print(f"Amount: ${self.amount}, Category: {self.category}, Description: {self.description}")

class IncomeTransaction(Transaction):
    """
    A subclass of Transaction representing an income transaction
    
    :param amount: The amount of income of the transaction
    :param category: The category the income belongs to
    :param description: A short description of the transaction
    :param source: The source of the income
    """
    def __init__(self, amount, type, category, description, source):
        """
        Initialize a new instance of IncomeTransaction
        
        :param amount: The amount of income of the transaction
        :param cateory: The category the income belongs to
        :param description: A short description of the transaction
        :param source: The source of the income"""
        super().__init__(amount, category, description)
        self.type = type
        self.source = source

    def display(self):
        """Returns the attributes of an income transaction"""
        super().display()
        print(f"Source: {self.source}")

class ExpenseTransaction(Transaction):
    """
    A subclass of Transaction representing an expense transaction
    
    :param amount: The amount of the expense
    :param cateory: The category the expense can be categorized as 
    :param description: A short description of the expense
    :param payment_method: The method to pay the expense
    """
    def __init__(self, amount, type, category, description, payment_method):
        """Initialize a new instance of ExpenseTransaction
        
        :param amount: The amount of the expense
        :param cateory: The category the expense can be categorized as 
        :param description: A short description of the expense
        :param payment_method: The method to pay the expense
        """
        super().__init__(amount, category, description)
        self.type = type
        self.payment_method = payment_method

    def display(self):
        """Returns the attributees of an expense transaction"""
        super().display()
        print(f"Payment Method: {self.payment_method}")

class PersonalFinanceTracker:
    """
    A class representin a personal finance tracker
    
    :param balance: The balance of the account after all transactions
    :param transactions: A list containing all the transactions
    """
    def __init__(self):
        """Initialize a new instance of PersonalFinanceTracker
    
        :param balance: The balance of the account after all transactions
        :param transactions: A list containing all the transactions
        """
        self.balance = 0
        self.transactions = []

    def check_balance(self):
        """
        Checks whether balance is negative or not

        Returns True if balance greater than 0
        Returns False if balance less than 0
        """
        if self.balance < 0:
            return True
        else:
            return False

    def add_transaction(self, transaction):
        """Adds transaction object to transaction list"""
        self.transactions.append(transaction)
        self.balance += transaction.amount

    def show_balance(self):
        """Display current balance"""
        print(f"Current Balance: ${self.balance}")

    def show_transactions(self):
        """Return list of all transaction objects contained in transaction list of PersonalFinanceTracker"""
        print("Transactions:")
        for transaction in self.transactions:
            transaction.display()

    def plot_transaction_amounts(self):
        """Creates bar graph displaying money in each transaction category"""
        amounts = [transaction.amount for transaction in self.transactions]
        categories = [transaction.category for transaction in self.transactions]

        # Plot bar chart
        plt.bar(categories, amounts, color=['green' if amount > 0 else 'red' for amount in amounts])

        # Add annotations (values) to the bars
        for i, amount in enumerate(amounts):
            plt.text(i, amount, f"${amount}", ha='center', va='bottom')

        plt.xlabel('Categories')
        plt.ylabel('Amount ($)')
        plt.title('Transaction Amounts')
        plt.show()

class Gui(tk.Tk):
    """
    A class representin a personal finance tracker
    
    :param balance: The balance of the account after all transactions
    :param transactions: A list containing all the transactions
    """
    def __init__(self, finance_tracker):
        # Initialize the window
        super().__init__()

        # Set the title
        self.title("My GUI App")
        
        # Store the finance tracker instance
        self.finance_tracker = finance_tracker

        # Create and add widgets (e.g., buttons, labels) to the window
        self.select_file_button = tk.Button(self, text="Import File", command=self.open_file_dialog)
        self.select_file_button.pack(pady=20)  # Add padding around the button

        self.button1 = tk.Button(self, text="Create Graph", command=self.clicked_graph_button)
        self.button1.pack(pady=20, padx=20)

    def open_file_dialog(self, finance_tracker):
        """Open the file explorer dialog"""
        file_path = filedialog.askopenfilename(title="Select a File")

        if file_path:
            print(f"Selected File: {file_path}")

        try:
            data = pd.read_excel(file_path, header=None)
            pass
        except FileNotFoundError:
            raise TypeError(f"The source file '{file_path}' does not exist.")
        
        all_data = data.values.tolist()

        for row in all_data:
            if row[1] == 'Income':
                new_income_transaction = IncomeTransaction(row[0], row[1], row[2], row[3], row[4])
                finance_tracker.add_transaction(new_income_transaction)
            elif row[1] == 'Expense':
                new_expense_transaction = ExpenseTransaction(row[0], row[1], row[2], row[3], row[4])
                finance_tracker.add_transaction(new_expense_transaction)
            else:
                print(f"Unhandeled transaction type: {row[1]}")
                continue

    def clicked_graph_button(self):
        self.finance_tracker.plot_transaction_amounts()

# Example usage:
if __name__ == "__main__":
    finance_tracker = PersonalFinanceTracker()

    # Adding transactions
    income_transaction = IncomeTransaction(1000, "Income","Salary", "Yeah ight", "XYZ Company")
    expense_transaction = ExpenseTransaction(-50, "Expense","Food", "Groceries", "Credit Card")

    example_transaction1 = IncomeTransaction(69, "Income","Donation", "Literally just asked", "Best friend")
    example_transaction2 = ExpenseTransaction(-132, "Expense","Entertainment", "Costco-Membership", "Credit Card")

    finance_tracker.add_transaction(income_transaction)
    finance_tracker.add_transaction(expense_transaction)
    finance_tracker.add_transaction(example_transaction1)
    finance_tracker.add_transaction(example_transaction2)

    # Displaying balance and transactions
    finance_tracker.show_balance()
    finance_tracker.show_transactions()

    my_gui = Gui(finance_tracker)

    my_gui.mainloop()