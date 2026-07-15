class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Brute-force: Push numbers to stack until an operator appears
        # Now perform the math operation on these numbers and store back the the result to stack
        # add new number to stack repeat until all numbers are calculated.
        # Pop the one last standing number from stack as a result

        # Invariant: For the expression, the operators appears after the operands
        # State: Remember the integers to calculate, maintain the order - LIFO
        # Violates: When there are more that two numbers or single number or no number before the operator
        #           when there are multiple operators for an operator
        # recover: For multiple operands consider only two number for single operator
        #           For multiple operator take one at time
        #           for mismatched operands and operators cannot be recovered

        # Edgecases: Zero division, truncate decimal

        stack = []


        # ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        # 10 * (6 / ((9 + 3) * -11)) + 17 + 5


        for t in tokens:
            if t in ("+", "/", "*", "-"):
                num2 = stack.pop()
                num1 = stack.pop()
                num = 0
                if t == "+":
                    num = num1 + num2
                elif t == "/":
                    num = int(num1 / num2)
                elif t == "*":
                    num = num1 * num2
                elif t == "-":
                    num = num1 - num2
                print(num1, t, num2)
                stack.append(num)
            else:
                stack.append(int(t))
        return stack.pop() if len(stack) == 1 else 0


        