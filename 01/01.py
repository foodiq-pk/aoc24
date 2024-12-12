import csv


def distance(list_a, list_b):
    
    list_a = sorted(list_a)
    list_b = sorted(list_b)
    distance = 0
    for i in range(len(list_a)):
        distance += abs(list_a[i] - list_b[i])
    return distance


def similarity(list_a, list_b):
    sim_score = 0
    for n in list_a:
        sim_score += n * list_b.count(n)
    return sim_score




input_file_1 = "01/01-input-test"
input_file_2 = "01/01-input-1"

with open(input_file_1) as f:
    file = csv.reader(f, delimiter=" ") # 3 spaces :/
    a = []
    b = []
    for c in file:
        a.append(int(c[0]))
        b.append(int(c[3]))
        
#1 test solution
print(distance(a,b))
print(similarity(a,b))


with open(input_file_2) as f:
    file = csv.reader(f, delimiter=" ") # 3 spaces :/
    a = []
    b = []
    for c in file:
        a.append(int(c[0]))
        b.append(int(c[3]))
#1 solutions
print(distance(a,b))
print(similarity(a,b))



