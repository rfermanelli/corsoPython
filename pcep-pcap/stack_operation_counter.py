class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class Adding_Stack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__stack_sum = 0
        self.__stack_operation_counter = 0

    def push(self, val):
        self.__stack_sum = self.__stack_sum + val
        Stack.push(self, val)
        self.__stack_operation_counter = self.__stack_operation_counter + 1
        return self.__stack_sum

    def pop(self):
        val = Stack.pop(self)
        self.__stack_operation_counter = self.__stack_operation_counter + 1
        self.__stack_sum = self.__stack_sum - val
        return self.__stack_sum

    def get_sum(self):
        return self.__stack_sum

    def get_stack_operation_counter(self):
        return self.__stack_operation_counter
#

stk = Adding_Stack()

stk.push(12)
stk.push(11)
stk.push(40)
print(stk.get_sum())
stk.pop()
print(stk.get_sum())
print(stk.get_stack_operation_counter())



