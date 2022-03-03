// Student ID: 1953107
// Full name: Tran Minh Vu
// Group: CC03
// Lecturer: Dr.Nguyen Hua Phung

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}


/////////////////////////////////////////
/////////// Program structure ///////////
/////////////////////////////////////////

// Object-oriented programming
program: classDecl* EOF;

classDecl: CLASS_ ID (COLON ID)? LCB classMem* RCB;
classMem: attribute | method;

attribute: VAR_ (attrBody | attrNonInit) SEMI
         | VAL_ attrBody SEMI;
attrBody: identifier COLON vartype ASNOP expr
        | identifier COMMA attrBody COMMA expr;
attrNonInit: identifier (COMMA identifier)* COLON vartype;

method: normalMet | constructor | destructor;
normalMet: (ID | VID) LB paraList? RB scope;
constructor: CONSTRUCTOR_ LB paraList? RB scope;
destructor: DESTRUCTOR_ LB RB scope;
paraList: idList (SEMI idList)*;
idList: identifier (COMMA identifier)* COLON vartype;

// Statements
scope: LCB stmt* RCB;
stmt: declStmt | asnStmt | ifStmt | forStmt | breakStmt | contStmt | retStmt | insMetStmt | staMetStmt | scope;

declStmt: VAR_ (declBody | declNonInit) SEMI
        | VAL_ declBody SEMI;
declBody: ID COLON vartype ASNOP expr
        | ID COMMA declBody COMMA expr;
declNonInit: ID (COMMA ID)* COLON vartype;

identifier: ID | VID;

asnStmt: lhs ASNOP expr SEMI;
lhs: identifier | SELF_
   | lhs (LSB expr RSB)+
   | lhs DOT ID
   | ID CSMEM VID;

ifStmt: IF_ LB expr RB scope (elifStmt | elseStmt)?;
elifStmt: ELSEIF_ LB expr RB scope (elifStmt | elseStmt)?;
elseStmt: ELSE_ scope;

forStmt: FOREACH_ LB ID IN_ expr DOUBLEDOT expr (BY_ expr)? RB scope;
/*
scopeLoop: LCB stmtLoop* RCB;
stmtLoop: stmt | ifStmtLoop | breakStmt | contStmt;
ifStmtLoop: IF_ LB expr RB scopeLoop (elifStmtLoop | elseStmtLoop)?;
elifStmtLoop: ELSEIF_ LB expr RB scopeLoop (elifStmtLoop | elseStmtLoop)?;
elseStmtLoop: ELSE_ scopeLoop;
*/
breakStmt: BREAK_ SEMI;
contStmt: CONTINUE_ SEMI;

//callMetStmt: callMethod SEMI;
//callMethod: identifier exprList;

insMetStmt: expr DOT ID exprList SEMI; // instance method

staMetStmt: ID CSMEM VID exprList SEMI; // static method

retStmt: RETURN_ expr? SEMI;

// Expressions
expr: INTLIT | FLOATLIT | BOOLLIT | STRLIT | NULL_ | SELF_ | arrLit // literals
    | identifier // identifier
    | LB expr RB // brackets
    | <assoc=right> NEW_ ID exprList // object creation
    | ID CSMEM VID exprList? // static access
    | expr DOT ID exprList? // instance access
    | expr (LSB expr RSB)+ // index operator
    | <assoc=right> SUBOP expr // sign
    | <assoc=right> NOTOP expr // logical not
    | expr (MULOP | DIVOP | MODOP) expr // multiplying
    | expr (ADDOP | SUBOP) expr // adding
    | expr (ANDOP | OROP) expr // logical
    | expr (EQCMP | DIFCMP | LESCMP | GRECMP | LEQCMP | GEQCMP) expr // relational
    | expr (SADDOP | SEQCMP) expr; //string
exprList: LB (expr (COMMA expr)*)? RB;

arrDec: ARRAY_ LSB vartype COMMA INTLIT RSB;
vartype: INT_ | FLOAT_ | BOOL_ | STR_ | arrDec | ID;


