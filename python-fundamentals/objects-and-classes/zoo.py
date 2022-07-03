# Create a class Zoo. It should have a class attribute called __animals that stores the total count of the animals in
# the zoo. The __init__ method should only receive the name of the zoo. There you should also create 3 empty lists
# (mammals, fishes, birds). The class should also have 2 more methods:
# •	add_animal(species, name) - based on the species, adds the name to the corresponding list
# •	get_info(species) - based on the species returns a string in the following format:
# "{Species} in {zoo_name}: {names} Total animals: {total_animals}"
# On the first line, you will receive the name of the zoo. On the second line, you will receive number n.
# On the following n lines you will receive animal info in the format: "{species} {name}".
# Add the animal to the zoo to the corresponding list. The species could be "mammal", "fish", or "bird".
# On the final line, you will receive a species. At the end,
# print the info for that species and the total count of animals in the zoo.


class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, animal_name):

        if species == "mammal":
            self.mammals.append(animal_name)
        elif species == "fish":
            self.fishes.append(animal_name)
        elif species == "bird":
            self.birds.append(animal_name)
        zoo.__animals += 1

    def get_species(self, species):
        if species == "mammal":
            return ", ".join(self.mammals)
        elif species == "fish":
            return ", ".join(self.fishes)
        elif species == "bird":
            return ", ".join(self.birds)

    def get_info(self, info):
        result = ""
        if info == "mammal":
            result += f"Mammals in {self.name}: {self.get_species(info)}\n"
        elif info == "fish":
            result += f"Fishes in {self.name}: {self.get_species(info)}\n"
        elif info == "bird":
            result += f"Birds in {self.name}: {self.get_species(info)}\n"
        result += f"Total animals: {zoo.__animals}"
        return result


name = input()
zoo = Zoo(name)

for n in range(int(input())):
    species, animal = input().split(" ")
    zoo.add_animal(species, animal)

info = input()
print(zoo.get_info(info))
