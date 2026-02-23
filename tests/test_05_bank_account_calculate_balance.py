"""
test_05_bank_account_calculate_balance.py

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


from src.bank_account import calculate_balance
from src.Transaction import Transaction



# def calculate_balance (list_of_transactions):

#     balance = 0.0

#     for trans in list_of_transactions:
#         trans_type = trans.get_transaction_type()
#         amount = trans.get_amount()
#         if (trans_type == 'deposit'):
#             balance = balance + amount
#         elif (trans_type == 'withdraw'):
#             balance = balance - amount
#         elif (trans_type == 'bank charge'):
#             balance = balance - amount
#         elif (trans_type == 'interest'):
#             balance = balance + amount

#     print ('Current balance is ${0:.2f}'.format(balance))
            
        
class TestBankAccountCalculateBalance(unittest.TestCase):
    """Unit tests for calculate_balance method."""

    # case_01: Test calculate_balance method
    def test_01_calculate_balance(self):
        """Test that calculate_balance method calculates the balance."""

        self.original_stdout = patch('sys.stdout', new_callable=StringIO).start()
        self.addCleanup(patch.stopall)

        list_of_transactions = []
        list_of_transactions.append(Transaction("20201105", "deposit", 1000.00))
        list_of_transactions.append(Transaction("20201106", "withdraw", 149.95))
        calculate_balance(list_of_transactions)
        received = self.original_stdout.getvalue()
        expected = "Current balance is $850.05\n"
        self.assertEqual(received, expected,
                         msg=f"\n Wrong output.\nExpected output: \n{expected}\nReceived output: \n{received}")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestBankAccountCalculateBalance))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)