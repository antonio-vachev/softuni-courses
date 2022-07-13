# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough.
# However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# •	"Shadowmourne" - requires 250 Shards
# •	"Valanyr" - requires 250 Fragments
# •	"Dragonwrath" - requires 250 Motes

# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.

# You will be given lines of input in the format: "{quantity1} {material1} {quantity2} {material2} …"
# Keep track of the key materials - the first one that reaches 250, wins the race.
# At that point, you have to print that the corresponding legendary item is obtained.

# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards} fragments: {number_of_fragments} motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.

# Example input:
# 123 silver 6 shards 8 shards 5 motes
# 9 fangs 75 motes 103 MOTES 8 Shards
# 86 Motes 7 stones 19 silver

# Example output:
# Dragonwrath obtained!
# shards: 22
# fragments: 0
# motes: 19
# silver: 123
# fangs: 9


requirement = 250
collecting = True
key_materials = {}
junk_materials = {}

while collecting:
    collected = input().split(" ")
    quantities = [int(num) for index, num in enumerate(collected) if index % 2 == 0]
    items = [item.lower() for index, item in enumerate(collected) if index % 2 > 0]

    for index, item in enumerate(items):
        if item == "shards" or item == "fragments" or item == "motes":
            if item not in key_materials:
                key_materials[item] = 0
            key_materials[item] += quantities[index]
            if key_materials[item] >= requirement:
                if item == "shards":
                    print("Shadowmourne obtained!")
                    key_materials[item] -= requirement
                elif item == "fragments":
                    print("Valanyr obtained!")
                    key_materials[item] -= requirement
                elif item == "motes":
                    print("Dragonwrath obtained!")
                    key_materials[item] -= requirement
                collecting = False
                break
        else:
            if item not in junk_materials:
                junk_materials[item] = 0
            junk_materials[item] += quantities[index]

if "shards" in key_materials:
    print(f"shards: {key_materials['shards']}")
else:
    print("shards: 0")
if "fragments" in key_materials:
    print(f"fragments: {key_materials['fragments']}")
else:
    print("fragments: 0")
if "motes" in key_materials:
    print(f"motes: {key_materials['motes']}")
else:
    print("motes: 0")

for item in junk_materials:
    print(f"{item}: {junk_materials[item]}")
