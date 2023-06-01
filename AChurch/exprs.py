from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from EvalVisitor import *

input_stream = InputStream(input('? '))
lexer = exprsLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
tree = parser.root()

if (parser.getNumberOfSyntaxErrors() == 0):
    visitor = EvalVisitor()
    a = visitor.visit(tree)
    print("\nPRINTING TREE:")
    print(show(a))
    
    print("\nALFACONVERTING:")
    print(show(a) + " --> ", end="")
    a = alpha_convert(a)
    print(show(a))
    
    print("\nBETAREDUCING:")
    print(show(a) + " --> ", end="")
    a = beta_reduction(a)
    print(show(a))
    
print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
print(tree.toStringTree(recog=parser))