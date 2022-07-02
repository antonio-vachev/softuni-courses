numbers_list = list(map(int, input().split(" ")))

while True:
    command = input().split(" ")
    if "Finish" in command:
        break
    elif "Add" in command:
        numbers_list.append(int(command[1]))
    elif "Remove" in command:
        for index, num in enumerate(numbers_list):
            if num == int(command[1]):
                numbers_list.pop(index)
                break
    elif "Replace" in command:
        for index, num in enumerate(numbers_list):
            if num == int(command[1]):
                numbers_list[index] = int(command[2])
                break
    elif "Collapse" in command:
        for index, num in enumerate(numbers_list):
            if num < int(command[1]):
                numbers_list = [x for x in numbers_list if x >= int(command[1])]

print(" ".join([str(x) for x in numbers_list]))
