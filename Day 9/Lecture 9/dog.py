class Dog:
    def __init__(self):
        self.fed = False

    def eat(self, food):
        self.fed = True

    def bark(self):
        raise AttributeError("bark")
