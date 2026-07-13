class Solution:
    def isValid(self, s: str) -> bool:
        # Approach

        """
        Two-stack approach:
        - Take two stacks, put all brackets in 1st stack
        - If the 2nd stack is empty then pop from 1st and put in 2nd
        - Now peak the two brackets in 1st and 2nd
        - Check if 1st bracket is opened and 2nd one is closed
        - If push the new bracket to 2nd.
        - Keep doing until both the stacks are empty
        - If either one is non-empty then not valid parentheses
        """

        class Stack:
            def __init__(self):
                self.arr = []

            def push(self, val):
                self.arr.append(val)

            def pop(self):
                if not self.arr:
                    return None
                
                return self.arr.pop()

            def peak(self):
                if not self.arr:
                    return None
                
                return self.arr[-1]

            def size(self):
                return len(self.arr)

            def display(self):
                for c in self.arr:
                    print(c)

        s1 = Stack()
        for c in s:
            s1.push(c)

        # Helper stack
        s2 = Stack()

        # [(])
        while s1.size():
            if s2.size() == 0:
                s2.push(s1.pop())
            
            is_square = (s1.peak() == "[" and s2.peak() == "]")
            is_curly = s1.peak() == "{" and s2.peak() == "}"
            is_brace = s1.peak() == "(" and s2.peak() == ")"

            if is_square or is_curly or is_brace:
                s2.pop()
                s1.pop()
            else:
                val = s1.pop()
                if val:
                    s2.push(val)
        
        # If s2 not empty then its not a valid
        return False if s2.size() > 0 else True



        