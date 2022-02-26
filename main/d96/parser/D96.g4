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
//classProgram: CLASS_ PROGRAM_ LCB (attribute | method)* methodMain (attribute | method)* RCB;

attribute: declare;

method: identifier LB paraList? RB scope | constructor | destructor;
constructor: CONSTRUCTOR_ LB paraList? RB scope;
destructor: DESTRUCTOR_ LB RB scope;
//methodMain: MAIN_ LB RB scopeMain;
paraList: idList (SEMI idList)*;
idList: identifier (COMMA identifier)* COLON (INT_ | FLOAT_ | BOOL_ | STR_);

// Statements
scope: LCB stmt* RCB;
stmt: declare | asnStmt | ifStmt | forStmt | retStmt | callMethod SEMI | scope
    | expr DOT ID LB (expr (COMMA expr)*)? RB SEMI // instance method
    | ID CSMEM VID LB (expr (COMMA expr)*)? RB SEMI; // static method

//scopeMain: LCB stmtMain* RCB;
//stmtMain: declare | asnStmt | ifStmt | forStmt | insAttr | staAttr | insMethod | staMethod;

declare: VAR_ (declBody | notvalBody) SEMI
       | VAL_ declBody SEMI;
declBody: identifier COLON vartype ASNOP expr
        | identifier COMMA declBody COMMA expr;
notvalBody: identifier (COMMA identifier)* COLON vartype;

identifier: ID | VID;

asnStmt: <assoc=right> lhs ASNOP expr SEMI;
lhs: identifier
   | lhs LSB expr RSB
   | lhs DOT lhs;

ifStmt: IF_ LB expr RB scope (ELSEIF_ LB expr RB scope)* (ELSE_ scope)?;

forStmt: FOREACH_ LB ID IN_ expr DOUBLEDOT expr (BY_ expr)? RB scopeLoop;
scopeLoop: LCB stmtLoop* RCB;
stmtLoop: stmt | ifStmtLoop | breakStmt | contStmt;
ifStmtLoop: IF_ LB expr RB scopeLoop (ELSEIF_ LB expr RB scopeLoop)* (ELSE_ scopeLoop)?;
breakStmt: BREAK_ SEMI;
contStmt: CONTINUE_ SEMI;

callMethod: identifier LB (expr (COMMA expr)*)? RB;

retStmt: RETURN_ expr? SEMI;

// Expressions
expr: INTLIT | FLOATLIT | BOOLLIT | STRLIT | NULL_ | SELF_ | arrLit | identifier // literals and identifiers
    | LB expr RB // brackets
    | NEW_ ID LB (expr (COMMA expr)*)? RB // object creation
    | ID CSMEM VID ((LB expr (COMMA expr)*)? RB)? // static access
    | expr DOT ID (LB expr (COMMA expr)* RB)? // instance access
    | expr (LSB expr RSB) // index operator
    | SUBOP expr // sign
    | NOTOP expr // logical not
    | expr (MULOP | DIVOP | MODOP) expr // multiplying
    | expr (ADDOP | SUBOP) expr // adding
    | expr (ANDOP | OROP) expr // logical
    | expr (EQCMP | DIFCMP | LESCMP | GRECMP | LEQCMP | GEQCMP) expr // relational
    | expr (SADDOP | SEQCMP) expr; //string
/*
objExpr: NEW_ ID LB (expr (COMMA expr)*)? RB
       | NULL_ | SELF_;
insAttr: expr DOT ID;
staAttr: ID CSMEM VID;
insMethod: expr DOT ID LB (expr (COMMA expr)*)? RB;
staMethod: ID CSMEM VID LB (expr (COMMA expr)*)? RB;
*/

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
arrLit: ARRAY_ LB (expr (COMMA expr)*)? RB;


/////////////////////////////////////////
/////////////// Terminals ///////////////
/////////////////////////////////////////

// Main class and method
//PROGRAM_: 'Program';
//MAIN_: 'main';

// Keywords
BREAK_:			'Break';
CONTINUE_:		'Continue';
IF_:			'If';
ELSEIF_:		'Elseif';
ELSE_:			'Else';
FOREACH_:		'Foreach';
TRUE_:			'True';
FALSE_:			'False';
ARRAY_:			'Array';
IN_:			'In';
INT_:			'Int';
FLOAT_:			'Float';
BOOL_:			'Boolean';
STR_:			'String';
RETURN_:		'Return';
NULL_:			'Null';
CLASS_:			'Class';
VAL_:			'Val';
VAR_:			'Var';
CONSTRUCTOR_:	'Constructor';
DESTRUCTOR_:	'Destructor';
NEW_:			'New';
BY_:			'By';
SELF_:          'Self';

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
DIFCMP:		'!=';
LESCMP:		'<';
LEQCMP:		'<=';
GRECMP:		'>';
GEQCMP:		'>=';
SEQCMP:  	'==.';
SADDOP:	    '+.';
//CIMEM:	'.';
CSMEM:		'::';
//NEW:		'New';


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