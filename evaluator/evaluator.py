from typing import Union, List
from collections import deque

class Evaluator:
    def evaluate(self, tokens: List[str]) -> Union[float, None]:
        numbers = deque()
        operators = deque()

        for token in tokens:
            if token == '(':
                operators.append(token)
            elif token == ')':
                while operators[-1] != '(':
                    numbers.append(self.apply_operation(operators.pop(), numbers.pop(), numbers.pop()))
                operators.pop()
            elif token in '+-*/':
                while operators and operators[-1] in '+-*/':
                    numbers.append(self.apply_operation(operators.pop(), numbers.pop(), numbers.pop()))
                operators.append(token)
            else:
                numbers.append(float(token))

        while operators:
            numbers.append(self.apply_operation(operators.pop(), numbers.pop(), numbers.pop()))

        return numbers[0] if numbers else None

    @staticmethod
    def apply_operation(op: str, b: float, a: float) -> float:
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
