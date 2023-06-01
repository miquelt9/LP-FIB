// Gramàtica per expressions senzilles
grammar exprs;
root : terme             // l'etiqueta ja és root
     ;

terme : LLETRA                          # lletra
     | '(' terme ')'                    # parentesis
     | terme terme                      # aplicacio
     | ('λ' || '\\') LLETRA+ '.' terme        # abstraccio
     ;

LLETRA : [a-z];

WS  : [ \t\n\r]+ -> skip ;