# Generated from main/ether/parser/ETHER.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("+\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3\3")
        buf.write("\7\3\20\n\3\f\3\16\3\23\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\2\2\6\2\4\6\b\2\2\2(\2\n\3\2\2\2\4\21\3\2")
        buf.write("\2\2\6\24\3\2\2\2\b\36\3\2\2\2\n\13\5\4\3\2\13\f\7\2\2")
        buf.write("\3\f\3\3\2\2\2\r\20\5\b\5\2\16\20\5\6\4\2\17\r\3\2\2\2")
        buf.write("\17\16\3\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2")
        buf.write("\2\22\5\3\2\2\2\23\21\3\2\2\2\24\25\7\b\2\2\25\26\7\4")
        buf.write("\2\2\26\27\7\n\2\2\27\30\7\6\2\2\30\31\7\n\2\2\31\32\7")
        buf.write("\6\2\2\32\33\7\13\2\2\33\34\7\5\2\2\34\35\7\7\2\2\35\7")
        buf.write("\3\2\2\2\36\37\7\t\2\2\37 \7\4\2\2 !\7\n\2\2!\"\7\6\2")
        buf.write("\2\"#\7\n\2\2#$\7\6\2\2$%\7\f\2\2%&\7\6\2\2&\'\7\13\2")
        buf.write("\2\'(\7\5\2\2()\7\7\2\2)\t\3\2\2\2\4\17\21")
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
    RULE_sendeth = 2
    RULE_sendtoken = 3

    ruleNames =  [ "program", "send", "sendeth", "sendtoken" ]

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
            self.state = 8
            self.send()
            self.state = 9
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

        def sendtoken(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ETHERParser.SendtokenContext)
            else:
                return self.getTypedRuleContext(ETHERParser.SendtokenContext,i)


        def sendeth(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ETHERParser.SendethContext)
            else:
                return self.getTypedRuleContext(ETHERParser.SendethContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ETHERParser.SENDETH or _la==ETHERParser.SENDTOKEN:
                self.state = 13
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ETHERParser.SENDTOKEN]:
                    self.state = 11
                    self.sendtoken()
                    pass
                elif token in [ETHERParser.SENDETH]:
                    self.state = 12
                    self.sendeth()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 17
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
        self.enterRule(localctx, 4, self.RULE_sendeth)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(ETHERParser.SENDETH)
            self.state = 19
            self.match(ETHERParser.LB)
            self.state = 20
            self.match(ETHERParser.ADDRESS)
            self.state = 21
            self.match(ETHERParser.COMA)
            self.state = 22
            self.match(ETHERParser.ADDRESS)
            self.state = 23
            self.match(ETHERParser.COMA)
            self.state = 24
            self.match(ETHERParser.AMOUNT)
            self.state = 25
            self.match(ETHERParser.RB)
            self.state = 26
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
        self.enterRule(localctx, 6, self.RULE_sendtoken)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(ETHERParser.SENDTOKEN)
            self.state = 29
            self.match(ETHERParser.LB)
            self.state = 30
            self.match(ETHERParser.ADDRESS)
            self.state = 31
            self.match(ETHERParser.COMA)
            self.state = 32
            self.match(ETHERParser.ADDRESS)
            self.state = 33
            self.match(ETHERParser.COMA)
            self.state = 34
            self.match(ETHERParser.TOKENID)
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





