import unittest
import sys
from io import StringIO
from src.accounting import execute_event


class Test2048(unittest.TestCase):
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
        sys.stdout = sys.__stdout__
        expected_output = """7\n0\n33\n"""
        self.assertEqual(capturedOutput.getvalue(), expected_output)
