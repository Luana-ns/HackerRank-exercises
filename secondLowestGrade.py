list = []
second_lowest_names = []
scores = set()

for _ in range(int(input('Number of students: '))):
    name = input('Enter name: ')
    score = float(input('Enter the value: '))
    list.append([name, score])
    scores.add(score)

second_lowest = sorted(scores)[1]

for name, score in list:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name, end='\n')
