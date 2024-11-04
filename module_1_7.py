grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=list(students)
students = sorted(students)
average_scores = {}
for i in range(len(students)):
 student = list(students)[i]
 grades_list = grades[i]
 average_score = sum(grades_list) / len(grades_list)
 average_scores[student] = average_score
print(average_scores)