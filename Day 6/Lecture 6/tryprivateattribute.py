class Dog ():
    def __init__(self, favorite_toy):
        self.__favorite_toy = favorite_toy

    def fetch(self):
        print(f"bring the {self.__favorite_toy}")


my_dog = Dog('rubber duck')
# my_dog.fetch()
my_dog.__favorite_toy = 'stuffed mouse'  # this will fail (raise an exception)
