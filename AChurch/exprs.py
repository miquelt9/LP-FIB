from __future__ import annotations
from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor
from exprsParser import exprsParser
from dataclasses import dataclass
import string

import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = open('token.txt').read().strip()
LOG_ACTIVATED = False

# Enable logging
if (LOG_ACTIVATED):
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    logger = logging.getLogger(__name__)


commands = "/start -> Inicia el bot\n/macros -> Mostra les macros definides\n/author -> Mostra l'autor\n/help -> Mostra les comandes disponibles"

# Define a few command handlers. These usually take the two arguments update and

# context.

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Missatge d'inici."""
    user = update.effective_user
    await update.message.reply_text("Hola " + str(user.first_name) + "!")
    await update.message.reply_text("Disposes de les següents comandes:\n"+commands)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia el missatge de help (i.e. les comandes disponibles)."""
    await update.message.reply_text("Pots utilitzar les següents comandes:\n"+commands)

async def author(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mostra l'autor del bot."""
    await update.message.reply_markdown("λ-Bot\nMiquel Torner Viñals, 2023\nGithub: [@miquelt9](https://github.com/miquelt9)", disable_web_page_preview=True)
    
async def macros(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mostra els macros."""
    await update.message.reply_text("Els macros definits són:")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    user_input = update.message.text
    if (user_input != ""):
        input_stream = InputStream(user_input)
        lexer = exprsLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = exprsParser(token_stream)
        tree = parser.root()

        if (parser.getNumberOfSyntaxErrors() == 0):
            visitor = EvalVisitor()
            visitor.visit(tree)
            
        else:
            print("")
            print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
            print(tree.toStringTree(recog=parser))
            
    else:
        await update.message.reply_text("Disculpa, però no he entès el teu missatge.")

def main() -> None:
    """Start the bot."""
    
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Donat una instruccio contestem a Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("author", author))
    application.add_handler(CommandHandler("macros", macros))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


    # Run the bot until the user presses Ctrl-C
    application.run_polling()



######################################################################################

DEBUG = 0
diccionari_macros = {}

@dataclass
class NodeAp:
    esq: Arbre
    dre: Arbre
    
@dataclass
class NodeAbs:
    esq: NodeVar
    dre: Arbre

@dataclass
class NodeVar:
    val: str
    
Arbre = NodeAp | NodeAbs | NodeVar
     
class EvalVisitor(exprsVisitor):

    def visitRoot(self, ctx):
        if DEBUG: print("Starting the visit")
        a = self.visitChildren(ctx)
        if DEBUG: print("Tree in Raw Format")
        if DEBUG: print(a)
        
        # Diferenciarem per casos, doncs si són macros no podem fer el mateix tractament
        if ctx.terme() and a != NodeVar(None):
            if DEBUG: print("Matched 'TERME'")
            
            print("Arbre:")
            print(show(a))
            
            print("α-conversió:")
            print(show(a) + " --> ", end="")
            a = alpha_convert(a)
            print(show(a))
            
            a = beta_reduction(a)

            print("Resultat:")
            print(show(a))
            
            return a
            
        elif ctx.assignar():
            if DEBUG: print("Matched 'ASSIGNAR'")
                

    def visitParentesis(self, ctx):
        [_,terme,_] = list(ctx.getChildren())
        return self.visit(terme)

    def visitAbstraccio(self, ctx):
        count = ctx.getChildCount()
        if DEBUG: print("--> Visiting childs on abstraction:")
        
        a = NodeAbs(NodeVar(str(ctx.getChild(count-3))), self.visit(ctx.getChild(count-1)))
        if DEBUG: print(str(ctx.getChild(count-3)))
        
        start = count - 4
        for i in range(start, 0, -1):
            if DEBUG: print("Current i: "+ str(i) + " - " + str(ctx.getChild(i)))
            a = NodeAbs(NodeVar(str(ctx.getChild(i))), a)    
            
        if DEBUG: print("Current tree abs: " + show(a))
        return a

    def visitAplicacio(self, ctx):
        if DEBUG: print("--> Visiting aplicacio")
        [terme1,terme2] = list(ctx.getChildren())
        p_infix = str(terme2.getChild(0))
        if (len(p_infix) == 1 and not p_infix.isalpha() and p_infix != '(' and p_infix != "\\" and p_infix != 'λ'):
            r = NodeAp(self.visit (terme2), self.visit(terme1))
        else: r = NodeAp(self.visit(terme1), self.visit(terme2))
        if DEBUG: print("Current tree apl: " + show(r))
        return r

    def visitLletra(self, ctx):
        if DEBUG: print("-> Visiting lletra")
        [lletra] = list(ctx.getChildren())
        if DEBUG: print("Current tree var: " + show(NodeVar(lletra.getText())))
        return NodeVar(lletra.getText())
    
    def visitMacro(self, ctx):
        [macro] = list(ctx.getChildren())
        if str(macro) in diccionari_macros:
            return diccionari_macros[str(macro)]
        
        print("⚠  The macro you used (" + str(macro) + ") was not declared\nShowing current dictionary:")
        print_available_macros()
        return NodeVar(None)
    
    def visitAssignarMacro(self, ctx):
        if DEBUG: print("-> Visiting assignar macro")
        [nom_macro,_,terme] = list(ctx.getChildren())
        diccionari_macros[str(nom_macro)] = self.visit(terme)
        
        print_available_macros()
            
    def visitAssignarInfix(self, ctx:exprsParser.AssignarInfixContext):
        if DEBUG: print("-> Visiting assignar infix")
        [nom_infix,_,terme] = list(ctx.getChildren())
        diccionari_macros[str(nom_infix)] = self.visit(terme)
        
        print_available_macros()
            
    def visitInfix(self, ctx):
        if DEBUG: print("-> Visiting infix")
        [infix] = list(ctx.getChildren())
        
        if not str(infix) in diccionari_macros:
            print("⚠  The infix you used (" + str(infix) + ") was not declared\nShowing current dictionary:")
            print_available_macros()     
            return NodeVar(None)
        
        return diccionari_macros[str(infix)]
   
def print_available_macros():
    for nom_macro, macro in diccionari_macros.items():
                print(str(nom_macro) + " ≡ " + show(macro))   
    
def show(a: Arbre) -> str:
    match a:
        case NodeAp(e,d):
            return '(' + str(show(e)) + str(show(d)) + ')'
        case NodeAbs(e,d):
            return '(λ' + str(show(e)) + '.' + str(show(d)) + ')'
        case NodeVar(var):
            return str(var)
        
def beta_reduction(a: Arbre):
    while(tree_is_beta_reducible(a)): 
        t = a; a = beta_reduction_depth(a)
        
        print("β-reducció:")
        print(show(t) + " → ", end="")
        if a == t:
            print(show(a)); print("...")
            print("⚠  Error during beta reduction, limit reached due to an infinite loop  ⚠")
            return NodeVar("Nothing")
        # if isinstance(t, NodeVar) and a.val == "Nothing": print("...")
        else: print(show(a))
        

    return a

def beta_reduction_depth(a: Arbre) -> Arbre:
    if isinstance(a, NodeAp) and isinstance(a.esq, NodeAbs):
        if DEBUG: print("beta-detected" + show(a))
        return beta_substitution(a.esq.dre, a.esq.esq.val, a.dre)
    
    elif isinstance(a, NodeAp):
        if DEBUG: print("beta-nodeap")
        return NodeAp(beta_reduction_depth(a.esq), beta_reduction_depth(a.dre))
    
    elif isinstance(a, NodeAbs):
        if DEBUG: print("beta-nodeabs")
        return NodeAbs(beta_reduction_depth(a.esq), beta_reduction_depth(a.dre))
    
    else:
        if DEBUG: print("beta-ret-same")
        return a
        
def beta_substitution(a: Arbre, var: str, subs: Arbre) -> Arbre:
    if isinstance(a, NodeVar):
        if a.val == var:
            return subs
        else:
            return a
        
    elif isinstance(a, NodeAp):
        return NodeAp(beta_substitution(a.esq, var, subs), beta_substitution(a.dre, var, subs))
    
    elif isinstance(a, NodeAbs):
        return NodeAbs(beta_substitution(a.esq, var, subs), beta_substitution(a.dre, var, subs))
    
    else:
        return a
    
def tree_is_beta_reducible(a: Arbre) -> bool:
    if isinstance(a, NodeVar): return False
    if isinstance(a, NodeAp) and isinstance(a.esq, NodeAbs): return True
    return tree_is_beta_reducible(a.esq) or tree_is_beta_reducible(a.dre)

def alpha_convert(a: Arbre):
    b = alpha(a, generate_vars())

    if DEBUG: print("NEW ALPHA TREE: " + show(b))
    return b

def alpha(a: Arbre, available_vars):
    if isinstance(a, NodeAp) and isinstance(a.esq, NodeAbs):
        may_conflict_vars = get_vars_tree(a.dre)
        already_inuse_vars = get_vars_tree(a.esq)
         # all standard dict available
        available_vars = [x for x in available_vars if x not in already_inuse_vars]
        # create dictionary that converts a -> b 
        alpha_dict = build_dictionary(may_conflict_vars, available_vars)
        # substitute a esq amb vars diff de les de la dreta
        t_esq = alpha_substitution(a.esq, alpha_dict)
        # apply alpha for both left and right to get it recursively
        n_esq = alpha(t_esq, available_vars)
        n_dre = alpha(a.dre, available_vars)
        return NodeAp(n_esq, n_dre)
    
    elif isinstance(a, NodeAp):
        return NodeAp(alpha(a.esq, available_vars), alpha(a.dre, available_vars))
    
    elif isinstance(a, NodeAbs):
        return NodeAbs(alpha(a.esq, available_vars), alpha(a.dre, available_vars))
    
    elif isinstance(a, NodeVar):
        return a
    
    # No hauria d'arribar 
    print("ERRRROR ON ALPHA!")
    return alpha(a, available_vars)
    
def get_vars_tree(a: Arbre):
    vars = []
    if isinstance(a, NodeVar): vars.append(a.val)
    else:
        vars.extend(get_vars_tree(a.esq))
        vars.extend(get_vars_tree(a.dre))
    return vars

def build_dictionary(conflict_list, all_letters):
    alpha_d = {}

    for letter in conflict_list:
        available_letters = [l for l in all_letters if l not in alpha_d.values()]
        alpha_d[letter] = available_letters[0]

    return alpha_d

def generate_vars():
    l = list(string.ascii_lowercase)
    for i in l:
        l.append(str(i+"'"))
        if len(l) > 100: break
    return l

def alpha_substitution(a: Arbre, conversor):
    if isinstance(a, NodeAp): return NodeAp(alpha_substitution(a.esq, conversor), alpha_substitution(a.dre, conversor))
    if isinstance(a, NodeAbs): return NodeAbs(alpha_substitution(a.esq, conversor), alpha_substitution(a.dre, conversor))
    # if NodeVar we check its variable and if in conversor, change it
    if a.val in conversor:
        a.val = conversor[a.val]
    return a






if __name__ == "__main__":
    main()