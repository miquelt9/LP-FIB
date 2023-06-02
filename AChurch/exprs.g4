// Gramàtica per expressions senzilles
grammar exprs;
root : terme             // l'etiqueta ja és root
     | assignar
     ;

assignar: NOM_MACRO ('≡' || '=') terme     # assignarMacro
     | INFIX ('≡' || '=') terme     # assignarInfix
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
INFIX: [!#$%&*+,-/:;<>?@^|~]; //all non-alphanumeric chars not used to avoid conflicts

WS  : [ \t\n\r]+ -> skip ;