from __future__ import annotations
from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor
from exprsParser import exprsParser
from dataclasses import dataclass
import string
import copy
import pydot
import random

import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

TOKEN = open('token.txt').read().strip()
LOG_ACTIVATED = False
VERBOSE = True
show_all_pictures = {}

# Enable logging
if (LOG_ACTIVATED):
    logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
    logger = logging.getLogger(__name__)


commands = "/start -> Inicia el bot\n/macros -> Mostra les macros definides\n/clear -> Neteja les macros\n/verbose [true|false] -> Mostra els passos intermigs a les β-reduccions \n/author -> Mostra l'autor\n/help -> Mostra les comandes disponibles"

# Define a few command handlers. These usually take the two arguments update and context.

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Missatge d'inici."""
    user = update.effective_user
    await update.message.reply_text("Hola " + str(user.first_name) + "!")
    await update.message.reply_text("Utilitza la comanda /help per veure totes les comandes.")
    initialize_globals(user.id, True)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envia el missatge de help (i.e. les comandes disponibles)."""
    await update.message.reply_text("Pots utilitzar les següents comandes:\n"+commands)

async def author(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mostra l'autor del bot."""
    await update.message.reply_markdown("λ-Bot\nMiquel Torner Viñals, 2023\nGithub: [@miquelt9](https://github.com/miquelt9)", disable_web_page_preview=True)
    
