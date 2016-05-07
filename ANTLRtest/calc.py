import antlr4
from Tools.scripts.treesync import raw_input

from CalculatorLexer import CalculatorLexer
from CalculatorParser import CalculatorParser

while True:
    expr = raw_input('>>> ')
    if expr == '':
        break

    cStream = antlr4.InputStream(expr)
    lexer = CalculatorLexer(cStream)
    tStream = antlr4.CommonTokenStream(lexer)
    parser = CalculatorParser(tStream)
    tree = parser.expr()
    print(tree)
