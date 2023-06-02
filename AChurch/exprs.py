from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from EvalVisitor import *

while True:
    input_stream = InputStream(input('? '))
    lexer = exprsLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = exprsParser(token_stream)
    tree = parser.root()

    if (parser.getNumberOfSyntaxErrors() == 0):
        visitor = EvalVisitor()
        visitor.visit(tree)
        
    else:
        if tree.getChildCount() == 0:
            print("Looks like you didn't write the input :|")
        else:
            print("")
            print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
            print(tree.toStringTree(recog=parser))