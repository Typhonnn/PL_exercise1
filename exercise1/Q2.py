class AMixin:
    def mixinExample(self):
        return "in Amixin.mixinExample " + self.name


class A(AMixin):
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    a_instance = A("Question7")
    print(a_instance.mixinExample())
