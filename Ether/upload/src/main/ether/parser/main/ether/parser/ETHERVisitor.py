# Generated from main/ether/parser/ETHER.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ETHERParser import ETHERParser
else:
    from ETHERParser import ETHERParser

# This class defines a complete generic visitor for a parse tree produced by ETHERParser.

class ETHERVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ETHERParser#program.
    def visitProgram(self, ctx:ETHERParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ETHERParser#send.
    def visitSend(self, ctx:ETHERParser.SendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ETHERParser#sendeth_init.
    def visitSendeth_init(self, ctx:ETHERParser.Sendeth_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ETHERParser#sendeth_more.
    def visitSendeth_more(self, ctx:ETHERParser.Sendeth_moreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ETHERParser#sendeth.
    def visitSendeth(self, ctx:ETHERParser.SendethContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ETHERParser#sendtoken.
    def visitSendtoken(self, ctx:ETHERParser.SendtokenContext):
        return self.visitChildren(ctx)



del ETHERParser