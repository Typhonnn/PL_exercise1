"""Author: Tal Balelty - 312270291"""


class AMixin:
    def mixinExample(self):
        return "in Amixin.mixinExample " + self.name


class A(AMixin):
    def __init__(self, name):
        self.name = name


def MixIn(TargetClass, MixInClass):
    if MixInClass not in TargetClass.__bases__:
        TargetClass.__bases__ += (MixInClass,)


if __name__ == "__main__":
    a_instance = A("Question7")
    MixIn(A, AMixin)
    print(a_instance.mixinExample())
