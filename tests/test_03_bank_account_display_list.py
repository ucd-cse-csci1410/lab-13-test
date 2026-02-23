"""
test_03_bank_account_display_list.py

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


from src.bank_account import display_list
from src.Transaction import Transaction




# def display_list (list_of_transactions):
#     list_of_transactions.sort (key=Transaction.get_date)
    
#     print ('List of Transactions')

#     print ('Date       Type                Amount')
#     print ('============================================')

#     for trans in list_of_transactions:
#         date = trans.get_date()
#         trans_type = trans.get_transaction_type()
#         amount = trans.get_amount()
#         print ('{0}     {1:15}     ${2:10.2f}'.format (date, trans_type, amount))

#     print ('===========================================')
#     print ('End of the list')
#     print()



class TestBankAccountDisplayList(unittest.TestCase):
    """Unit tests for display_list method."""

    # case_01: Test display_list method
    def test_01_display_list(self):
        """Test that display_list method displays the list of transactions."""

        self.original_stdout = patch('sys.stdout', new_callable=StringIO).start()
        self.addCleanup(patch.stopall)

        list_of_transactions = []
        list_of_transactions.append(Transaction("20201105", "deposit", 1000.00))
        list_of_transactions.append(Transaction("20201106", "withdraw", 149.95))
        display_list(list_of_transactions)

        received = self.original_stdout.getvalue()
        expected = "List of Transactions\nDate       Type                Amount\n============================================\n20201105     deposit             $   1000.00\n20201106     withdraw            $    149.95\n============================================\nEnd of the list\n"
        self.assertEqual(received, expected,
                         msg=f"\n Wrong output.\nExpected output: \n{expected}\nReceived output: \n{received}")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestBankAccountDisplayList))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)