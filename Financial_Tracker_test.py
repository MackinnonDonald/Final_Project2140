from Financial_Tracker import *
import unittest

class TestFinanceTracker(unittest.TestCase):
    
    def test_create_tracker(self):
        """Testing if an instance of PersonalFinanceTracker can be created successfully"""
        sample_tracker = PersonalFinanceTracker()
        self.assertIsInstance(sample_tracker, PersonalFinanceTracker)

    def test_create_transaction(self):
        """Testing the Transaction class and its functions"""

        sample_transaction = Transaction(1000.02, "Bank Robbery", "Robbed a bank")
        expected_result = "Amount: $1000.02, Category: Bank Robbery, Description: Robbed a bank"
        self.assertIsInstance(sample_transaction, Transaction)
        self.assertEqual(sample_transaction.display(), expected_result)

        sample_transaction2 = Transaction(-10500.32, "Felony Charges", "Pleaded guilty")
        expected_result2 = "Amount: $-10500.32, Category: Felony Charges, Description: Pleaded guilty"
        self.assertIsInstance(sample_transaction2, Transaction)
        self.assertEqual(sample_transaction2.display(), expected_result2)

    def test_create_income_transaction(self):
        """Testing the IncomeTransaction class and its functions"""
        sample_income_transaction = IncomeTransaction(2000.12, "Income", "Salary", "40 hour week", "Work")
        expected_result3 = "Amount: $2000.12, Type: Income, Category: Salary, Description: 40 hour week, Source: Work"
        self.assertIsInstance(sample_income_transaction, IncomeTransaction)
        self.assertEqual(sample_income_transaction.display(), expected_result3)

    def test_invalid_income_transaction(self):
        """Tests invalid types of income transactions and the errors raised"""
        with self.assertRaises(ValueError):
            invalid_income_transaction = IncomeTransaction(-413.23, "Income", "Salary", "Income Taxes", "IRS")
        with self.assertRaises(TypeError):
            invalid_income_transaction2 = IncomeTransaction('1738.01', "Income", "Donation", "Tax Refund", "IRS")


    def test_create_expense_transaction(self):
        """Testing the ExpenseTransaction class and its functions"""
        sample_expense_transaction = ExpenseTransaction(-100.24, "Expense", "Grocerries", "WholeFoods", "Credit Card")
        expected_result4 = "Amount: $-100.24, Type: Expense, Category: Grocerries, Description: WholeFoods, Payment Method: Credit Card"
        self.assertIsInstance(sample_expense_transaction, ExpenseTransaction)
        self.assertEqual(sample_expense_transaction.display(), expected_result4)

    def test_invalid_expense_transaction(self):
        """Tests invalid types of income transactions and the errors raised"""
        with self.assertRaises(ValueError):
            invalid_income_transaction = ExpenseTransaction(413.23, "Expense", "Refund", 123, "Debit Card")
        with self.assertRaises(TypeError):
            invalid_income_transaction2 = IncomeTransaction('-178.21', "Expense", "Five Guys", "Keeping it real", "Credit Card")

if __name__ == '__main__':
    unittest.main()
