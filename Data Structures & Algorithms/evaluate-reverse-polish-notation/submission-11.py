class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackNum = []
        for i, a in enumerate(tokens):
            if a.lstrip('-').isnumeric():
                stackNum.append(int(a))
            else:
                valLast = stackNum.pop() 
                valFirst = stackNum.pop()
                res = 0
                match a:
                    case '+':
                        res = valFirst + valLast
                    case '-':
                        res = valFirst - valLast
                    case '*':
                        res = valFirst * valLast
                    case '/':
                        res = int(valFirst / valLast) if valFirst != 0 else 0
                stackNum.append(res)
                
        return stackNum[-1]