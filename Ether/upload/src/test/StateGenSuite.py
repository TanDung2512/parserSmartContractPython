import unittest
from TestUtils import TestStateGen
import os
class StateGenSuite(unittest.TestCase):
    def test(self):
        # input = """
        # sendeth(0xAAAA, 0xBBBB, 30);\n
        # sendtoken(0xCCCC, 0xAAAA, EUR,10);\n
        # sendeth(0xAAAA, 0xDDDD, 40);\n
        # sendeth(0xAAAA, 0xBBBB,USD ,40);\n
        # sendtoken(0xAAAA, 0xBBBB, 1);\n
        # """
        fileread = open('test/testcases/sendEther.txt',"r")
        input = str(fileread.read())
        expect = ""
        self.assertTrue(TestStateGen.test(input,expect,1))