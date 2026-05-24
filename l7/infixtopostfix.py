def precedence(c):
    if c == "^":
        return 3
    elif c == "/" or c == "*":
        return 2
    elif c == "+" or c == "-":
        return 1
    
def IFtoPF(infix):
    stack = []
    postfix = []
    operators = ["^", "/", "*", "+", "-"]

    for i in infix:
        if ("a" <= i <= "z") or ("A" <= i <= "Z") or ("0" <= i <= "9"):
            postfix.append(i)
        elif i in operators:
            while stack and precedence(stack.top()) >= precedence(i):
                postfix.append(stack.pop())
            stack.push(i)
        elif i == "(":
            stack.push(i)
        elif i == ")":
            while stack.top() != "(":
                postfix.append(stack.pop())
            stack.pop()
        
