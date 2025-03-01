from simple_model_checker.grammar.ctl import CTL
from simple_model_checker.grammar.formula import Formula

actionMap = {
  'p': ["act", "act1"],
  'q': ["act2", "act3", "act4"],
}
ctl = CTL(action_map=actionMap)

formula1 = Formula("AG", Formula("a", "b", "&&"))  # AG(a && b)
Formula.add_actions(ctl, formula1)
print(f"Formula: AG(a && b), Quantifier: {formula1.get_quantifier()}, Actions: {formula1.get_actions()}")

formula2 = Formula("A", "a", "b", "pUq")  # A( a pUq b )
Formula.add_actions(ctl, formula2)
print(
  f"Formula: A( a pUq b ), Quantifier: {formula2.get_quantifier()}, Operator: {formula2.get_operator()},"
  f" Actions: {formula2.get_actions()}")

formula3 = Formula("EF", Formula("b", Formula("AG", "c"), "||"))  # EF( b || AG (c) )
Formula.add_actions(ctl, formula3)
print(
  f"Formula: EF(b || AG(c)), Quantifier: {formula3.get_quantifier()}, "
  f" Nested: {formula3.get_nested_ctl()[1].get_quantifier() if formula3.get_nested_ctl()[1] else None},"
  f" Actions: {formula3.get_actions()}")

formula4 = Formula(True, Formula("AG", "c"))  # !AG(c)
print(f"Formula: !AG(c), Negation: {formula4.is_negation()}, Quantifier: {formula4.get_quantifier()}")

formula5 = Formula("a")  # a
print(f"Formula: a, Single AP: {formula5.is_single_ap()}, AP: {formula5.get_ap()}")

formula6 = Formula(True)  # True
print(f"Formula: True, Single Tautology: {formula6.is_single_tt()}, Tautology: {formula6.get_tautology()}")
