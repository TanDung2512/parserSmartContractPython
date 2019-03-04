from ETHERVisitor import ETHERVisitor
from ETHERParser import ETHERParser
from stateerr import *
from Utils import Utils


class State:
    def __init__(self, users):
        self.users = users

    def __str__(self):
        return "[" + ", ".join([str(x) for x in self.users]) + "]\n"


class User:
    def __init__(self, Address, Ether, Token):
        self.address = Address
        self.ether = Ether
        self.token = Token

    def __str__(self):
        return self.address + "(" + str(self.ether) + ", " + str(self.token) + ")"


class StateGen(ETHERVisitor):
    State = State([])

    # Visit a parse tree produced by ETHERParser#program.
    def visitProgram(self, ctx: ETHERParser.ProgramContext):
        return self.visit(ctx.send())

    # Visit a parse tree produced by ETHERParser#send.
    def visitSend(self, ctx: ETHERParser.SendContext):
        sendlist = [ctx.getChild(x) for x in range(0, ctx.getChildCount())]
        Users = []
        for x in sendlist:
            if x.ADDRESS(0).getText() not in Users: Users.append(x.ADDRESS(0).getText())
            if x.ADDRESS(1).getText() not in Users: Users.append(x.ADDRESS(1).getText())
        for x in Users:
            self.State.users.append(User(x, 100, 100))
        return [str(self.State)] + [self.visit(x) for x in sendlist]

    # Visit a parse tree produced by ETHERParser#sendeth.
    def visitSendeth(self, ctx: ETHERParser.SendethContext):
        for x in self.State.users:
            if x.address == ctx.ADDRESS(0).getText():
                x.ether -= int(ctx.AMOUNT().getText())
            if x.address == ctx.ADDRESS(1).getText():
                x.ether += int(ctx.AMOUNT().getText())
        return str(self.State)

    # Visit a parse tree produced by ETHERParser#sendtoken.
    def visitSendtoken(self, ctx: ETHERParser.SendtokenContext):
        for x in self.State.users:
            if x.address == ctx.ADDRESS(0).getText():
                x.token -= int(ctx.AMOUNT().getText())
            if x.address == ctx.ADDRESS(1).getText():
                x.token += int(ctx.AMOUNT().getText())
        return str(self.State)


