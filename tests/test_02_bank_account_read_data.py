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



solution_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
src_dir = os.path.join(solution_dir, 'src')
sys.path.insert(0, solution_dir)
sys.path.insert(0, src_dir)




from src.bank_account import read_data



# def read_data (list_of_transactions):
#     input_file = open ('bank_account_data.txt', 'r')


#     for line in input_file:
#         split_list = line.split(':')
#         trans = Transaction (split_list[0], split_list[1], float(split_list[2]))
#         list_of_transactions.append (trans)

#     input_file.close()
    

            

class TestBankAccountReadData(unittest.TestCase):
    """Unit tests for read_data method."""

    # case_01: Test read_data method
    def test_01_read_data(self):
        """Test that read_data method reads data from the file."""

        list_of_transactions = []
        read_data(list_of_transactions)

        received = list_of_transactions[0].get_date()
        expected = "20201105"
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

        received = list_of_transactions[1].get_date()
        expected = "20201106"
        self.assertEqual(received, expected,
                         msg=f"\n Wrong output.\nExpected date: '{expected}'\nReceived date: '{received}'")

        received = list_of_transactions[1].get_transaction_type()
        expected = "withdraw"
        self.assertEqual(received, expected,
                         msg=f"\n Wrong output.\nExpected transaction type: '{expected}'\nReceived transaction type: '{received}'")

        received = list_of_transactions[1].get_amount()
        expected = 149.95
        self.assertEqual(received, expected,
                         msg=f"\n Wrong output.\nExpected amount: '{expected}'\nReceived amount: '{received}'")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestBankAccountReadData))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)