# You will receive a number representing the number of wagons a train has. Create a list (train) with the given length
# containing only zeros. Until you receive the command "End", you will receive some of the following commands:

# •	"add {people}" – you should add the number of people in the last wagon
# • "insert {index} {people}" - you should add the number of people at the given wagon
# • "leave {index} {people}" - you should remove the number of people from the wagon.

# There will be no case in which the people will be more than the count in the wagon. There will be no case in
# which the index is invalid! After you receive the "End" command print the train.

# Example input:
# 5
# add 10
# add 20
# insert 0 16
# insert 1 44
# leave 1 12
# insert 2 100
# insert 4 61
# leave 4 1
# add 15
# End

num_wagons = [0 for x in range(int(input()))]

while True:
    action = input()
    if action == "End":
        break
    elif "add" in action:
        action_list = action.split(" ")
        num_wagons[-1] += int(action_list[1])
    elif "insert" in action:
        action_list = action.split(" ")
        index = int(action_list[1])
        people = int(action_list[2])
        num_wagons[index] += people
    elif "leave" in action:
        action_list = action.split(" ")
        index = int(action_list[1])
        people = int(action_list[2])
        num_wagons[index] -= people

print(num_wagons)

