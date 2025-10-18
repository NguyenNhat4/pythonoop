

class A:
    def __init__(self, b: int, c: int):
        self._b = b
        self._c = c

    def tmpfunction(self):
        print(self._b, self._c)


a = A(1, 2)


a.tmpfunction()


