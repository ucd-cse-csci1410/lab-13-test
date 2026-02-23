"""
test_02_bank_account.py

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


from src.bank_account import save_date
from src.Transaction import Transaction




# def save_date (list_of_transactions):
#     output_file = open ('bank_account_data2.txt', 'w')

#     list_of_transactions.sort (key=Transaction.get_date)


#     for trans in list_of_transactions:
#         date = trans.get_date()
#         trans_type = trans.get_transaction_type()
#         amount = trans.get_amount()
#         print ('{0}:{1}:{2:.2f}'.format (date, trans_type, amount), file=output_file)
        
#     output_file.close()
#     print ('Data saved')
            

class TestBankAccountSaveData(unittest.TestCase):
    """Unit tests for save_data method."""

    # case_01: Test save_data method
    def test_01_save_data(self):
        """Test that save_data method saves data to the file."""
        self.original_stdout = patch('sys.stdout', new_callable=StringIO).start()
        self.addCleanup(patch.stopall)

        list_of_transactions = []
        list_of_transactions.append(Transaction("20201105", "deposit", 1000.00))
        list_of_transactions.append(Transaction("20201106", "withdraw", 149.95))
        save_date(list_of_transactions)
        received = self.original_stdout.getvalue()
        expected = "Data saved\n"
        self.assertEqual(received, expected,
                         msg=f"\n Wrong output.\nExpected output: \n{expected}\nReceived output: \n{received}")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestBankAccountSaveData))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)