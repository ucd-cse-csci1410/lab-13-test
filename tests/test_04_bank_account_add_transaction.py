"""
test_04_bank_account_add_transaction.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the BankAccount class.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest
import sys
import os

from io import StringIO
from unittest.mock import patch


solution_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
src_dir = os.path.join(solution_dir, 'src')
sys.path.insert(0, solution_dir)
sys.path.insert(0, src_dir)


from src.bank_account import add_transaction
from src.Transaction import Transaction


# def add_transaction (list_of_transactions):
#     date = input ('Enter date using the format yyyymmdd: ' )
#     trans_type = input ('Enter transaction type: ')
#     amount = float (input ('Enter transaction amount: '))

#     trans = Transaction (date, trans_type, amount)
#     list_of_transactions.append(trans)



            

class TestBankAccountAddTransaction(unittest.TestCase):
    """Unit tests for add_transaction method."""

    # case_01: Test add_transaction method
    def test_01_add_transaction(self):
        """Test that add_transaction method adds a transaction to the list."""

        self.original_stdout = patch('sys.stdout', new_callable=StringIO).start()
        self.addCleanup(patch.stopall)

        list_of_transactions = []
        with patch('builtins.input', side_effect=['20260222', 'deposit', '1000']):
            add_transaction(list_of_transactions)
        received = list_of_transactions[0].get_date()
        expected = "20260222"
        self.assertEqual(received, expected,
                         msg=f"\n Wrong output.\nExpected date: '{expected}'\nReceived date: '{received}'")

        received = list_of_transactions[0].get_transaction_type()
        expected = "deposit"
        self.assertEqual(received, expected,
                         msg=f"\n Wrong output.\nExpected transaction type: '{expected}'\nReceived transaction type: '{received}'")

        received = list_of_transactions[0].get_amount()
        expected = 1000.00
        self.assertEqual(received, expected,
                         msg=f"\n Wrong output.\nExpected amount: '{expected}'\nReceived amount: '{received}'")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestBankAccountAddTransaction))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)