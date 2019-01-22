import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lơercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    