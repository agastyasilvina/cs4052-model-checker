# Generated from Formula.g4 by ANTLR 4.13.2
# encoding: utf-8
# Updated 01/03/2025 for indentation fixing (Agastya Silvina)
from antlr4 import *
from io import StringIO
import sys

from simple_model_checker.grammar.formula import Formula

if sys.version_info[1] > 5:
	from typing import TextIO


def serializedATN():
    return [
        4,1,15,167,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,31,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,135,8,1,1,1,1,1,1,1,3,
        1,140,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,165,8,7,1,7,0,0,8,0,2,
        4,6,8,10,12,14,0,0,179,0,16,1,0,0,0,2,139,1,0,0,0,4,141,1,0,0,0,
        6,144,1,0,0,0,8,147,1,0,0,0,10,150,1,0,0,0,12,153,1,0,0,0,14,164,
        1,0,0,0,16,17,3,2,1,0,17,18,5,0,0,1,18,19,6,0,-1,0,19,1,1,0,0,0,
        20,21,5,6,0,0,21,140,6,1,-1,0,22,23,5,7,0,0,23,140,6,1,-1,0,24,25,
        5,11,0,0,25,30,3,4,2,0,26,27,3,14,7,0,27,28,3,6,3,0,28,29,6,1,-1,
        0,29,31,1,0,0,0,30,26,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,33,
        5,12,0,0,33,34,6,1,-1,0,34,140,1,0,0,0,35,36,5,11,0,0,36,37,3,4,
        2,0,37,38,3,14,7,0,38,39,3,10,5,0,39,40,5,12,0,0,40,41,6,1,-1,0,
        41,140,1,0,0,0,42,43,3,12,6,0,43,44,3,8,4,0,44,45,6,1,-1,0,45,140,
        1,0,0,0,46,47,5,11,0,0,47,52,3,8,4,0,48,49,3,14,7,0,49,50,3,10,5,
        0,50,51,6,1,-1,0,51,53,1,0,0,0,52,48,1,0,0,0,52,53,1,0,0,0,53,54,
        1,0,0,0,54,55,5,12,0,0,55,56,6,1,-1,0,56,140,1,0,0,0,57,58,5,9,0,
        0,58,59,5,11,0,0,59,60,3,4,2,0,60,61,5,10,0,0,61,62,3,6,3,0,62,63,
        5,12,0,0,63,64,6,1,-1,0,64,140,1,0,0,0,65,66,5,8,0,0,66,67,5,11,
        0,0,67,68,3,4,2,0,68,69,5,10,0,0,69,70,3,6,3,0,70,71,5,12,0,0,71,
        72,6,1,-1,0,72,140,1,0,0,0,73,74,5,9,0,0,74,75,5,11,0,0,75,76,3,
        4,2,0,76,77,5,10,0,0,77,78,3,10,5,0,78,79,5,12,0,0,79,80,6,1,-1,
        0,80,140,1,0,0,0,81,82,5,8,0,0,82,83,5,11,0,0,83,84,3,4,2,0,84,85,
        5,10,0,0,85,86,3,10,5,0,86,87,5,12,0,0,87,88,6,1,-1,0,88,140,1,0,
        0,0,89,90,5,9,0,0,90,91,5,11,0,0,91,92,3,8,4,0,92,93,5,10,0,0,93,
        94,3,10,5,0,94,95,5,12,0,0,95,96,6,1,-1,0,96,140,1,0,0,0,97,98,5,
        8,0,0,98,99,5,11,0,0,99,100,3,8,4,0,100,101,5,10,0,0,101,102,3,10,
        5,0,102,103,5,12,0,0,103,104,6,1,-1,0,104,140,1,0,0,0,105,106,5,
        14,0,0,106,107,5,11,0,0,107,108,3,4,2,0,108,109,3,14,7,0,109,110,
        3,6,3,0,110,111,5,12,0,0,111,112,6,1,-1,0,112,140,1,0,0,0,113,114,
        5,14,0,0,114,115,5,11,0,0,115,116,3,4,2,0,116,117,5,12,0,0,117,118,
        6,1,-1,0,118,140,1,0,0,0,119,120,5,14,0,0,120,121,5,11,0,0,121,122,
        3,4,2,0,122,123,3,14,7,0,123,124,3,10,5,0,124,125,5,12,0,0,125,126,
        6,1,-1,0,126,140,1,0,0,0,127,128,5,14,0,0,128,129,5,11,0,0,129,134,
        3,8,4,0,130,131,3,14,7,0,131,132,3,10,5,0,132,133,6,1,-1,0,133,135,
        1,0,0,0,134,130,1,0,0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,137,
        5,12,0,0,137,138,6,1,-1,0,138,140,1,0,0,0,139,20,1,0,0,0,139,22,
        1,0,0,0,139,24,1,0,0,0,139,35,1,0,0,0,139,42,1,0,0,0,139,46,1,0,
        0,0,139,57,1,0,0,0,139,65,1,0,0,0,139,73,1,0,0,0,139,81,1,0,0,0,
        139,89,1,0,0,0,139,97,1,0,0,0,139,105,1,0,0,0,139,113,1,0,0,0,139,
        119,1,0,0,0,139,127,1,0,0,0,140,3,1,0,0,0,141,142,5,13,0,0,142,143,
        6,2,-1,0,143,5,1,0,0,0,144,145,5,13,0,0,145,146,6,3,-1,0,146,7,1,
        0,0,0,147,148,3,2,1,0,148,149,6,4,-1,0,149,9,1,0,0,0,150,151,3,2,
        1,0,151,152,6,5,-1,0,152,11,1,0,0,0,153,154,5,1,0,0,154,155,6,6,
        -1,0,155,13,1,0,0,0,156,157,5,2,0,0,157,165,6,7,-1,0,158,159,5,3,
        0,0,159,165,6,7,-1,0,160,161,5,4,0,0,161,165,6,7,-1,0,162,163,5,
        5,0,0,163,165,6,7,-1,0,164,156,1,0,0,0,164,158,1,0,0,0,164,160,1,
        0,0,0,164,162,1,0,0,0,165,15,1,0,0,0,5,30,52,134,139,164
    ]

