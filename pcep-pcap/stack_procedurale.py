stack = [0,1]

def push_stack(elemento_stack):
    stack.append(elemento_stack)
    return

def pop():
    return stack.pop()

push_stack(2)
push_stack(3)
push_stack(4)
print(stack)
pop()
print(stack)
