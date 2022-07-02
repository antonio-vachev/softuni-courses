

from math import ceil, floor

budget = float(input())
students = int(input())
price_single_flour = float(input())
price_single_egg = float(input())
price_single_apron = float(input())

free_flour_packages = floor(students / 5)
extra_aprons = ceil(students * 0.2)

price_eggs = 10 * price_single_egg * students
price_aprons = price_single_apron * (students + extra_aprons)
price_flour = (students - free_flour_packages) * price_single_flour

total_cost = price_eggs + price_aprons + price_flour

if total_cost <= budget:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    print(f"{abs(budget - total_cost):.2f}$ more needed.")
