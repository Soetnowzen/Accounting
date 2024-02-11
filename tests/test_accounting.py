import unittest
import sys
from io import StringIO
from src.accounting import execute_event


class Test2048(unittest.TestCase):
    def setUp(self):
        self.saved_stdout = sys.stdout

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_sample_input_1(self):
        """
        Input:
        3 5
        SET 1 7
        PRINT 1
        PRINT 2
        RESTART 33
        PRINT 1

        expected output
        7
        0
        33
        """
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        input_string = """SET 1 7\nPRINT 1\nPRINT 2\nRESTART 33\nPRINT 1"""
        execute_event(3, 5, input_string)
        expected_output = """7\n0\n33\n"""
        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_sample_input_2(self):
        """
        Input:
        5 7
        RESTART 5
        SET 3 7
        PRINT 1
        PRINT 2
        PRINT 3
        PRINT 4
        PRINT 5

        expected output
        5
        5
        7
        5
        5
        """
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        input_string = """RESTART 5\nSET 3 7\nPRINT 1\nPRINT 2\nPRINT 3\nPRINT 4\nPRINT 5"""
        execute_event(5, 7, input_string)
        expected_output = """5\n5\n7\n5\n5\n"""
        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_invalid_input(self):
        """
        Test behavior with invalid input
        """
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        input_string = """SET 1 7\nPRINT 1\nINVALID_COMMAND\nRESTART -1\nPRINT 1"""
        execute_event(3, 5, input_string)
        expected_output = """7\nUnknown command ['INVALID_COMMAND']\n7\n"""
        self.assertEqual(capturedOutput.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
