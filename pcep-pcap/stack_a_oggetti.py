class stack:
    def __init__(self):
        self.__stack_list = []

    def push_stack(self, elemento_stack):
        self.__stack_list.append(elemento_stack)
        return

    def pop_stack(self):
        return self.__stack_list.pop()


stack_object_1 = stack()
stack_object_2 = stack()

stack_object_1.push_stack(3)
stack_object_2.push_stack(stack_object_1.pop_stack())

print(stack_object_2.pop_stack())
#
little_stack = stack()
another_stack = stack()
funny_stack = stack()

little_stack.push_stack(1)
another_stack.push_stack(little_stack.pop_stack() + 1)
funny_stack.push_stack(another_stack.pop_stack() - 2)

print(funny_stack.pop_stack())

class stack_sum(stack):
    def __init__(self):
        stack.__init__(self)
        self.__sum =0

    def get_sum(self):
        return self.__sum

    def push_stack(self, elemento_stack):
        self.__sum += elemento_stack
        Stack.push(self, val)

    def pop_stack(self):
        self.__sum -= self.__stack_list.pop()
        return val







