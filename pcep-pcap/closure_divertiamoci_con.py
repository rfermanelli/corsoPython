def f(x):
    esp = x ** 2
    def r(z):
        return z ** esp

    return r

x = 10
y = f(10)
print(y(2))




