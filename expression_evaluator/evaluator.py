from typing import Union, List, Deque
from collections import deque

class Evaluator:
    def evaluate(self, tokens: List[str]) -> Union[float, None]:
        output = deque()
        operators = deque()
        
        for token in tokens:
            if token.isnumeric() or '.' in token:  # Operand
                output.append(float(token))
            elif token in '()+-*/^':  # Operator or Parentheses
                if token in '()':
                    self.handle_parentheses(token, operators, output)
                else:
                    self.handle_operator(token, operators, output)
        
        while operators:
            self.pop_operator_to_output(operators, output)
        
        if len(output) != 1:
            return None  # Invalid expression
        
        return output[0]

    @staticmethod
    def handle_parentheses(token: str, operators: Deque[str], output: Deque[float]) -> None:
        if token == '(':
            operators.append(token)
        else:  # token == ')'
            while operators and operators[-1] != '(':
                Evaluator.pop_operator_to_output(operators, output)
            operators.pop()  # Remove the open parenthesis

    @staticmethod
    def handle_operator(token: str, operators: Deque[str], output: Deque[float]) -> None:
        while operators and Evaluator.precedence(operators[-1]) >= Evaluator.precedence(token):
            Evaluator.pop_operator_to_output(operators, output)
        operators.append(token)

    @staticmethod
    def precedence(op: str) -> int:
        if op in '+-':
            return 1
        elif op in '*/':
            return 2
        elif op == '^':
            return 3
        return 0

    @staticmethod
    def pop_operator_to_output(operators: Deque[str], output: Deque[float]) -> None:
        op = operators.pop()
        b = output.pop()
        a = output.pop()
        output.append(Evaluator.apply_operation(op, a, b))

    @staticmethod
    def apply_operation(op: str, a: float, b: float) -> float:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ValueError("Division by zero")
            return a / b
        elif op == '^':
            return a ** b