async def macros(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Mostra els macros."""
    initialize_globals(update.effective_user.id)
    t = ""
    for nom_macro, macro in diccionari_macros[update.effective_user.id].items():
        t += (str(nom_macro) + " ≡ " + show(macro) + '\n')
    if t != "":
        await update.message.reply_text("Els macros definits són:")
        await update.message.reply_text(t)
    else:
        await update.message.reply_text("Actualment no hi ha macros definides.")

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Neteja els macros."""
    initialize_globals(update.effective_user.id)
    diccionari_macros[update.effective_user.id].clear()
    await update.message.reply_text("El diccionari de macros s'ha netejat.")
    
async def verbose(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Activa o desactiva el mode verbose."""
    user_input = update.message.text
    if DEBUG: print(user_input)
    splitted_input = user_input.split()
    
    if (len(splitted_input) == 2):
        global show_all_pictures
        if splitted_input[1] == "True" or splitted_input[1] == "true":
            show_all_pictures[update.effective_user.id] = True
            await update.message.reply_text("Les imatges de les β-reduccions es mostraran.")
            
        elif splitted_input[1] == "False" or splitted_input[1] == "false":
            show_all_pictures[update.effective_user.id] = False
            await update.message.reply_text("No es mostraran les  β-reduccions.")
    
        else:
            await update.message.reply_text("No té entès, siusplau envia /verbose [true|false], per exemple:\n/verbose true")
    else:
            await update.message.reply_text("Sisplau inclou només un argument, per exemple:\n/verbose false")

async def treat_lambda_tree(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    user_input = update.message.text
    
    initialize_globals(user.id)
        
    if (user_input != ""):
        input_stream = InputStream(user_input)
        lexer = exprsLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = exprsParser(token_stream)
        tree = parser.root()

        if (parser.getNumberOfSyntaxErrors() == 0):
            visitor = EvalVisitor(user.id)
            a = visitor.visit(tree)  
            
            if errors_macro != []:
                    await update.message.reply_text("Errors amb les macros i infix següents:")
                    t = ""
                    for [k, name] in errors_macro:
                        if (k == "I"): t += ("L'infix '" + name + "' no està definit.\n")
                        else: t += ("La macro '" + name + "' no està definida.\n")
                    await update.message.reply_text(t)
                    errors_macro.clear()
                        
            elif isinstance(a, Arbre):
                if VERBOSE: print("Proceding with tree:"); print(show(a))
                await update.message.reply_text(str(show(a)))
                
                #We send the initial image graph
                graph = build_graph(a)
                graph.write_png('tree-' + str(user.id) + '.png')
                try:
                    await update.message.reply_photo(photo=open('tree-' + str(user.id) + '.png', 'rb'), caption="Arbre inicial")
                except:
                    await update.message.reply_text("La imatge no té les mides requerides per Telegram, enviant com a document...")
                    await update.message.reply_document(open('tree-' + str(user.id) + '.png', 'rb'))
                
                if VERBOSE: print("α-conversió:")
                if VERBOSE: print(show(a) + " --> ", end="")
                
                old_a = copy.deepcopy(a)
                alpha_convert(a)
                
                if VERBOSE: print("BF-ALFA: " + show(old_a))
                if VERBOSE: print("NEW: " + show(a))
                if str(old_a) != str(a):
                    await update.message.reply_text(show(old_a) + " → α → " + show(a))
                    
                if VERBOSE: print(show(a))
                
                trace = [a]
                trace.extend(beta_reduction(a))

                trace_show = []
                for x in trace:
                    trace_show.append(show(x))
                
                if len(trace) == 0:
                    # await update.message.reply_text(str(show(a)) + " is not β-reductible")
                    if VERBOSE: print("Trying to β-reduce smth which is not β-reducible")
                    
                elif trace[-1] == None:
                    if VERBOSE: print(trace_show)
                    
                    if show_all_pictures[update.effective_user.id]:
                        await update.message.reply_text("El mode verbose no es mostra donat que s'ha arribat al límit de recursivitat.") 
                    
                    for i in range(len(trace) - 2):
                        mov = trace_show[i] + " → β → " + trace_show[i+1]
                        await update.message.reply_text(mov)     
   
                    a = trace[-1]
                    await update.message.reply_text(trace_show[-2] + " → β → " + trace_show[-2])
                    await update.message.reply_text("Nothing") 
                    
                    #We prepare the nothing graph
                    graph = build_graph(NodeVar("Nothing"))
                    
                else:
                    if VERBOSE: print(trace_show)
                    for i in range(len(trace) - 1):
                        mov = trace_show[i] + " → β → " + trace_show[i+1]
                        await update.message.reply_text(mov)
                        # for verbose mode:
                        if show_all_pictures[update.effective_user.id] and i != len(trace) - 2:
                            graph = build_graph(trace[i+1]) 
                            graph.write_png('tree-' + str(user.id) + '.png')
                            try:
                                await update.message.reply_photo(photo=open('tree-' + str(user.id) + '.png', 'rb'))
                            except:
                                await update.message.reply_text("La imatge no té les mides requerides per Telegram, enviant com a document...")
                                await update.message.reply_document(open('tree-' + str(user.id) + '.png', 'rb'))
                              
                    a = trace[-1]
                    await update.message.reply_text(show(a))  
                    
                    #We prepare the resulting graph
                    graph = build_graph(a)

                #We send the resulting image graph
                graph.write_png('tree-' + str(user.id) + '.png')                    
                try:
                    await update.message.reply_photo(photo=open('tree-' + str(user.id) + '.png', 'rb'), caption="Arbre resultant")
                except:
                    await update.message.reply_text("La imatge no té les mides requerides per Telegram, enviant com a document...")
                    await update.message.reply_document(open('tree-' + str(user.id) + '.png', 'rb'))
                    
                if VERBOSE: print("Resultat:")
                if VERBOSE: print(show(a))
                
            else:
                if VERBOSE: print("Macro defined!")
                await update.message.reply_text(a + "≡" + str(show(diccionari_macros[update.effective_user.id][a])) + " s'ha definit amb èxit.")
            
        else:
            await update.message.reply_text("Comprova el teu arbre i torna'l a enviar")
            print("")
            print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
            print(tree.toStringTree(recog=parser))
            
    else:
        await update.message.reply_text("Disculpa, però no he entès el teu missatge.")

    
def initialize_globals(uid, force=False):
    global show_all_pictures
    if force:
        show_all_pictures[uid] = False
        diccionari_macros[uid] = {}
    else:
        if not (uid in show_all_pictures):
            show_all_pictures[uid] = False
            diccionari_macros[uid] = {}

def main() -> None:
    """Start the bot."""
    
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Donat una instruccio contestem a Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("author", author))
    application.add_handler(CommandHandler("macros", macros))
    application.add_handler(CommandHandler("clear", clear))
    application.add_handler(CommandHandler("verbose", verbose))

    # on non command i.e a possible tree
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, treat_lambda_tree))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()



######################################################################################

DEBUG = 0
diccionari_macros = {}
errors_macro = []

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

    def __init__(self, uid):
        self.uid = uid

    def visitRoot(self, ctx):
        if DEBUG: print("Starting the visit")
        a = self.visitChildren(ctx)
        if DEBUG: print("Tree in Raw Format")
        if DEBUG: print(a)
        
        # Diferenciarem per casos, doncs si són macros no podem fer el mateix tractament
        if ctx.terme() and a != NodeVar(None):
            if DEBUG: print("Matched 'TERME'")
            ## We return the tree so the bot does the handling
            return a
            
        elif ctx.assignar():
            if DEBUG: print("Matched 'ASSIGNAR'")
            return a                

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
        if str(macro) in diccionari_macros[self.uid]:
            return diccionari_macros[self.uid][str(macro)]
        
        print("⚠  The macro you used (" + str(macro) + ") was not declared\nShowing current dictionary:")
        print_available_macros(self.uid)
        global errors_macro 
        errors_macro.append(["M", str(macro)])
        return NodeVar(None)
    
    def visitAssignarMacro(self, ctx):
        if DEBUG: print("-> Visiting assignar macro")
        [nom_macro,_,terme] = list(ctx.getChildren())
        diccionari_macros[self.uid][str(nom_macro)] = self.visit(terme)
        
        print_available_macros(self.uid)
        return str(nom_macro)
            
    def visitAssignarInfix(self, ctx:exprsParser.AssignarInfixContext):
        if DEBUG: print("-> Visiting assignar infix")
        [nom_infix,_,terme] = list(ctx.getChildren())
        diccionari_macros[self.uid][str(nom_infix)] = self.visit(terme)
        
        print_available_macros(self.uid)
        return str(nom_infix)
            
    def visitInfix(self, ctx):
        if DEBUG: print("-> Visiting infix")
        [infix] = list(ctx.getChildren())
        
        if not str(infix) in diccionari_macros[self.uid]:
            print("⚠  The infix you used (" + str(infix) + ") was not declared\nShowing current dictionary:")
            print_available_macros(self.uid)     
            global errors_macro 
            errors_macro.append(["I", str(infix)])
            return NodeVar(None)
        
        return diccionari_macros[self.uid][str(infix)]
   
def print_available_macros(uid):
    for nom_macro, macro in diccionari_macros[uid].items():
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
    traceback = []
    set_trace = set() #memory is cheaper than time so we 
    while(tree_is_beta_reducible(a)): 
        a = beta_reduction_depth(a)
        
        if VERBOSE: print("β-reducció:")
        if (len(traceback) > 0 and VERBOSE): print(show(traceback[-1]) + " → ", end="")
        if str(a) in set_trace:
            if VERBOSE: print(show(a)); print("...")
            if VERBOSE: print("⚠  Error during beta reduction, limit reached  ⚠")
            # return NodeVar("Nothing")
            traceback.append(None)
            return traceback
        # if isinstance(t, NodeVar) and a.val == "Nothing": print("...")
        else: 
            if VERBOSE: print(show(a))
            traceback.append(a)
            set_trace.add(str(a))
            
    return traceback

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

def build_graph(a: Arbre):
    graph = pydot.Dot(graph_type='digraph')
    generate_graph(a, graph, '', [])
    return graph

def generate_graph(tree: Arbre, graph: pydot.Dot, parent_node_name: str, linked_vars: list):
    
    if isinstance(tree, NodeVar):
        node_name = tree.val
    elif isinstance(tree, NodeAbs):
        node_name = "λ" + tree.esq.val
    else:
        node_name = '@'
    
    # Create a unique name for the current node (random is used bc otherwise siblings with same value have same id)
    current_node_name = str(id(tree)*random.randint(1,id(tree))) 
    if DEBUG: print("ID: " + current_node_name)
    
    node = pydot.Node(current_node_name, label=str(node_name) , shape="plaintext")
    graph.add_node(node)
    
    if isinstance(tree, NodeAp):
        generate_graph(tree.esq, graph, current_node_name, linked_vars)
        generate_graph(tree.dre, graph, current_node_name, linked_vars)
    elif isinstance(tree, NodeAbs):
        lv = copy.deepcopy(linked_vars)
        lv.append([current_node_name,tree.esq.val])
        generate_graph(tree.dre, graph, current_node_name, lv)

    if parent_node_name != '':
        for [k, val] in linked_vars:
            if node_name == val:
                graph.add_edge(pydot.Edge(current_node_name, k, style='dashed', arrowsize=0.7))
                
        graph.add_edge(pydot.Edge(parent_node_name, current_node_name, arrowsize=0.7))



if __name__ == "__main__":
    main()