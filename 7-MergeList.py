list1 = [10, 20, 30, 20]
list2 = [40, 10, 50, 20]

merged = list1 + list2

merged.sort()

print("Merged and sorted list:", merged)

checked = []

for item in merged:
    if item not in checked:
        print(item, ":", merged.count(item))
        checked.append(item)