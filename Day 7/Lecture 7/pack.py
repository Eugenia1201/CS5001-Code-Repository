""" Dog And Pack
"""


class Dog:
    def __init__(self, pack):
        self.pack = pack
        self.fed = False

    def eat(self, food, share):
        self.fed = True
        if share and (self.pack is not None):
            self.pack.share_food(food)


class Pack:
    def __init__(self, animal_class):
        self.fed = False
        self.members = [animal_class(self) for _ in range(3)]
        # create 3 animals

    def share_food(self, food):
        for member in self.members:
            member.eat(food, False)
        self.fed = True


if __name__ == "__main__":
    p = Pack(Dog)
    d = p.members[0]
    d.eat("dog food", True)
    pass
