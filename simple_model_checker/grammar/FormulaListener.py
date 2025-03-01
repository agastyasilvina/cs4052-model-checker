# Generated from Formula.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FormulaParser import FormulaParser
else:
    from FormulaParser import FormulaParser

# This class defines a complete listener for a parse tree produced by FormulaParser.
class FormulaListener(ParseTreeListener):

    # Enter a parse tree produced by FormulaParser#query.
    def enterQuery(self, ctx:FormulaParser.QueryContext):
        pass

    # Exit a parse tree produced by FormulaParser#query.
    def exitQuery(self, ctx:FormulaParser.QueryContext):
        pass


    # Enter a parse tree produced by FormulaParser#formula.
    def enterFormula(self, ctx:FormulaParser.FormulaContext):
        pass

    # Exit a parse tree produced by FormulaParser#formula.
    def exitFormula(self, ctx:FormulaParser.FormulaContext):
        pass


    # Enter a parse tree produced by FormulaParser#first.
    def enterFirst(self, ctx:FormulaParser.FirstContext):
        pass

    # Exit a parse tree produced by FormulaParser#first.
    def exitFirst(self, ctx:FormulaParser.FirstContext):
        pass


    # Enter a parse tree produced by FormulaParser#second.
    def enterSecond(self, ctx:FormulaParser.SecondContext):
        pass

    # Exit a parse tree produced by FormulaParser#second.
    def exitSecond(self, ctx:FormulaParser.SecondContext):
        pass


    # Enter a parse tree produced by FormulaParser#ctl_init.
    def enterCtl_init(self, ctx:FormulaParser.Ctl_initContext):
        pass

    # Exit a parse tree produced by FormulaParser#ctl_init.
    def exitCtl_init(self, ctx:FormulaParser.Ctl_initContext):
        pass


    # Enter a parse tree produced by FormulaParser#ctl_end.
    def enterCtl_end(self, ctx:FormulaParser.Ctl_endContext):
        pass

    # Exit a parse tree produced by FormulaParser#ctl_end.
    def exitCtl_end(self, ctx:FormulaParser.Ctl_endContext):
        pass


    # Enter a parse tree produced by FormulaParser#neg.
    def enterNeg(self, ctx:FormulaParser.NegContext):
        pass

    # Exit a parse tree produced by FormulaParser#neg.
    def exitNeg(self, ctx:FormulaParser.NegContext):
        pass


    # Enter a parse tree produced by FormulaParser#op_bool.
    def enterOp_bool(self, ctx:FormulaParser.Op_boolContext):
        pass

    # Exit a parse tree produced by FormulaParser#op_bool.
    def exitOp_bool(self, ctx:FormulaParser.Op_boolContext):
        pass



del FormulaParser