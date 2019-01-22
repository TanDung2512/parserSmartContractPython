from ETHERVisitor import ETHERVisitor
from ETHERParser import ETHERParser
from stateerr import *


class States:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
    def __str__(self):
        return "[" + str(self.user1) + "\t, " + str(self.user2) + "]"

class User:
    def __init__(self, userAddress, ether, token):
        self.userAddress = userAddress
        self.ether = ether
        self.token = token
    def __str__(self):
        return self.userAddress + "(" + str(self.ether) + ", " + str(self.token) + ")"

class StateGen(ETHERVisitor):
    # Visit a parse tree produced by ETHERParser#program.
    initState = True

    sender = None
    receiver = None

    def visitProgram(self, ctx:ETHERParser.ProgramContext):
        return self.visit(ctx.send())


    # Visit a parse tree produced by ETHERParser#send.
    def visitSend(self, ctx:ETHERParser.SendContext):
        stateSendEtherInit = self.visit(ctx.sendeth_init()) # return list

        stateSendToken = self.visit(ctx.sendtoken()) # return list

        stateSendEtherMore = self.visit(ctx.sendeth_more()) # return list

        return stateSendEtherInit + '\n' + stateSendToken + '\n' + stateSendEtherMore + '\n'


    # Visit a parse tree produced by ETHERParser#sendeth_init.
    def visitSendeth_init(self, ctx:ETHERParser.Sendeth_initContext):
        stateSendEther = [self.visit(x) for x in ctx.sendeth()]


        return '\n'.join(str(x) for x in stateSendEther)


    # Visit a parse tree produced by ETHERParser#sendeth_more.
    def visitSendeth_more(self, ctx:ETHERParser.Sendeth_moreContext):
        if len(ctx.sendeth()) == 0:
            return ""

        stateSendEther = [self.visit(x) for x in ctx.sendeth()]

        return '\n'.join(str(x) for x in stateSendEther)


    # Visit a parse tree produced by ETHERParser#sendeth.
    def visitSendeth(self, ctx:ETHERParser.SendethContext):
        state = []

        if StateGen.initState == True:
            state.append(States(User(ctx.ADDRESS(0).getText(), 100, 1), User(ctx.ADDRESS(1).getText(), 100, 1)))

            StateGen.initState = False

            StateGen.sender = User(ctx.ADDRESS(0).getText(), 100, 1)
            StateGen.receiver = User(ctx.ADDRESS(1).getText(), 100, 1)

            amount = int(ctx.AMOUNT().getText())

            if (StateGen.sender.ether < amount):
                raise InvalidAmount(amount)

            StateGen.sender.ether -= amount
            StateGen.receiver.ether += amount

            state.append(States(StateGen.sender, StateGen.receiver))

            return '\n'.join(str(x) for x in state)

        else:
            amount = int(ctx.AMOUNT().getText())

            if (StateGen.sender.ether < amount):
                raise InvalidAmount(amount)

            StateGen.sender.ether -= amount
            StateGen.receiver.ether += amount

            return str(States(StateGen.sender, StateGen.receiver))

    # Visit a parse tree produced by ETHERParser#sendtoken.
    def visitSendtoken(self, ctx:ETHERParser.SendtokenContext):

        amount = int(ctx.AMOUNT().getText())

        if (StateGen.receiver.token < amount):
            raise InvalidAmount(amount)

        StateGen.sender.token += amount
        StateGen.receiver.token -= amount

        return str(States(StateGen.sender, StateGen.receiver))

        
