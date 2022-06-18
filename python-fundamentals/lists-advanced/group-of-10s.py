# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the
# numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}". Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.

# Examples of grouping:
# Group of 10's: [8, 3]
# Group of 20's: [12, 17, 19]
# Group of 30's: [25]
# Group of 40's: [38, 35]
# Group of 50's: [50]

numbers = list(map(int, input().split(", ")))
upper_limit = 10

while True:
    if len(numbers) == 0:
        break
    else:
        filtered_nums = list(filter(lambda x: x <= upper_limit, numbers))
        for num in filtered_nums:
            numbers.remove(num)

        print(f"Group of {upper_limit}'s: {filtered_nums}")
        upper_limit += 10
