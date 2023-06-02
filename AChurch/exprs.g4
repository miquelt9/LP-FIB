// Gramàtica per expressions senzilles
grammar exprs;
root : terme             // l'etiqueta ja és root
     | assignar
     ;

assignar: INFIX ('≡' || '=') terme     # assignarInfix 
     | NOM_MACRO ('≡' || '=') terme     # assignarMacro
     ;

terme : LLETRA                          # lletra
     | NOM_MACRO INFIX NOM_MACRO        # infix
     | NOM_MACRO                        # macro
     | '(' terme ')'                    # parentesis
     | terme terme                      # aplicacio
     | ('λ' || '\\') LLETRA+ '.' terme        # abstraccio
     ;

LLETRA : [a-z];
NOM_MACRO: [A-Z][a-zA-Z0-9]*;
INFIX: [!"·$%&*.,:;<>?¿|@#/~¬€_+\-^]; //had problems using negated version of alphabet so...

WS  : [ \t\n\r]+ -> skip ;