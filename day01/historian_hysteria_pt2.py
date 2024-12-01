list1 = list()
list2 = list()

# read contents from file
with open("puzzle1.txt", "r") as file:
    for line in file:
        columns = line.split()
        list1.append(int(columns[0]))
        list2.append(int(columns[1]))

similarity_score = list()

for item in list1:
    apperance = list2.count(item)
    similarity_score.append(item * apperance)

print(sum(similarity_score))