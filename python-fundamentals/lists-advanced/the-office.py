# You will receive two lines of input:
# •	a list of employees' happiness as a string of numbers separated by a single space
# •	a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# •	If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"

# Example of input:
# 1 2 3 4 2 1
# 3


happiness = list(map(int, input().split(" ")))
improvement = int(input())
improved_happiness = list(map(lambda x: x * improvement, happiness))
average_happiness = sum(improved_happiness) / len(improved_happiness)
above_average = list(filter(lambda x: x >= average_happiness, improved_happiness))

if len(above_average) >= len(improved_happiness)/2:
    print(f"Score: {len(above_average)}/{len(improved_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(above_average)}/{len(improved_happiness)}. Employees are not happy!")

