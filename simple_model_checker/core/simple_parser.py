from antlr4 import *
from simple_model_checker.grammar.FormulaLexer import FormulaLexer
from simple_model_checker.grammar.FormulaParser import FormulaParser

class SimpleParser:
    """
    A CTL Formula parser.
    The SimpleParser parses the CTL formula provided from a JSON file (e.g. /data/ctl.json) and generates
    an instance of Formula. The Parser and the Lexer are generated using Antlr version 4.x.
    The Grammar used is shown in Formula.g4
    """

    @staticmethod
    def parse_ctl(input_string):
        """
        Returns the formula generated from the CTL query.

        Args:
            input_string (str): CTL Query (e.g. "AF(a && AG (a || A(a U b)))")

        Returns:
            Formula: A Formula object
        """
        input_stream = InputStream(input_string)
        lexer = FormulaLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = FormulaParser(stream)
        formula = parser.query()
        return formula.result

if __name__ == '__main__':
    ctl_formula = "AF(a && AG (a || A(a U b)))"
    try:
        formula_obj = SimpleParser.parse_ctl(ctl_formula)
        # TODO: Create a better print statement
        print(formula_obj)
    except Exception as e:
        print(f"Error parsing CTL formula: {e}")