class FormulaParser ( Parser ):

    grammarFileName = "Formula.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'!'", "'&&'", "'||'", "'=>'", "'<=>'", 
                     "'True'", "'False'", "'A'", "'E'", "<INVALID>", "'('", 
                     "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "TRUE", "FALSE", "ALL", 
                      "EXISTS", "UNTIL", "OPEN", "CLOSE", "ATOMIC", "TEMPORAL", 
                      "WS" ]

    RULE_query = 0
    RULE_formula = 1
    RULE_first = 2
    RULE_second = 3
    RULE_ctl_init = 4
    RULE_ctl_end = 5
    RULE_neg = 6
    RULE_op_bool = 7

    ruleNames =  [ "query", "formula", "first", "second", "ctl_init", "ctl_end", 
                   "neg", "op_bool" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    TRUE=6
    FALSE=7
    ALL=8
    EXISTS=9
    UNTIL=10
    OPEN=11
    CLOSE=12
    ATOMIC=13
    TEMPORAL=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self._formula = None # FormulaContext

        def formula(self):
            return self.getTypedRuleContext(FormulaParser.FormulaContext,0)


        def EOF(self):
            return self.getToken(FormulaParser.EOF, 0)

        def getRuleIndex(self):
            return FormulaParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = FormulaParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            localctx._formula = self.formula()
            self.state = 17
            self.match(FormulaParser.EOF)
            localctx.result = localctx._formula.result
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self.op = False
            self._first = None # FirstContext
            self._op_bool = None # Op_boolContext
            self._second = None # SecondContext
            self._ctl_end = None # Ctl_endContext
            self._neg = None # NegContext
            self._ctl_init = None # Ctl_initContext
            self._UNTIL = None # Token
            self._TEMPORAL = None # Token

        def TRUE(self):
            return self.getToken(FormulaParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(FormulaParser.FALSE, 0)

        def OPEN(self):
            return self.getToken(FormulaParser.OPEN, 0)

        def first(self):
            return self.getTypedRuleContext(FormulaParser.FirstContext,0)


        def CLOSE(self):
            return self.getToken(FormulaParser.CLOSE, 0)

        def op_bool(self):
            return self.getTypedRuleContext(FormulaParser.Op_boolContext,0)


        def second(self):
            return self.getTypedRuleContext(FormulaParser.SecondContext,0)


        def ctl_end(self):
            return self.getTypedRuleContext(FormulaParser.Ctl_endContext,0)


        def neg(self):
            return self.getTypedRuleContext(FormulaParser.NegContext,0)


        def ctl_init(self):
            return self.getTypedRuleContext(FormulaParser.Ctl_initContext,0)


        def EXISTS(self):
            return self.getToken(FormulaParser.EXISTS, 0)

        def UNTIL(self):
            return self.getToken(FormulaParser.UNTIL, 0)

        def ALL(self):
            return self.getToken(FormulaParser.ALL, 0)

        def TEMPORAL(self):
            return self.getToken(FormulaParser.TEMPORAL, 0)

        def getRuleIndex(self):
            return FormulaParser.RULE_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormula" ):
                listener.enterFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormula" ):
                listener.exitFormula(self)




    def formula(self):

        localctx = FormulaParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_formula)
        self._la = 0 # Token type
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(FormulaParser.TRUE)
                localctx.result = Formula(True)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(FormulaParser.FALSE)
                localctx.result = Formula(False)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.match(FormulaParser.OPEN)
                self.state = 25
                localctx._first = self.first()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0):
                    self.state = 26
                    localctx._op_bool = self.op_bool()
                    self.state = 27
                    localctx._second = self.second()
                    localctx.op = True


                self.state = 32
                self.match(FormulaParser.CLOSE)

                if localctx.op:
                    localctx.result = Formula(localctx._first.result, localctx._second.result, localctx._op_bool.result)
                else:
                    localctx.result = Formula(localctx._first.result)
                        
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(FormulaParser.OPEN)
                self.state = 36
                localctx._first = self.first()
                self.state = 37
                localctx._op_bool = self.op_bool()
                self.state = 38
                localctx._ctl_end = self.ctl_end()
                self.state = 39
                self.match(FormulaParser.CLOSE)
                localctx.result = Formula(localctx._first.result, localctx._ctl_end.result, localctx._op_bool.result)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                localctx._neg = self.neg()
                self.state = 43
                localctx._ctl_init = self.ctl_init()
                localctx.result = Formula(localctx._neg.result, localctx._ctl_init.result)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 46
                self.match(FormulaParser.OPEN)
                self.state = 47
                localctx._ctl_init = self.ctl_init()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0):
                    self.state = 48
                    localctx._op_bool = self.op_bool()
                    self.state = 49
                    localctx._ctl_end = self.ctl_end()
                    localctx.op = True


                self.state = 54
                self.match(FormulaParser.CLOSE)

                if localctx.op:
                    localctx.result = Formula(localctx._ctl_init.result, localctx._ctl_end.result, localctx._op_bool.result)
                else:
                    localctx.result = localctx._ctl_init.result
                        
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 57
                self.match(FormulaParser.EXISTS)
                self.state = 58
                self.match(FormulaParser.OPEN)
                self.state = 59
                localctx._first = self.first()
                self.state = 60
                localctx._UNTIL = self.match(FormulaParser.UNTIL)
                self.state = 61
                localctx._second = self.second()
                self.state = 62
                self.match(FormulaParser.CLOSE)
                localctx.result = Formula("E", localctx._first.result, localctx._second.result, (None if localctx._UNTIL is None else localctx._UNTIL.text))
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 65
                self.match(FormulaParser.ALL)
                self.state = 66
                self.match(FormulaParser.OPEN)
                self.state = 67
                localctx._first = self.first()
                self.state = 68
                localctx._UNTIL = self.match(FormulaParser.UNTIL)
                self.state = 69
                localctx._second = self.second()
                self.state = 70
                self.match(FormulaParser.CLOSE)
                localctx.result = Formula("A", localctx._first.result, localctx._second.result, (None if localctx._UNTIL is None else localctx._UNTIL.text))
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 73
                self.match(FormulaParser.EXISTS)
                self.state = 74
                self.match(FormulaParser.OPEN)
                self.state = 75
                localctx._first = self.first()
                self.state = 76
                localctx._UNTIL = self.match(FormulaParser.UNTIL)
                self.state = 77
                localctx._ctl_end = self.ctl_end()
                self.state = 78
                self.match(FormulaParser.CLOSE)
                localctx.result = Formula("E", localctx._first.result, localctx._ctl_end.result, (None if localctx._UNTIL is None else localctx._UNTIL.text))
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 81
                self.match(FormulaParser.ALL)
                self.state = 82
                self.match(FormulaParser.OPEN)
                self.state = 83
                localctx._first = self.first()
                self.state = 84
                localctx._UNTIL = self.match(FormulaParser.UNTIL)
                self.state = 85
                localctx._ctl_end = self.ctl_end()
                self.state = 86
                self.match(FormulaParser.CLOSE)
                localctx.result = Formula("A", localctx._first.result, localctx._ctl_end.result, (None if localctx._UNTIL is None else localctx._UNTIL.text))
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 89
                self.match(FormulaParser.EXISTS)
                self.state = 90
                self.match(FormulaParser.OPEN)
                self.state = 91
                localctx._ctl_init = self.ctl_init()
                self.state = 92
                localctx._UNTIL = self.match(FormulaParser.UNTIL)
                self.state = 93
                localctx._ctl_end = self.ctl_end()
                self.state = 94
                self.match(FormulaParser.CLOSE)
                localctx.result = Formula("E", localctx._ctl_init.result, localctx._ctl_end.result, (None if localctx._UNTIL is None else localctx._UNTIL.text))
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 97
                self.match(FormulaParser.ALL)
                self.state = 98
                self.match(FormulaParser.OPEN)
                self.state = 99
                localctx._ctl_init = self.ctl_init()
                self.state = 100
                localctx._UNTIL = self.match(FormulaParser.UNTIL)
                self.state = 101
                localctx._ctl_end = self.ctl_end()
                self.state = 102
                self.match(FormulaParser.CLOSE)
                localctx.result = Formula("A", localctx._ctl_init.result, localctx._ctl_end.result, (None if localctx._UNTIL is None else localctx._UNTIL.text))
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 105
                localctx._TEMPORAL = self.match(FormulaParser.TEMPORAL)
                self.state = 106
                self.match(FormulaParser.OPEN)
                self.state = 107
                localctx._first = self.first()
                self.state = 108
                localctx._op_bool = self.op_bool()
                self.state = 109
                localctx._second = self.second()
                self.state = 110
                self.match(FormulaParser.CLOSE)
                localctx.result = Formula((None if localctx._TEMPORAL is None else localctx._TEMPORAL.text), localctx._first.result, localctx._second.result, localctx._op_bool.result)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 113
                localctx._TEMPORAL = self.match(FormulaParser.TEMPORAL)
                self.state = 114
                self.match(FormulaParser.OPEN)
                self.state = 115
                localctx._first = self.first()
                self.state = 116
                self.match(FormulaParser.CLOSE)
                localctx.result = Formula((None if localctx._TEMPORAL is None else localctx._TEMPORAL.text), localctx._first.result)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 119
                localctx._TEMPORAL = self.match(FormulaParser.TEMPORAL)
                self.state = 120
                self.match(FormulaParser.OPEN)
                self.state = 121
                localctx._first = self.first()
                self.state = 122
                localctx._op_bool = self.op_bool()
                self.state = 123
                localctx._ctl_end = self.ctl_end()
                self.state = 124
                self.match(FormulaParser.CLOSE)
                localctx.result = Formula((None if localctx._TEMPORAL is None else localctx._TEMPORAL.text), localctx._first.result, localctx._ctl_end.result, localctx._op_bool.result)
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 127
                localctx._TEMPORAL = self.match(FormulaParser.TEMPORAL)
                self.state = 128
                self.match(FormulaParser.OPEN)
                self.state = 129
                localctx._ctl_init = self.ctl_init()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0):
                    self.state = 130
                    localctx._op_bool = self.op_bool()
                    self.state = 131
                    localctx._ctl_end = self.ctl_end()
                    localctx.op = True


                self.state = 136
                self.match(FormulaParser.CLOSE)

                if localctx.op:
                    localctx.result = Formula((None if localctx._TEMPORAL is None else localctx._TEMPORAL.text), localctx._ctl_init.result, localctx._ctl_end.result, localctx._op_bool.result)
                else:
                    localctx.result = Formula((None if localctx._TEMPORAL is None else localctx._TEMPORAL.text), localctx._ctl_init.result)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FirstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self._ATOMIC = None # Token

        def ATOMIC(self):
            return self.getToken(FormulaParser.ATOMIC, 0)

        def getRuleIndex(self):
            return FormulaParser.RULE_first

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFirst" ):
                listener.enterFirst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFirst" ):
                listener.exitFirst(self)




    def first(self):

        localctx = FormulaParser.FirstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_first)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            localctx._ATOMIC = self.match(FormulaParser.ATOMIC)
            localctx.result = (None if localctx._ATOMIC is None else localctx._ATOMIC.text)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SecondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self._ATOMIC = None # Token

        def ATOMIC(self):
            return self.getToken(FormulaParser.ATOMIC, 0)

        def getRuleIndex(self):
            return FormulaParser.RULE_second

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSecond" ):
                listener.enterSecond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSecond" ):
                listener.exitSecond(self)




    def second(self):

        localctx = FormulaParser.SecondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_second)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            localctx._ATOMIC = self.match(FormulaParser.ATOMIC)
            localctx.result = (None if localctx._ATOMIC is None else localctx._ATOMIC.text)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ctl_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self._formula = None # FormulaContext

        def formula(self):
            return self.getTypedRuleContext(FormulaParser.FormulaContext,0)


        def getRuleIndex(self):
            return FormulaParser.RULE_ctl_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCtl_init" ):
                listener.enterCtl_init(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCtl_init" ):
                listener.exitCtl_init(self)




    def ctl_init(self):

        localctx = FormulaParser.Ctl_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ctl_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            localctx._formula = self.formula()
            localctx.result = localctx._formula.result
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ctl_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None
            self._formula = None # FormulaContext

        def formula(self):
            return self.getTypedRuleContext(FormulaParser.FormulaContext,0)


        def getRuleIndex(self):
            return FormulaParser.RULE_ctl_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCtl_end" ):
                listener.enterCtl_end(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCtl_end" ):
                listener.exitCtl_end(self)




    def ctl_end(self):

        localctx = FormulaParser.Ctl_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ctl_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            localctx._formula = self.formula()
            localctx.result = localctx._formula.result
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NegContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None


        def getRuleIndex(self):
            return FormulaParser.RULE_neg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNeg" ):
                listener.enterNeg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNeg" ):
                listener.exitNeg(self)




    def neg(self):

        localctx = FormulaParser.NegContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_neg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(FormulaParser.T__0)
            localctx.result = True
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_boolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.result = None


        def getRuleIndex(self):
            return FormulaParser.RULE_op_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_bool" ):
                listener.enterOp_bool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_bool" ):
                listener.exitOp_bool(self)




    def op_bool(self):

        localctx = FormulaParser.Op_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_op_bool)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(FormulaParser.T__1)
                localctx.result = "&&"
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(FormulaParser.T__2)
                localctx.result = "||"
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.match(FormulaParser.T__3)
                localctx.result = "=>"
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 4)
                self.state = 162
                self.match(FormulaParser.T__4)
                localctx.result = "<=>"
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





