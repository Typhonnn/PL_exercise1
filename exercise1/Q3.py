class A:
    # def __init__(self):
    #     print("A.__init__")

    def m(self):
        print("m of A called")


class B(A):
    # def __init__(self):
    #     print(super())

    def m(self):
        print("m of B called")
        A.m(self)


class C(A):
    def m(self):
        print("m of C called")
        b = B()
        b.m()
        A.m(self)
        # super().__init__()


class D(B, C):
    def m(self):
        print("m of D called")
        b = B()
        b.m()
        C.m(self)
        # super().m()
        # A.__init__(self)


d = D()
d.m()
