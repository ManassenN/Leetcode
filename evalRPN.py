class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token in operators:
                # Pop two operands from the stack
                operand2 = stack.pop()
                operand1 = stack.pop()

                # Apply the operator and push the result back onto the stack
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                elif token == '/':
                    # Note: The division between two integers always truncates toward zero in this case
                    stack.append(int(operand1 / operand2))
            else:
                # If the token is an operand, push it onto the stack
                stack.append(int(token))

        # The final result is on top of the stack
        return stack[0]


