grammar Formula;

query returns [result]: formula EOF { $result = $formula.result };

formula returns [result] locals [op = False]:
      TRUE { $result = Formula(True) }
    | FALSE { $result = Formula(False) }
    | OPEN first (op_bool second { $op = True })? CLOSE
        {
            if $op:
                $result = Formula($first.result, $second.result, $op_bool.result)
            else:
                $result = Formula($first.result)
        }
    | OPEN first op_bool ctl_end CLOSE { $result = Formula($first.result, $ctl_end.result, $op_bool.result) }
    | neg ctl_init { $result = Formula($neg.result, $ctl_init.result) }
    | OPEN ctl_init (op_bool ctl_end { $op = True })? CLOSE
        {
            if $op:
                $result = Formula($ctl_init.result, $ctl_end.result, $op_bool.result)
            else:
                $result = $ctl_init.result
        }
    | EXISTS OPEN first UNTIL second CLOSE { $result = Formula("E", $first.result, $second.result, $UNTIL.text) }
    | ALL OPEN first UNTIL second CLOSE { $result = Formula("A", $first.result, $second.result, $UNTIL.text) }
    | EXISTS OPEN first UNTIL ctl_end CLOSE { $result = Formula("E", $first.result, $ctl_end.result, $UNTIL.text) }
    | ALL OPEN first UNTIL ctl_end CLOSE { $result = Formula("A", $first.result, $ctl_end.result, $UNTIL.text) }
    | EXISTS OPEN ctl_init UNTIL ctl_end CLOSE { $result = Formula("E", $ctl_init.result, $ctl_end.result, $UNTIL.text) }
    | ALL OPEN ctl_init UNTIL ctl_end CLOSE  { $result = Formula("A", $ctl_init.result, $ctl_end.result, $UNTIL.text) }
    | TEMPORAL OPEN first op_bool second CLOSE { $result = Formula($TEMPORAL.text, $first.result, $second.result, $op_bool.result) }
    | TEMPORAL OPEN first CLOSE { $result = Formula($TEMPORAL.text, $first.result) }
    | TEMPORAL OPEN first op_bool ctl_end CLOSE { $result = Formula($TEMPORAL.text, $first.result, $ctl_end.result, $op_bool.result) }
    | TEMPORAL OPEN ctl_init (op_bool ctl_end { $op = True })? CLOSE
        {
            if $op:
                $result = Formula($TEMPORAL.text, $ctl_init.result, $ctl_end.result, $op_bool.result)
            else:
                $result = Formula($TEMPORAL.text, $ctl_init.result)
        }
    ;

first returns [result]: ATOMIC { $result = $ATOMIC.text };
second returns [result]: ATOMIC { $result = $ATOMIC.text };

ctl_init returns [result]: formula { $result = $formula.result };

ctl_end returns [result]: formula { $result = $formula.result };

neg returns [result]: '!' { $result = True };

op_bool returns [result]:
      '&&' { $result = "&&" }
    | '||' { $result = "||" }
    | '=>' { $result = "=>" }
    | '<=>' { $result = "<=>" }
    ;

// Lexer rules
TRUE: 'True';
FALSE: 'False';
ALL: 'A';
EXISTS: 'E';
UNTIL: [a-z]? 'U' [a-z]?;
OPEN: '(';
CLOSE: ')';
ATOMIC: ('!')* [a-z];
TEMPORAL:
      'A' [a-z]? 'F' [a-z]?
    | 'A' [a-z]? 'G' [a-z]?
    | 'A' [a-z]? 'X' [a-z]?
    | 'E' [a-z]? 'F' [a-z]?
    | 'E' [a-z]? 'G' [a-z]?
    | 'E' [a-z]? 'X' [a-z]?
    ;

WS: [ \t\r\n\f]+ -> channel(HIDDEN);