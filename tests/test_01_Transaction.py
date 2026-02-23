"""
test_01_Transaction.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the Transaction class.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.Transaction import Transaction 

# class Transaction:
#     """Transaction class which keep track of a bank transaction"""
       

#     def __init__(self, date, transaction_type, amount):
#         """Initialize instance variables date, type, and amount"""
#         self.date = date
#         self.transaction_type = transaction_type
#         self.amount = amount

#     def get_date (self):
#         """Returns transaction date"""
#         return self.date

#     def get_transaction_type (self):
#         """Returns transaction type"""
#         return self.transaction_type

#     def get_amount (self):
#         """Returns transaction amount"""
#         return self.amount


class TestTransaction(unittest.TestCase):
    """Unit tests for Transaction class."""

    # case_01: get_date() should return the date of the transaction.
    def test_01_get_date(self):
        """get_date() should return the date of the transaction."""

        received = Transaction("2026-02-22", "Deposit", 1000).get_date()
        expected = "2026-02-22"
        self.assertEqual(
            received,
            expected, 
            msg=f"\n Wrong output.\nExpected date: '{expected}'\nReceived date: '{received}'")
    # case_02: get_transaction_type() should return the type of the transaction.
    def test_02_get_transaction_type(self):
        """get_transaction_type() should return the type of the transaction."""

        received = Transaction("2026-02-22", "Deposit", 1000).get_transaction_type()
        expected = "Deposit"
        self.assertEqual(
            received,
            expected, 
            msg=f"\n Wrong output.\nExpected transaction type: '{expected}'\nReceived transaction type: '{received}'")
    # case_03: get_amount() should return the amount of the transaction.
    def test_03_get_amount(self):
        """get_amount() should return the amount of the transaction."""

        received = Transaction("2026-02-22", "Deposit", 1000).get_amount()
        expected = 1000
        self.assertEqual(
            received,
            expected, 
            msg=f"\n Wrong output.\nExpected amount: '{expected}'\nReceived amount: '{received}'")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestTransaction))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)