# You are a facility manager at a large business center. One of your responsibilities is to check if each conference
# room in the center has enough chairs for the visitors.

# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the following n lines for each room, you will receive
# information about the chairs in the room and the number of visitors.

# Each chair will be presented with the char "X".

# Next, there will be a single space and the number of visitors at the end. For example: "XXXXX 4" (5 chairs and 4
# visitors). Keep track of the free chairs:

# •	If there are not enough chairs in a specific room, print the following
# message: "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.

# •	Otherwise, print: "Game On, {total_free_chairs} free chairs left".

# Example input:
# 4
# XXXX 4
# XX 1
# XXXXXX 3
# XXX 3

num_rooms = int(input())
total_chairs = 0
flag = False

for room in range(1, num_rooms + 1):
    visitors_chairs = input().split(" ")
    room_chairs = len(visitors_chairs[0])
    room_visitors = int(visitors_chairs[1])

    if room_visitors > room_chairs:
        print(f"{room_visitors - room_chairs} more chairs needed in room {room}")
        flag = True
    else:
        total_chairs += room_chairs - room_visitors

if not flag:
    print(f"Game On, {total_chairs} free chairs left")