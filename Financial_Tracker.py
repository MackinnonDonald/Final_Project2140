import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import pandas as pd

class Transaction:
    """
    A class representing a transaction with no assigned type (income or expense)
    
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
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be an integer or float.")
        self.amount = amount
        self.category = category
        self.description = description
    
    def __str__(self):
        return f"Amount: ${self.amount}, Category: {self.category}, Description: {self.description}"

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
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be an integer or float.")
        elif amount < 0:
            raise ValueError("Amount of an income transaction must be greater than 0.")
        self.type = type
        self.source = source

    def __str__(self):
        return f"Amount: ${self.amount}, Type: {self.type}, Category: {self.category}, Description: {self.description}, Source: {self.source}"

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
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be an integer or float.")
        elif amount > 0:
            raise ValueError("Amount of an expense transaction must be less than 0.")
        self.type = type
        self.payment_method = payment_method

    def __str__(self):
        """Returns the attributees of an expense transaction"""
        return f"Amount: ${self.amount}, Type: {self.type}, Category: {self.category}, Description: {self.description}, Payment Method: {self.payment_method}"

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

    def remove_transaction(self, transaction_index):
        """Removes transaction object from transaction list"""
        try:
            self.balance -= self.transactions[transaction_index-1].amount
            removed_transaction = self.transactions.pop(transaction_index - 1)  # Adjust for 0-based index
            return removed_transaction
        except IndexError:
            raise IndexError("Invalid transaction index.")

    def show_balance(self):
        """Display current balance"""
        print(f"Current Balance: ${self.balance}")

    def show_transactions(self):
        """Return list of all transaction objects contained in transaction list of PersonalFinanceTracker"""
        print("Transactions:")
        for transaction in self.transactions:
            transaction.display()

    def total_categories(self):
        """Creates bar graph displaying total money in each transaction category"""
        category_totals = {}

        # Iterate through transactions and accumulate amounts for each category
        for transaction in self.transactions:
            category = transaction.category
            amount = transaction.amount

            # If category already exists in the dictionary, add the amount
            if category in category_totals:
                category_totals[category] += amount
            else:
                # Otherwise, create a new entry for the category
                category_totals[category] = amount

        return category_totals
            
    def plot_transaction_amounts(self):
        category_totals = self.total_categories()

        # Extract categories and total amounts for plotting
        categories = list(category_totals.keys())
        total_amounts = list(category_totals.values())

        # Plot bar chart
        plt.bar(categories, total_amounts, color=['green' if amount > 0 else 'red' for amount in total_amounts])

        # Add annotations (values) to the bars
        for i, amount in enumerate(total_amounts):
            plt.text(i, amount, f"${amount}", ha='center', va='bottom')

        plt.xlabel('Categories')
        plt.ylabel('Total Amount ($)')
        plt.title('Total Transaction Amounts by Category')
        plt.show()

class Gui(tk.Tk):
    """
    A class representin a personal finance tracker
    
    :param balance: The balance of the account after all transactions
    :param transactions: A list containing all the transactions
    """
    def __init__(self, finance_tracker, excel_file_path=None):
        # Initialize the window
        super().__init__()

        # Set the title
        self.title("My GUI App")
        
        # Store the finance tracker instance
        self.finance_tracker = finance_tracker
        self.excel_file_path = excel_file_path

        # Create and add widgets (e.g., buttons, labels) to the window
        self.import_file_button = tk.Button(self, text="Import File", command= lambda: self.open_file_dialog(self.finance_tracker))
        self.import_file_button.pack(pady=10)  

        self.graph_button = tk.Button(self, text="Create Graph", command=self.clicked_graph_button)
        self.graph_button.pack(pady=20)

        self.add_transaction_button = tk.Button(self, text = "Add new transaction", command= lambda: self.open_new_transaction_window())
        self.add_transaction_button.pack(pady=25)
        self.remove_transaction_button = tk.Button(self, text = "Remove transaction", command = lambda: self.open_remove_transaction_window())
        self.remove_transaction_button.pack(pady=30)

        self.display_transactions_button = tk.Button(self, text = "Display transactions", command = lambda: self.display_transactions()) 
        self.display_transactions_button.pack(pady=35)

        self.update_bal_button = tk.Button(self, text="Update Balance", command=self.update_balance_label)
        self.update_bal_button.pack(pady=40,padx=20)
        self.balance_label = tk.Label(self, text=f"Current Balance: ${self.finance_tracker.balance}")
        self.balance_label.pack(pady=40)

    def open_file_dialog(self, finance_tracker):
        """Open the file explorer dialog"""
        self.excel_file_path = filedialog.askopenfilename(title="Select a File")

        if self.excel_file_path:
            print(f"Selected File: {self.excel_file_path}")

        try:
            data = pd.read_excel(self.excel_file_path, header=None)
            pass
        except FileNotFoundError:
            raise TypeError(f"The source file '{self.excel_file_path}' does not exist.")
        
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
        print(f"Data from '{self.excel_file_path}' has been successfully imported")
        self.update_balance_label()

    def display_transactions(self):
        display_window = tk.Toplevel(self)
        display_window.title("All Transactions")

        text_widget = tk.Text(display_window, height=100, width=250)
        text_widget.pack(padx=50,pady=50)

        all_transactions = self.finance_tracker.transactions

        for i, transaction in enumerate(all_transactions, start=1):
            transaction_str = f"{i}) {str(transaction)}\n"
            text_widget.insert(tk.END, transaction_str)

    def clicked_graph_button(self):
        self.finance_tracker.plot_transaction_amounts()
    
    def update_balance_label(self):
        self.balance_label.config(text=f"Current Balance: ${self.finance_tracker.balance}")

    def open_new_transaction_window(self):
        NewTransactionWindow(self, self.finance_tracker, self.excel_file_path)

    def open_remove_transaction_window(self):
        RemoveTransactionWindow(self, self.finance_tracker)

class NewTransactionWindow(tk.Toplevel):
    def __init__(self, parent, finance_tracker, excel_file_path=None):
        super().__init__(parent)
        self.title("New Transaction")

        # Create entry widgets
        self.amount_entry = tk.Entry(self, width=10)
        self.transaction_type_entry = tk.Entry(self, width=20)
        self.category_entry = tk.Entry(self, width=20)
        self.description_entry = tk.Entry(self, width=30)
        self.source_or_payment_entry = tk.Entry(self, width=30)

        # Create labels for entry widgets
        tk.Label(self, text="Amount:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self, text="Type (Income/Expense):").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self, text="Category:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self, text="Description:").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(self, text="Source/Payment Method:").grid(row=4, column=0, padx=10, pady=5)

        # Position entry widgets
        self.amount_entry.grid(row=0, column=1)
        self.transaction_type_entry.grid(row=1, column=1)
        self.category_entry.grid(row=2, column=1)
        self.description_entry.grid(row=3, column=1)
        self.source_or_payment_entry.grid(row=4, column=1)

        # Create button to add the new transaction
        tk.Button(self, text="Add Transaction", command=self.add_new_transaction).grid(row=5, column=0, columnspan=2, pady=10)

        # Store reference to finance tracker
        self.finance_tracker = finance_tracker
        self.excel_file_path = excel_file_path

    def add_new_transaction(self):
        # Retrieve user input from entry widgets
        amount = float(self.amount_entry.get())
        transaction_type = self.transaction_type_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()
        source_or_payment_method = self.source_or_payment_entry.get()
        # If an Excel file path is provided, append the new transaction to the existing data
        if self.excel_file_path:
            # Ensure the order of columns in new_transaction_data matches the Excel file
            new_transaction_data = [amount, transaction_type, category, description, source_or_payment_method]

            # Get the header from the existing Excel file (assuming the first row is the header)
            existing_header = pd.read_excel(self.excel_file_path, nrows=0).columns

            # Create a Series with the correct order of columns
            new_transaction_series = pd.Series(new_transaction_data, index=existing_header)

            # Read the existing data, add new transaction to it, write to excel
            new_data = pd.read_excel(self.excel_file_path)
            new_data = new_data._append(new_transaction_series, ignore_index=True)
            new_data.to_excel(self.excel_file_path, index=False, header=True, engine='openpyxl')

        # Add the new transaction to the finance tracker
        if transaction_type == 'Income':
            new_income_transaction = IncomeTransaction(amount, transaction_type, category, description, source_or_payment_method)
            self.finance_tracker.add_transaction(new_income_transaction)
        elif transaction_type == 'Expense':
            new_expense_transaction = ExpenseTransaction(amount, transaction_type, category, description, source_or_payment_method)
            self.finance_tracker.add_transaction(new_expense_transaction)
        else:
            print(f"Unhandled transaction type: {transaction_type}")

        # Close the window
        self.destroy()

class RemoveTransactionWindow(tk.Toplevel):
    def __init__(self, parent, finance_tracker, excel_file_path=None):
        super().__init__(parent)
        self.title("Remove Transaction")

        # Create entry widgets
        self.transaction_index_entry = tk.Entry(self, width=10)
        tk.Label(self, text="Transaction Index:").grid(row=0, column=0, padx=10, pady=5)
        self.transaction_index_entry.grid(row=0, column=1)

        tk.Button(self, text="Remove Transaction", command=self.remove_transaction).grid(row=5, column=0, columnspan=2, pady=10)

        self.finance_tracker = finance_tracker

    def remove_transaction(self):
        try:
            transaction_index = int(self.transaction_index_entry.get())
            self.finance_tracker.remove_transaction(transaction_index)
            print(f"Removed transaction at index {transaction_index}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except IndexError:
            print("Invalid transaction index.")
        
# Example usage:
if __name__ == "__main__":
    finance_tracker = PersonalFinanceTracker()

    # Adding transactions
    # income_transaction = IncomeTransaction(-1000, "Income","Salary", "Yeah ight", "XYZ Company")
    # expense_transaction = ExpenseTransaction(-50, "Expense","Food", "Groceries", "Credit Card")

    # finance_tracker.add_transaction(income_transaction)
    # finance_tracker.add_transaction(expense_transaction)
    # finance_tracker.add_transaction(example_transaction1)
    # finance_tracker.add_transaction(example_transaction2)

    sample_transaction = Transaction(1000, "Bank Robbery", "Robbed a bank")
    # sample_transaction.display()
    # Displaying balance and transactions
    finance_tracker.show_balance()
    finance_tracker.show_transactions()

    my_gui = Gui(finance_tracker)

    my_gui.mainloop()