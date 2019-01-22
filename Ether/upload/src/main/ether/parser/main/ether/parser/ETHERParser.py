# Generated from main/ether/parser/ETHER.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\67\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\6\4\27\n\4\r\4\16\4\30")
        buf.write("\3\5\7\5\34\n\5\f\5\16\5\37\13\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2\62\2\16\3\2\2")
        buf.write("\2\4\21\3\2\2\2\6\26\3\2\2\2\b\35\3\2\2\2\n \3\2\2\2\f")
        buf.write("*\3\2\2\2\16\17\5\4\3\2\17\20\7\2\2\3\20\3\3\2\2\2\21")
        buf.write("\22\5\6\4\2\22\23\5\f\7\2\23\24\5\b\5\2\24\5\3\2\2\2\25")
        buf.write("\27\5\n\6\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2")
        buf.write("\30\31\3\2\2\2\31\7\3\2\2\2\32\34\5\n\6\2\33\32\3\2\2")
        buf.write("\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\t\3\2")
        buf.write("\2\2\37\35\3\2\2\2 !\7\b\2\2!\"\7\4\2\2\"#\7\n\2\2#$\7")
        buf.write("\6\2\2$%\7\n\2\2%&\7\6\2\2&\'\7\13\2\2\'(\7\5\2\2()\7")
        buf.write("\7\2\2)\13\3\2\2\2*+\7\t\2\2+,\7\4\2\2,-\7\n\2\2-.\7\6")
        buf.write("\2\2./\7\n\2\2/\60\7\6\2\2\60\61\7\f\2\2\61\62\7\6\2\2")
        buf.write("\62\63\7\13\2\2\63\64\7\5\2\2\64\65\7\7\2\2\65\r\3\2\2")
        buf.write("\2\4\30\35")
        return buf.getvalue()


