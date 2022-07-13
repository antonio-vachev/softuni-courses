# SoftUni just got a new fancy parking lot. It even has online parking validation, except the online service doesn't
# work. It can only receive users' data, but it doesn't know what to do with it. Good thing you're on the dev team and
# know how to fix it, right?

# Write a program, which validates a parking place - users can register to enter the park
# and unregister to leave.

# The program receives 2 types of commands:
# •	"register {username} {license_plate_number}":

# The system only supports one car per user at the moment, so if a user tries to register another license plate
# using the same username, the system should print: "ERROR: already registered with plate number {
# license_plate_number}"

# If the check above passes successfully, the user should be registered, so the system
# should print: "{username} registered {license_plate_number} successfully"

# •	"unregister {username}":
# If the user is not present in the database, the system should print: "ERROR: user {username} not found"
# If the check above passes successfully, the system should print: "{username} unregistered successfully"

# After you execute all of the commands, print all the currently registered users
# and their license plates in the format:
# •	"{username} => {license_plate_number}"

# Input
# •	First line: n - number of commands - integer
# •	Next n lines: commands in one of the two possible formats:
# Register: "register {username} {license_plate_number}"
# Unregister: "unregister {username}"

# Example input:
# 5
# register John CS1234JS
# register George JAVA123S
# register Andy AB4142CD
# register Jesica VR1223EE
# unregister Andy

# Example output:
# John registered CS1234JS successfully
# George registered JAVA123S successfully
# Andy registered AB4142CD successfully
# Jesica registered VR1223EE successfully
# Andy unregistered successfully
# John => CS1234JS
# George => JAVA123S
# Jesica => VR1223EE


num_commands = int(input())
registered = {}

for num in range(num_commands):
    command = input().split()
    action = command[0]
    username = command[1]

    if action == "register":
        license_plate = command[2]
        if username not in registered:
            registered[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")

    else:
        if username not in registered:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del registered[username]

for key, value in registered.items():
    print(f"{key} => {value}")