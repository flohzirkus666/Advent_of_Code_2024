list1 = list()
list2 = list()

# read contents from file
with open("puzzle1.txt", "r") as file:
    for line in file:
        columns = line.split()
        list1.append(int(columns[0]))
        list2.append(int(columns[1]))

# sort lists
list1.sort()
list2.sort()

difference = list()
# compare both lists
for item in zip(list1, list2):
    if item[0] < item[1]:
        difference.append(item[1] - item[0])
    else:
        difference.append(item[0] - item[1])

print(sum(difference))
