grammar ETHER;

options{
    language=Python3;
}

program: send EOF;

send: (sendtoken | sendeth)*;

sendeth: SENDETH LB ADDRESS COMA ADDRESS COMA AMOUNT RB SEMI;

sendtoken: SENDTOKEN LB ADDRESS COMA ADDRESS COMA TOKENID COMA AMOUNT RB SEMI;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

LB: '(';
RB: ')';
COMA: ',';
SEMI: ';';
	
SENDETH: S E N D E T H;
SENDTOKEN: S E N D T O K E N;

ADDRESS: '0x' [0-9a-fA-F]+;

AMOUNT: [0-9]+;
TOKENID: [0-9]*[a-zA-Z][0-9a-zA-Z]*;


fragment A: ('a'|'A');
fragment B: ('b'|'B');
fragment C: ('c'|'C');
fragment D: ('d'|'D');
fragment E: ('e'|'E');
fragment F: ('f'|'F');
fragment G: ('g'|'G');
fragment H: ('h'|'H');
fragment I: ('i'|'I');
fragment J: ('j'|'J');
fragment K: ('k'|'K');
fragment L: ('l'|'L');
fragment M: ('m'|'M');
fragment N: ('n'|'N');
fragment O: ('o'|'O');
fragment P: ('p'|'P');
fragment Q: ('q'|'Q');
fragment R: ('r'|'R');
fragment S: ('s'|'S');
fragment T: ('t'|'T');
fragment U: ('u'|'U');
fragment V: ('v'|'V');
fragment W: ('w'|'W');
fragment X: ('x'|'X');
fragment Y: ('y'|'Y');
fragment Z: ('z'|'Z');

ERRORTOK: .;
