# Generated from E:/Andre/Универ/Информатика/Checker/Random-word-generator/ANTLRtest\Calculator.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculatorParser import CalculatorParser
else:
    from CalculatorParser import CalculatorParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorParser.

class CalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorParser#Integer.
    def visitInteger(self, ctx:CalculatorParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Abs.
    def visitAbs(self, ctx:CalculatorParser.AbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Brackets.
    def visitBrackets(self, ctx:CalculatorParser.BracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#MulDiv.
    def visitMulDiv(self, ctx:CalculatorParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#AddSub.
    def visitAddSub(self, ctx:CalculatorParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Exp.
    def visitExp(self, ctx:CalculatorParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorParser#Minus.
    def visitMinus(self, ctx:CalculatorParser.MinusContext):
        return self.visitChildren(ctx)



del CalculatorParser