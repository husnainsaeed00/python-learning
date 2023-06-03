import random
class Hat:
    houses = ["pak", "ind", "bwp"]
    @classmethod
    def sort(cls,name):
        print(name, "is in ",  random.choice(cls.houses))

Hat.sort("harry")