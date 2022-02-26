// Student ID: 1953107

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}


/////////////////////////////////////////////
//////////// Program structure //////////////
/////////////////////////////////////////////
program: CLASS* EOF;

CLASS: 'Class' ID '{' (ATTRIBUTE|METHOD)* '}';

ATTRIBUTE: VAL | VAR;
VAL: 'Val' (ID',')* ID ':' DECLARE ';';
VAR: 'Var' ('$'ID',')* ('$'ID) ':' DECLARE ';';
fragment DECLARE: ;

METHOD: ID '(' ((PARA',')* PARA)? ')' '{' STATEMENT* '}';
fragment PARA: ;
fragment STATEMENT: ;


/////////////////////////////////////////////
//////////// Lexical structure //////////////
/////////////////////////////////////////////

COMMENT: '##' . '##';
ID: [A-Za-z_][A-Za-z_0-9]*;

// Literals
INTLIT: DECLIT | OCTLIT | HEXLIT | BINLIT;
DECLIT: [0-9] | [1-9][0-9_]*[0-9]; //{self.text = self.text.replace('_','')};
OCTLIT: '0' ('0' | [1-7][0-7]*);
HEXLIT: '0'[xX] ('0' | [1-9A-F][0-9A-F]*);
BINLIT: '0'[bB] ('0' | '1'[01]*);

FLOATLIT: INT_PART '.' DEC_PART EXP_PART?;
fragment INT_PART: DECLIT;
fragment DEC_PART: [0-9]*;
fragment EXP_PART: [eE] [-+]? INT_PART;

BOOLLIT: 'True' | 'False';

STRLIT: '"' (REGULAR_CHAR | SPECIAL_CHAR)* '"'; /*{
special_char42iYAwzSal = ['\b' , '\f' , '\r' , '\n' , '\t' , '\''  , '\\'  , '"'  ]
replace_char42iYAwzSal = ['\\b', '\\f', '\\r', '\\n', '\\t', '\\\'', '\\\\', '\'"']
for 42iYAwzSal in range(len(special_char42iYAwzSal)):
	self.text = self.text.replace(special_char42iYAwzSal[42iYAwzSal], replace_char42iYAwzSal[42iYAwzSal])
del special_char42iYAwzSal
del replace_char42iYAwzSal
};*/
fragment REGULAR_CHAR: ~('\b'  | '\f'  | '\r'  | '\n'  | '\t'  | '\''   | '\\'   | '"'  );
fragment SPECIAL_CHAR:   '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\\'' | '\\\\' | '\'"' ;

ARRAYLIT: 'Array' '(' ((ARRAYLIT ',')* ARRAYLIT) | IDX_ARR_ELEMENTS ')';
fragment IDX_ARR_ELEMENTS: 	((INTLIT   ',')* INTLIT  )
						  |	((FLOATLIT ',')* FLOATLIT)
						  |	((BOOLLIT  ',')* BOOLLIT )
						  |	((STRLIT   ',')* STRLIT  );

// Expressions
INT_SIGN: '-';
INT_ARIT: [+-*/%];
INT_RELA: '==' | '!=' | '>' | '>=' | '<' | '<=';

FLOAT_SIGN: '-';
FLOAT_ARIT: [+-*/];
FLOAT_RELA: '>' | '>=' | '<' | '<=';

BOOL_OPER: '!' | '&&' | '||' | '==';

STR_OPER: '+.';
STR_RELA: '==.';


WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;