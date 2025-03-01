from typing import Optional, List, Any

# CTL may have more than two ap, however due to the syntax within the formala.g4,
# and for simplicity we limit the size into 2
SIZE_LIMIT = 2


class Formula:
  """Represents a CTL formula."""

  def __init__(self, *args: Any):
    """
    Initialises a Formula object.  This constructor supports multiple overloaded signatures.

    Possible signatures:
        Formula(ap: str)  # Single atomic proposition
        Formula(tautology: bool) # True or False
        Formula(quantifier: str, ap: str) # Quantifier and atomic proposition
        Formula(quantifier: str, formula: Formula) # Quantifier and nested formula
        Formula(negation: bool, formula: Formula)  # Negation of a formula
        Formula(ap1: str, ap2: str, operator: str) # Two atomic propositions and an operator
        Formula(ap: str, formula: Formula, operator: str)
        Formula(formula: Formula, ap: str, operator: str)
        Formula(formula1: Formula, formula2: Formula, operator: str)
        Formula(quantifier: str, ap1: str, ap2: str, operator: str)
        Formula(quantifier: str, formula1: Formula, formula2: Formula, operator: str)
        Formula(quantifier: str, ap: str, formula: Formula, operator: str)
    """
    self.parent: Optional["Formula"] = None
    self.negation: bool = False
    self.quantifier: Optional[str] = None
    self.operator: Optional[str] = None

    #########################################################################
    #  atomic propositions, tautologies, and nested CTL formulas.
    #########################################################################
    self.ap: List[Optional[str]] = [None] * SIZE_LIMIT
    self.ap_neg: List[bool] = [False] * SIZE_LIMIT

    self.single_ap: bool = False
    self.tautology: List[Optional[str]] = [None] * SIZE_LIMIT
    self.single_tt: bool = False
    self.nested_ctl: List[Optional["Formula"]] = [None] * SIZE_LIMIT
    self.actions: Optional[List[Optional[Any]]] = None

    self._process_arguments(*args)

  def _process_arguments(self, *args: Any) -> None:
    """Handles argument processing based on the constructor's overloaded signatures."""

    num_args = len(args)

    if num_args == 1:
      self._handle_single_argument(args[0])
    elif num_args == 2:
      self._handle_two_arguments(args[0], args[1])
    elif num_args == 3:
      self._handle_three_arguments(args[0], args[1], args[2])
    elif num_args == 4:
      self._handle_four_arguments(args[0], args[1], args[2], args[3])
    else:
      raise ValueError(f"Invalid number of arguments: {num_args}")

  def _handle_single_argument(self, arg: Any) -> None:
    if isinstance(arg, str):
      # Formula(String ap)
      self._put_ap(arg, 0)
      self.single_ap = True
    elif isinstance(arg, bool):
      # Formula(boolean tautology)
      self.tautology[0] = "True" if arg else "False"
      self.single_tt = True
    else:
      raise TypeError(f"Invalid single argument type: {type(arg)}")

  def _handle_two_arguments(self, arg1: Any, arg2: Any) -> None:
    if isinstance(arg1, str) and isinstance(arg2, str):
      # Formula(String temporal, String ap)
      self._put_ap(arg2, 0)
      self.quantifier = arg1
    elif isinstance(arg1, str) and isinstance(arg2, Formula):
      # Formula(String temporal, Formula formula)
      self._put_formula(arg2, 0)
      self.quantifier = arg1
    elif isinstance(arg1, bool) and isinstance(arg2, Formula):
      # Formula(boolean neg, Formula formula)
      self.negation = arg1
      self.shallow_copy(arg2)
    else:
      raise TypeError(f"Invalid argument types for two arguments: {type(arg1)}, {type(arg2)}")

  def _handle_three_arguments(self, arg1: Any, arg2: Any, arg3: Any) -> None:
    if isinstance(arg1, str) and isinstance(arg2, str) and isinstance(arg3, str):
      # Formula(String ap, String ap2, String op)
      self._put_ap(arg1, 0)
      self._put_ap(arg2, 1)
      self.operator = arg3
    elif isinstance(arg1, str) and isinstance(arg2, Formula) and isinstance(arg3, str):
      # Formula(String ap, Formula formula2, String op)
      self._put_formula(arg2, 1)
      self._put_ap(arg1, 0)
      self.operator = arg3
    elif isinstance(arg1, Formula) and isinstance(arg2, str) and isinstance(arg3, str):
      # Formula(Formula formula, String ap2, String op)
      self._put_formula(arg1, 0)
      self._put_ap(arg2, 1)
      self.operator = arg3
    elif isinstance(arg1, Formula) and isinstance(arg2, Formula) and isinstance(arg3, str):
      # Formula(Formula formula, Formula formula2, String op)
      self._put_formula(arg1, 0)
      self._put_formula(arg2, 1)
      self.operator = arg3
    else:
      raise TypeError("Invalid argument types for three arguments.")

  def _handle_four_arguments(self, arg1: Any, arg2: Any, arg3: Any, arg4: Any) -> None:
    # Formula(String quantifier, String ap, String ap2, String op)
    # Formula(String quantifier, Formula formula, Formula formula2, String op)
    # Formula(String quantifier, String ap, Formula formula2, String op)
    self.quantifier = arg1

    if isinstance(arg2, str) and isinstance(arg3, str):
      self._put_ap(arg2, 0)
      self._put_ap(arg3, 1)
    elif isinstance(arg2, Formula) and isinstance(arg3, Formula):
      self._put_formula(arg2, 0)
      self._put_formula(arg3, 1)
    elif isinstance(arg2, str) and isinstance(arg3, Formula):
      self._put_ap(arg2, 0)
      self._put_formula(arg3, 1)
    else:
      raise TypeError("Invalid argument types for four arguments.")

    self.operator = arg4

  def get_parent(self) -> Optional["Formula"]:
    return self.parent

  def is_negation(self) -> bool:
    return self.negation

  def get_quantifier(self) -> Optional[str]:
    return self.quantifier

  def get_operator(self) -> Optional[str]:
    return self.operator

  def get_ap(self) -> List[Optional[str]]:
    return self.ap

  def get_ap_neg(self) -> List[bool]:
    return self.ap_neg

  def is_single_ap(self) -> bool:
    return self.single_ap

  def get_tautology(self) -> List[Optional[str]]:
    return self.tautology

  def is_single_tt(self) -> bool:
    return self.single_tt

  def get_nested_ctl(self) -> List[Optional["Formula"]]:
    return self.nested_ctl

  def get_actions(self) -> Optional[List[Optional[Any]]]:
    return self.actions

  def _put_ap(self, ap: str, index: int) -> None:
    """Adds an atomic proposition at the given index."""
    self.ap_neg[index] = len(ap) % 2 == 0
    self.ap[index] = ap[-1]

  def _put_formula(self, formula: "Formula", index: int) -> None:
    """Adds a nested formula at the given index."""
    if formula.single_ap:
      self._put_ap(formula.ap[0], index)
    elif formula.single_tt:
      self.tautology[index] = formula.tautology[0]
    else:
      self.nested_ctl[index] = formula
      formula.parent = self

  def shallow_copy(self, formula: "Formula") -> None:
    """Performs a shallow copy of another Formula object."""
    self.ap = formula.ap[:]
    self.ap_neg = formula.ap_neg[:]
    self.negation = formula.negation
    self.operator = formula.operator
    self.quantifier = formula.quantifier
    self.nested_ctl = formula.nested_ctl[:]
    self.tautology = formula.tautology[:]
    self.parent = formula.parent
    self.single_ap = formula.single_ap
    self.single_tt = formula.single_tt
    self.actions = formula.actions

  @staticmethod
  def add_actions(ctl: Any, formula: "Formula") -> None:
    """Adds actions to the formula and its nested formulas."""
    if formula.actions is None:
      formula.actions = [None] * 2

    if formula.quantifier is not None:
      if len(formula.quantifier) > 2:
        actions = [
          ctl.action_map.get(c) for c in formula.quantifier[1:] if c in ctl.action_map
        ]
        formula.actions[:len(actions)] = actions

        formula.quantifier = "".join(c for c in formula.quantifier if not c.islower())
    if formula.operator is not None and "U" in formula.operator:
      if formula.operator[0] in ctl.action_map:
        formula.actions[0] = ctl.action_map[formula.operator[0]]
      if formula.operator[-1] in ctl.action_map:
        formula.actions[1] = ctl.action_map[formula.operator[-1]]
      formula.operator = ''.join(c for c in formula.operator if not c.islower())

    for nested_formula in formula.nested_ctl:
      if nested_formula is not None:
        Formula.add_actions(ctl, nested_formula)
