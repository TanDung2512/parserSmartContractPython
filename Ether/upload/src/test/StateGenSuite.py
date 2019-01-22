import unittest
from TestUtils import TestStateGen

class StateGenSuite(unittest.TestCase):
    def test(self):
        """Simple program: int main() {} """
        input = """sendeth(0xAAAA, 0xBBBB, 30);\nsendtoken(0xBBBB, 0xAAAA, 1);\nsendeth(0xAAAA, 0xBBBB, 30);\nsendeth(0xAAAA, 0xBBBB, 40);\nsendtoken(0xAAAA, 0xBBBB, 1);\n"""
        expect = ""
        self.assertTrue(TestStateGen.test(input,expect,1))