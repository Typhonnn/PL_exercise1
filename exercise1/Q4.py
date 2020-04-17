import enum
import logging

logging.basicConfig(filename="Q4Debug.log", level=logging.DEBUG,
                    format="%(asctime)s:%(lineno)d:%(levelname)s:%(message)s", filemode="w")


class AnimalType(enum.Enum):
    Mammal = 1
    Reptile = 2
    Bird = 3


class Animal:
    def __init__(self, name, n_legs, dob, animal_type):
        self.name = name
        self.n_legs = n_legs
        self.dob = dob
        self.animal_type = AnimalType(animal_type).name
        logging.debug("Class Animal created: {}, {}, {}, {}".format(self.name, self.n_legs, self.dob, self.animal_type))


class DomesticatedAnimal:
    def __init__(self, checkup_date):
        self.checkup_date = checkup_date
        logging.debug("Class DomesticatedAnimal created: {}".format(self.checkup_date))


class Feline(Animal):
    def __init__(self, name, n_legs, dob, animal_type, mustache_len):
        self.mustache_len = mustache_len
        super().__init__(name, n_legs, dob, animal_type)
        logging.debug(
            "Class Feline attribute: {}, {}, {}, {}, {}".format(self.name, self.n_legs, self.dob, self.animal_type,
                                                                self.mustache_len))


class Tiger(Feline):
    def __init__(self, name, n_legs, dob, animal_type, mustache_len):
        super().__init__(name, n_legs, dob, animal_type, mustache_len)
        logging.debug(
            "Class Tiger created: {}, {}, {}, {}, {}".format(self.name, self.n_legs, self.dob, self.animal_type,
                                                             self.mustache_len))


class HouseCat(Feline, DomesticatedAnimal):
    def __init__(self, name, n_legs, dob, animal_type, mustache_len, checkup_date):
        super().__init__(name, n_legs, dob, animal_type, mustache_len)
        DomesticatedAnimal.__init__(self, checkup_date)
        logging.debug(
            "Class HouseCat created: {}, {}, {}, {}, {}, {}".format(self.name, self.n_legs, self.dob, self.animal_type,
                                                                    self.mustache_len, self.checkup_date))


def create_house_cat():
    name = input("Enter Name: ")
    dob = input("Enter Date of Birth: ")
    mustache_len = input("Enter Mustache Length: ")
    checkup_date = input("Enter Latest Vet Checkup Date: ")
    return HouseCat(name, 4, dob, 1, mustache_len, checkup_date)


def create_tiger():
    name = input("Enter Name: ")
    dob = input("Enter Date of Birth: ")
    mustache_len = input("Enter Mustache Length: ")
    return Tiger(name, 4, dob, 1, mustache_len)


def count_animals(animals):
    count_cats = 0
    count_tigers = 0
    for ani in animals:
        if ani is HouseCat:
            count_cats += 1
        else:
            count_tigers += 1
    print("Cats: {}\nTigers: {}".format(count_cats, count_tigers))


cat = HouseCat("Gorge", 4, "12/03/2015", 1, 5, "15/04/2020")
print(cat)
tiger = Tiger("Tiger", 4, "15/07/2018", 1, 10)
print(tiger)

while True:
    print("To Create New Animal Choose:\n1. House Cat\n2. Tiger\nTap any key to exit.")
    choose = input()
    animals = []
    if choose == '1':
        animals.append(create_house_cat())
    elif choose == '2':
        animals.append(create_tiger())
    else:
        count_animals(animals)
        exit(0)
