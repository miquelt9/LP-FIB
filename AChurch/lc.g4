// Gramàtica per expressions senzilles
grammar lc;
root : terme             // l'etiqueta ja és root
     | assignar
     ;

assignar: INFIX EQUALS terme     # assignarInfix 
     | NOM_MACRO EQUALS terme     # assignarMacro
     ;

terme : LLETRA                          # lletra
     | INFIX                            # infix
     | NOM_MACRO                        # macro
     | '(' terme ')'                    # parentesis
     | terme terme                      # aplicacio
     | ('λ' || '\\') LLETRA+ '.' terme        # abstraccio
     ;

LLETRA : [a-z];
NOM_MACRO: [A-Z][a-zA-Z0-9]*;
INFIX: [!"·$%&*.,:;<>?¿|@#/~¬€_+\-^]; //had problems using negated version of alphabet so...

EQUALS : ('≡' | '=');
WS  : [ \t\n\r]+ -> skip ;