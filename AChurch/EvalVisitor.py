from __future__ import annotations
from exprsVisitor import exprsVisitor
from exprsParser import exprsParser
from dataclasses import dataclass
import string

DEBUG = 0

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
        if DEBUG: print("HERE")
        a = self.visitChildren(ctx)
        if DEBUG: print("HERE2")
        if DEBUG: print(a)
        return a

    def visitParentesis(self, ctx):
        [_,terme,_] = list(ctx.getChildren())
        return self.visit(terme)

    def visitAbstraccio(self, ctx):
        count = ctx.getChildCount()
        if DEBUG: print("Visiting childs on abstraction:")
        
        a = NodeAbs(NodeVar(str(ctx.getChild(count-3))), self.visit(ctx.getChild(count-1)))
        if DEBUG: print(str(ctx.getChild(count-3)))
        
        start = count - 4
        for i in range(start, 0, -1):
            if DEBUG: print("Current i: "+ str(i) + " - " + str(ctx.getChild(i)))
            a = NodeAbs(NodeVar(str(ctx.getChild(i))), a)    
            
        if DEBUG: print("Current tree abs: " + show(a))
        return a

    def visitAplicacio(self, ctx):
        [terme1,terme2] = list(ctx.getChildren())
        r = NodeAp(self.visit(terme1), self.visit(terme2))
        if DEBUG: print("Current tree apl: " + show(r))
        return r

    def visitLletra(self, ctx):
        [lletra] = list(ctx.getChildren())
        
        if DEBUG: print("Current tree var: " + show(NodeVar(lletra.getText())))
        return NodeVar(lletra.getText())
    
    
def show(a: Arbre) -> str:
    match a:
        case NodeAp(e,d):
            return '(' + str(show(e)) + str(show(d)) + ')'
        case NodeAbs(e,d):
            return '(λ' + str(show(e)) + '.' + str(show(d)) + ')'
        case NodeVar(var):
            return str(var)
        
def beta_reduction(a: Arbre) -> Arbre:
    if isinstance(a, NodeAp) and isinstance(a.esq, NodeAbs):
        r = beta_substitution(a.esq.dre, a.esq.esq.val, a.dre)
        
        if (contains_abs(r)): r = beta_reduction(r)
        return r
    
    elif isinstance(a, NodeAp):
        return NodeAp(beta_reduction(a.esq), beta_reduction(a.dre))
    
    else:
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
    
def contains_abs(a: Arbre) -> bool:
    if isinstance(a, NodeVar): return False
    if isinstance(a, NodeAbs): return True
    return contains_abs(a.esq) or contains_abs(a.dre)

def alpha_convert(a: Arbre):
    b = alpha(a)
    if DEBUG: print("NEW ALPHA TREE: " + show(b))
    return a

def alpha(a):
    if isinstance(a, NodeAp) and isinstance(a.esq, NodeAbs):
        may_conflict_vars = get_vars_tree(a.dre)
        already_inuse_vars = get_vars_tree(a.esq)
        available_vars = [x for x in list(string.ascii_lowercase) if x not in already_inuse_vars] # all standard dict available
        # create dictionary that converts a -> b 
        alpha_dict = build_dictionary(may_conflict_vars, available_vars)
        # substitute a esq amb vars diff de les de la dreta
        t_esq = alpha_substitution(a.esq, alpha_dict)
        # apply alpha for both left and right to get it recursively
        n_esq = alpha(t_esq)
        n_dre = alpha(a.dre)
        return NodeAp(n_esq, n_dre)
    
    elif isinstance(a, NodeAp):
        return NodeAp(alpha(a.esq), alpha(a.dre))
    
    elif isinstance(a, NodeAbs):
        return NodeAbs(alpha(a.esq), alpha(a.dre))
    
    elif isinstance(a, NodeVar):
        return a
    
    # No hauria d'arribar 
    print("ERRRROR ON ALPHA!")
    return alpha(a)
    
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

def alpha_substitution(a: Arbre, conversor):
    if isinstance(a, NodeAp): return NodeAp(alpha_substitution(a.esq, conversor), alpha_substitution(a.dre, conversor))
    if isinstance(a, NodeAbs): return NodeAbs(alpha_substitution(a.esq, conversor), alpha_substitution(a.dre, conversor))
    # if NodeVar we check its variable and if in conversor, change it
    if a.val in conversor:
        a.val = conversor[a.val]
    return a

# def alpha_convert_depth(a: Arbre, variable: str, new_variable: str):
#     if isinstance(a, NodeVar):
#         if a.val == variable: 
#             return NodeVar(new_variable)
#         return a
        
#     elif isinstance(a, NodeAp):
#         esq_converted = alpha_convert_depth(a.esq, variable, new_variable)
#         dre_converted = alpha_convert_depth(a.dre, variable, new_variable)
#         return NodeAp(esq_converted, dre_converted)
    
#     elif isinstance(a, NodeAbs):
#         if a.esq.val == variable: 
#             new_var = get_new_variable()
#             body_converted = alpha_convert_depth(a.dre, a.esq.val, new_var)
#             return NodeAbs(NodeVar(new_var), body_converted)
        
#         else:
#             body_converted = alpha_convert_depth(a.dre, variable, new_variable)
#             return NodeAbs(a.esq, body_converted)
    
#     return a