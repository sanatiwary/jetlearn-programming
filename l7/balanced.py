# x = input("enter a string: ")
# if (x[0] == "(" and x[-1] == ")") or (x[0] == "[" and x[-1] == "]") or (x[0] == "{" and x[-1] == "}") or (x[0] != "(" and x[0] != "[" and x[0] != "{" and x[-1] != ")" and x[-1] != "]" and x[-1] != "}"):
#     print("balanced")
# else:
#     print("unbalanced")
openList = ["(", "[", "{"]
closeList = [")", "]", "}"]

def check(input):
    stack = []
    for i in input:
        if i in openList:
            stack.append(i)
        elif i in closeList:
            pos = closeList.index(i)
            if len(stack) > 0 and openList[pos] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return "unbalanced"
    if len(stack) == 0:
        return "balanced"
    else:
        return "unbalanced"
    
print(check(input("enter a string: ")))