class ETHERParser ( Parser ):

    grammarFileName = "ETHER.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "WS", "LB", "RB", "COMA", "SEMI", "SENDETH", 
                      "SENDTOKEN", "ADDRESS", "AMOUNT", "TOKENID", "ERRORTOK" ]

    RULE_program = 0
    RULE_send = 1
    RULE_sendeth_init = 2
    RULE_sendeth_more = 3
    RULE_sendeth = 4
    RULE_sendtoken = 5

    ruleNames =  [ "program", "send", "sendeth_init", "sendeth_more", "sendeth", 
                   "sendtoken" ]

    EOF = Token.EOF
    WS=1
    LB=2
    RB=3
    COMA=4
    SEMI=5
    SENDETH=6
    SENDTOKEN=7
    ADDRESS=8
    AMOUNT=9
    TOKENID=10
    ERRORTOK=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def send(self):
            return self.getTypedRuleContext(ETHERParser.SendContext,0)


        def EOF(self):
            return self.getToken(ETHERParser.EOF, 0)

        def getRuleIndex(self):
            return ETHERParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ETHERParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.send()
            self.state = 13
            self.match(ETHERParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SendContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sendeth_init(self):
            return self.getTypedRuleContext(ETHERParser.Sendeth_initContext,0)


        def sendtoken(self):
            return self.getTypedRuleContext(ETHERParser.SendtokenContext,0)


        def sendeth_more(self):
            return self.getTypedRuleContext(ETHERParser.Sendeth_moreContext,0)


        def getRuleIndex(self):
            return ETHERParser.RULE_send

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSend" ):
                return visitor.visitSend(self)
            else:
                return visitor.visitChildren(self)




    def send(self):

        localctx = ETHERParser.SendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_send)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.sendeth_init()
            self.state = 16
            self.sendtoken()
            self.state = 17
            self.sendeth_more()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sendeth_initContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sendeth(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ETHERParser.SendethContext)
            else:
                return self.getTypedRuleContext(ETHERParser.SendethContext,i)


        def getRuleIndex(self):
            return ETHERParser.RULE_sendeth_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSendeth_init" ):
                return visitor.visitSendeth_init(self)
            else:
                return visitor.visitChildren(self)




    def sendeth_init(self):

        localctx = ETHERParser.Sendeth_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sendeth_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 19
                self.sendeth()
                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ETHERParser.SENDETH):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Sendeth_moreContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sendeth(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ETHERParser.SendethContext)
            else:
                return self.getTypedRuleContext(ETHERParser.SendethContext,i)


        def getRuleIndex(self):
            return ETHERParser.RULE_sendeth_more

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSendeth_more" ):
                return visitor.visitSendeth_more(self)
            else:
                return visitor.visitChildren(self)




    def sendeth_more(self):

        localctx = ETHERParser.Sendeth_moreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sendeth_more)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ETHERParser.SENDETH:
                self.state = 24
                self.sendeth()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SendethContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SENDETH(self):
            return self.getToken(ETHERParser.SENDETH, 0)

        def LB(self):
            return self.getToken(ETHERParser.LB, 0)

        def ADDRESS(self, i:int=None):
            if i is None:
                return self.getTokens(ETHERParser.ADDRESS)
            else:
                return self.getToken(ETHERParser.ADDRESS, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ETHERParser.COMA)
            else:
                return self.getToken(ETHERParser.COMA, i)

        def AMOUNT(self):
            return self.getToken(ETHERParser.AMOUNT, 0)

        def RB(self):
            return self.getToken(ETHERParser.RB, 0)

        def SEMI(self):
            return self.getToken(ETHERParser.SEMI, 0)

        def getRuleIndex(self):
            return ETHERParser.RULE_sendeth

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSendeth" ):
                return visitor.visitSendeth(self)
            else:
                return visitor.visitChildren(self)




    def sendeth(self):

        localctx = ETHERParser.SendethContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sendeth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(ETHERParser.SENDETH)
            self.state = 31
            self.match(ETHERParser.LB)
            self.state = 32
            self.match(ETHERParser.ADDRESS)
            self.state = 33
            self.match(ETHERParser.COMA)
            self.state = 34
            self.match(ETHERParser.ADDRESS)
            self.state = 35
            self.match(ETHERParser.COMA)
            self.state = 36
            self.match(ETHERParser.AMOUNT)
            self.state = 37
            self.match(ETHERParser.RB)
            self.state = 38
            self.match(ETHERParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SendtokenContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SENDTOKEN(self):
            return self.getToken(ETHERParser.SENDTOKEN, 0)

        def LB(self):
            return self.getToken(ETHERParser.LB, 0)

        def ADDRESS(self, i:int=None):
            if i is None:
                return self.getTokens(ETHERParser.ADDRESS)
            else:
                return self.getToken(ETHERParser.ADDRESS, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ETHERParser.COMA)
            else:
                return self.getToken(ETHERParser.COMA, i)

        def TOKENID(self):
            return self.getToken(ETHERParser.TOKENID, 0)

        def AMOUNT(self):
            return self.getToken(ETHERParser.AMOUNT, 0)

        def RB(self):
            return self.getToken(ETHERParser.RB, 0)

        def SEMI(self):
            return self.getToken(ETHERParser.SEMI, 0)

        def getRuleIndex(self):
            return ETHERParser.RULE_sendtoken

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSendtoken" ):
                return visitor.visitSendtoken(self)
            else:
                return visitor.visitChildren(self)




    def sendtoken(self):

        localctx = ETHERParser.SendtokenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sendtoken)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(ETHERParser.SENDTOKEN)
            self.state = 41
            self.match(ETHERParser.LB)
            self.state = 42
            self.match(ETHERParser.ADDRESS)
            self.state = 43
            self.match(ETHERParser.COMA)
            self.state = 44
            self.match(ETHERParser.ADDRESS)
            self.state = 45
            self.match(ETHERParser.COMA)
            self.state = 46
            self.match(ETHERParser.TOKENID)
            self.state = 47
            self.match(ETHERParser.COMA)
            self.state = 48
            self.match(ETHERParser.AMOUNT)
            self.state = 49
            self.match(ETHERParser.RB)
            self.state = 50
            self.match(ETHERParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





