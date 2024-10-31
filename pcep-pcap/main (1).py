class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val


print(ExampleClass.__dict__)
example_object = ExampleClass(2)
example_object.invaria = 0

if hasattr(example_object, 'invaria'):
     del example_object.__dict__['invaria']
     if hasattr(example_object, 'invaria'):
         pass
     else:
         print('oh yeah!!!')
print(ExampleClass.__dict__)
print(example_object.__dict__)

if hasattr(ExampleClass, 'varia'):
    print('yeah!!!')
