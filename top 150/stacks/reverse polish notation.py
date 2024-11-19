class Solution:
    def add(self, a,b):
        return a + b

    def subtract(self,a,b):
        return a- b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        return int(a/b)

    def evalRPN(self, tokens: List[str]) -> int:

        if len(tokens) == 1:
            return int(tokens[0])

        operators = {
                        '+': self.add,
                        '-': self.subtract,
                        '*': self.multiply,
                        '/': self.divide,
                    }

        stack = []
        output = 0

        for i in range(len(tokens)):
            if tokens[i] in operators:
                arg2 = int(stack.pop())
                arg1 = int(stack.pop())
                output = operators[tokens[i]](arg1,arg2)
                stack.append(output)
            else:
                stack.append(tokens[i])
 
        return output
