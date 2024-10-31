# Una classe iteratore equivalente all'iteratore costruito con le clasuole for e in
class Generator:
    def __init__(self, limite):
        self.limite = limite
        self.fine = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.fine = self.fine + 1
        if self.fine == self.limite:
            raise StopIteration
        return self.fine


# Una classe iteratore che mappa i primi n elementi della successione di Fibonacci
class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.a_prec = 1
        self.a_succ = 1
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.indice < self.n:
            self.indice += 1
            if self.indice == 1 or self.indice == 2:
                return 1
            else:
                self.a_prec, self.a_succ = self.a_succ, self.a_prec + self.a_succ
                return self.a_succ
        else:
            raise StopIteration


# Una classe iteratore che mappa i primi n elementi della successione di Fibonacci
class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.a_prec = 1
        self.a_succ = 1
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.indice = self.indice + 1
        if self.indice == 1 or self.indice == 2:
            return 1
        if self.indice <= self.n:
            self.a_prec, self.a_succ = self.a_succ, self.a_prec + self.a_succ
            return self.a_succ
        else:
            raise StopIteration


n = 10
generator_list = [i for i in Generator(n)]
print('I primi', n, 'elementi del generatore sono:', generator_list)

n = 10
fibonacci_iterator_list = [a for a in FibonacciIterator(n)]
print('I primi', n, 'elementi della successione di Fibonacci sono:', fibonacci_iterator_list)


# Una funzione iteratore yield che mappa i primi n elementi della successione di Fibonacci
def fibonacci_yield_iterator(n):
    a_prec = 1
    a_succ = 1
    indice = 0
    while indice < n:
        indice = indice + 1
        if indice == 1 or indice == 2:
            yield 1
        else:
            a_prec, a_succ = a_succ, a_prec + a_succ
            yield a_succ


n = 10
fibonacci_yield_list = [a for a in fibonacci_yield_iterator(n)]
print('I primi', n, 'elementi della successione di Fibonacci sono:', fibonacci_yield_list)