/////////////////////////////////////////
/////////////// Literals ////////////////
/////////////////////////////////////////
// Int
INTLIT: (DECLIT | OCTLIT | HEXLIT | BINLIT) {self.text = self.text.replace('_','')};
fragment DECLIT: [0-9] | [1-9]('_'?[0-9])*;
fragment OCTLIT: '0' ( [0-7] | [1-7]('_'?[0-7])* );
fragment HEXLIT: '0'[xX] ([0-9A-F] | [1-9A-F]('_'?[0-9A-F])* );
fragment BINLIT: '0'[bB] ([01] | '1'('_'?[01])* );

// Float
FLOATLIT: INT_PART DEC_PART? EXP_PART? {self.text = self.text.replace('_','')};
fragment INT_PART: [0-9] | [1-9]('_'?[0-9])*;
fragment DEC_PART: '.' [0-9]*;
fragment EXP_PART: [eE] [-+]? INT_PART;

// Boolean
BOOLLIT: TRUE_ | FALSE_;

// String
STRLIT: '"' STR_CHAR* '"' /*{
special_char42iYAwzSal = ['\b' , '\f' , '\r' , '\n' , '\t' , '\''  , '\\'  , '"'  ]
replace_char42iYAwzSal = ['\\b', '\\f', '\\r', '\\n', '\\t', '\\\'', '\\\\', '\'"']
for _42iYAwzSal in range(len(special_char42iYAwzSal)):
	self.text = self.text.replace(replace_char42iYAwzSal[_42iYAwzSal], specialD_char42iYAwzSal[_42iYAwzSal])
del special_char42iYAwzSal
del replace_char42iYAwzSal
}*/;
fragment STR_CHAR: REGULAR_CHAR | SPECIAL_CHAR;
fragment REGULAR_CHAR: ~('\b'  | '\f'  | '\r'  | '\n'  | '\t'  | '\''   | '\\'   | '"'  );
fragment SPECIAL_CHAR:   '\\b' | '\\f' | '\\r' | '\\n' | '\\t' | '\\\'' | '\\\\' | '\'"' ;

// Array
arrLit: ARRAY_ exprList;


/////////////////////////////////////////
/////////////// Terminals ///////////////
/////////////////////////////////////////

// Main class and method
//PROGRAM_: 'Program';
//MAIN_: 'main';

// Keywords
BREAK_:		'Break';
CONTINUE_:		'Continue';
IF_:			'If';
ELSEIF_:		'Elseif';
ELSE_:			'Else';
FOREACH_:		'Foreach';
TRUE_:			'True';
FALSE_:		'False';
ARRAY_:		'Array';
IN_:			'In';
INT_:			'Int';
FLOAT_:		'Float';
BOOL_:			'Boolean';
STR_:			'String';
RETURN_:		'Return';
NULL_:			'Null';
CLASS_:		'Class';
VAL_:			'Val';
VAR_:			'Var';
CONSTRUCTOR_:	       'Constructor';
DESTRUCTOR_:	       'Destructor';
NEW_:			'New';
BY_:			'By';
SELF_:               'Self';

// Separators
SEMI:       ';';
COLON:      ':';
COMMA:      ',';
DOT:        '.';
DOUBLEDOT:  '..';
LB:         '('; // brackets
RB:         ')';
LSB:        '['; // square brackets
RSB:        ']';
LCB:        '{'; // curly brackets
RCB:        '}';

// Operators
ADDOP:		'+';
SUBOP:		'-';
MULOP:		'*';
DIVOP:		'/';
MODOP:		'%';
NOTOP:		'!';
ANDOP:		'&&';
OROP:		'||';
EQCMP:		'==';
ASNOP:		'=';
DIFCMP:	'!=';
LESCMP:	'<';
LEQCMP:	'<=';
GRECMP:	'>';
GEQCMP:	'>=';
SEQCMP:  	'==.';
SADDOP:	'+.';
CSMEM:		'::';


/////////////////////////////////////////
////////////// Identifiers //////////////
/////////////////////////////////////////
ID: [a-zA-Z_] [a-zA-Z0-9_]*;
VID: '$'[a-zA-Z0-9_]+;


/////////////////////////////////////////
////// Skippers and error handlers //////
/////////////////////////////////////////

COMMENT: '##' CMT_CHAR* '##' -> skip;
fragment CMT_CHAR: ~'#' | '#'(~'#')+;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .{raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' STR_CHAR* {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE: '"' (~'"')*?('\\'~[bfrnt'\\] | '\''~'"') {raise IllegalEscape(self.text[1:])};