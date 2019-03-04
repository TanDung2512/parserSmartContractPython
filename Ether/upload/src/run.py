import sys,os
sys.path.append('./test/')
sys.path.append('./main/ether/parser/')
sys.path.append('./main/ether/utils/')
sys.path.append('./main/ether/astgen/')
sys.path.append('./main/ether/checker/')
sys.path.append('./main/ether/codegen/')
sys.path.append('./main/ether/stategen/')
import subprocess
import unittest
from antlr4 import *

ANTLR_JAR = "/usr/local/lib/antlr-4.7.1-complete.jar"
TARGET_DIR = '../target'
GENERATE_DIR = 'main/ether/parser'

def main(argv):


    if len(argv) < 1:
        printUsage()
    # elif argv[1] == 'gen':
    #     subprocess.run(["java","-jar",ANTLR_JAR,"-o","../target","-no-listener","-visitor","main/ether/parser/ETHER.g4"])
    # elif argv[1] == 'clean':
    #     subprocess.run(["rm","-rf",TARGET_DIR + "/*"])

    if argv[1] == 'test':
        if not os.path.isdir(TARGET_DIR + "/" + GENERATE_DIR):
            subprocess.run(["java","-jar",ANTLR_JAR,"-o",GENERATE_DIR,"-no-listener","-visitor","main/ether/parser/ETHER.g4"])
        if not (TARGET_DIR + "/" + GENERATE_DIR) in sys.path:
            sys.path.append(TARGET_DIR + "/" + GENERATE_DIR)
        if len(argv) < 2:
            printUsage()
        elif argv[2] == 'StateGenSuite':
            from StateGenSuite import StateGenSuite

            getAndTest(StateGenSuite)
        else:
            printUsage()
    else:
        printUsage()



def getAndTest(cls):
    suite = unittest.makeSuite(cls)

    test(suite)

def test(suite):
    from pprint import pprint
    from io import StringIO
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    # print('Tests run ', result.testsRun)
    # print('Errors ', result.errors)
    # print(result.failures)

    # f = open('test/solutions/sendEther.txt','r')
    # print(f.read())
    stream.seek(0)
    #print('Test output\n', stream.read())

def printUsage():
    print("python3 run.py gen")
    print("python3 run.py test LexerSuite")
    print("python3 run.py test ParserSuite")
    print("python3 run.py test ASTGenSuite")
    print("python3 run.py test CheckerSuite")
    print("python3 run.py test CodeGenSuite")

if __name__ == "__main__":

   main(sys.argv[1:])

