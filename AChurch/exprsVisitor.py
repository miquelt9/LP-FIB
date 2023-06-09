# Generated from exprs.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .exprsParser import exprsParser
else:
    from exprsParser import exprsParser

# This class defines a complete generic visitor for a parse tree produced
# by exprsParser.


class exprsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprsParser#root.
    def visitRoot(self, ctx: exprsParser.RootContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by exprsParser#assignarInfix.
    def visitAssignarInfix(self, ctx: exprsParser.AssignarInfixContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by exprsParser#assignarMacro.
    def visitAssignarMacro(self, ctx: exprsParser.AssignarMacroContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by exprsParser#parentesis.
    def visitParentesis(self, ctx: exprsParser.ParentesisContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by exprsParser#macro.
    def visitMacro(self, ctx: exprsParser.MacroContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by exprsParser#lletra.
    def visitLletra(self, ctx: exprsParser.LletraContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by exprsParser#abstraccio.
    def visitAbstraccio(self, ctx: exprsParser.AbstraccioContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by exprsParser#infix.
    def visitInfix(self, ctx: exprsParser.InfixContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by exprsParser#aplicacio.
    def visitAplicacio(self, ctx: exprsParser.AplicacioContext):
        return self.visitChildren(ctx)


del exprsParser
