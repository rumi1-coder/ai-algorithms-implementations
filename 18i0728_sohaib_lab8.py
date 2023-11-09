from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


# Base class for all constraints
class Constraint(Generic[V, D], ABC):
    # The variables that the constraint is between
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    # Must be overridden by subclasses
    #@abstractmethod
    #def satisfied(self, assignment: Dict[V, D]) -> bool:
        #return "\n"
# A constraint satisfaction problem consists of variables of type V
# that have ranges of values known as domains of type D and constraints
# that determine whether a particular variable's domain selection is valid
class CSP(Generic[V, D]):

     def __init__ (self, variables: List[V], domains: Dict[V, List[D]]) -> None:
         self.variables: List[V] = variables  # variables to be constrained
         self.domains: Dict[V, List[D]] = domains  # domain of each variable
         self.constraints: Dict[V, List[Constraint[V, D]]] = {}
         for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")
     def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)

        # Check if the value assignment is consistent by checking all constraints
        # for the given variable against it

     def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                 return False
        return True

     def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
           # assignment is complete if every variable is assigned (our base case)
           if len(assignment) == len(self.variables):
               return assignment

           # get all variables in the CSP but not in the assignment
           unassigned: List[V] = [v for v in self.variables if v not in assignment]

           # get the every possible domain value of the first unassigned variable
           first: V = unassigned[0]
           for value in self.domains[first]:
               local_assignment = assignment.copy()
               local_assignment[first] = value
               # if we're still consistent, we recurse (continue)
               if self.consistent(first, local_assignment):
                   result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)
                   # if we didn't find the result, we will end up backtracking
                   if result is not None:
                       return result
           return None





class SendMoreMoneyConstraint(Constraint[str, int]):
    def __init__(self, letters: List[str]) -> None:
        super().__init__(letters)
        self.letters: List[str] = letters

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        # if there are duplicate values then it's not a solution
        #when two letters have the same digit then return false
        if len(set(assignment.values())) < len(assignment):
            return False

        # if all variables have been assigned, check if it adds correctly
        if len(assignment) == len(self.letters):
            s: int = assignment["S"]
            e: int = assignment["E"]
            n: int = assignment["N"]
            d: int = assignment["D"]
            m: int = assignment["M"]
            o: int = assignment["O"]
            r: int = assignment["R"]
            y: int = assignment["Y"]
            send: int = s * 1000 + e * 100 + n * 10 + d
            more: int = m * 1000 + o * 100 + r * 10 + e
            money: int = m * 10000 + o * 1000 + n * 100 + e * 10 + y
            return send + more == money
        return True  # no conflict


if __name__ == "__main__":
     letters: List[str] = ["S", "E", "N", "D", "M", "O", "R", "Y"]
     possible_digits: Dict[str, List[int]] = {}
     for letter in letters:
         possible_digits[letter] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
     possible_digits["M"] = [1]  # so we don't get answers starting with a 0
     csp: CSP[str, int] = CSP(letters, possible_digits)
     csp.add_constraint(SendMoreMoneyConstraint(letters))
     solution: Optional[Dict[str, int]] = csp.backtracking_search()
     if solution is None:
         print("No solution found!")
     else:
         print(solution)



