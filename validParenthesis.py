# Leetcode 20

# Algorithm:
# For this problem, we will use a stack data structure to facilitate ourselves.
# We will loop through the string and check if the character is an opening bracket or a closing bracket.
# We can check this by adding each closing bracket to a map and mapping it to its opening bracket.
# If the current character is a closing bracket, we will check if the stack is non-empty. We will take the top of the stack and compare that against the value of that character in the map.
# This means that we use the existing character as a key and obtain its value from the map and then check if the top of the stack is the same.
# If it is, we go ahead and pop the value else we return false.
# However, if the character is an opening bracket instead, we just add it to the stack. 
# We return true in the end if the stack is empty else we return false.

# Code:
def validParenthesis(s: str) -> bool:
    closeToOpen = {")":"(", "]":"[", "}":"{"}
    stack = []
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

print(validParenthesis("()"))
print(validParenthesis("()[]{}"))
print(validParenthesis("(])"))
print(validParenthesis("([)]"))
print(validParenthesis("}"))
print(validParenthesis("((((({{{{{[[[[]]]]}}}}})))))"))

