from typing import List

class Tokenizer:
    def __init__(self, expression: str) -> None:
        self.expression = expression.strip()
        self.index = 0

    def tokenize(self) -> List[str]:
        tokens = []
        number = []
        open_brackets = 0
        close_brackets = 0

        while self.index < len(self.expression):
            c = self.expression[self.index]

            if c.isdigit() or c == '.':
                number.append(c)
            else:
                if c != ' ':
                    if number:
                        tokens.append(''.join(number))
                        number.clear()

                    if c == '(':
                        open_brackets += 1
                    elif c == ')':
                        close_brackets += 1

                    tokens.append(c)

            self.index += 1

        if number:
            tokens.append(''.join(number))
        return tokens
