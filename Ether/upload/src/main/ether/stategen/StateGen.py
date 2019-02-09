from ETHERVisitor import ETHERVisitor
from ETHERParser import ETHERParser
from stateerr import *
from Utils import Utils

class State:
    def __init__(self, address, ):

class StateGen(ETHERVisitor):
    # Visit a parse tree produced by ETHERParser#program.
    def visitProgram(self, ctx:ETHERParser.ProgramContext):
        return self.visit(ctx.send())


    # Visit a parse tree produced by ETHERParser#send.
    def visitSend(self, ctx:ETHERParser.SendContext):
        return [self.visit(ctx.getChild(x)) for x in range(0, ctx.getChildCount() - 1)]


    # Visit a parse tree produced by ETHERParser#sendeth.
    def visitSendeth(self, ctx:ETHERParser.SendethContext):
        pass


    # Visit a parse tree produced by ETHERParser#sendtoken.
    def visitSendtoken(self, ctx:ETHERParser.SendtokenContext):
        pass

    