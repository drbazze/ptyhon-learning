#https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    names = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append([name, score])

    # names = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39], ["Maki", 20], ["Majom", 20]]

    if len(names) == 1:
        print(names[0])
    else:
        #Student list sorted by grades
        sorted_by_grades = sorted(names, key=lambda x: x[1])
        #set of the grades, no duplicates
        second_lowest_score = sorted(list(set([x[1] for x in sorted_by_grades])))[1]
        #List of the second lowest scored students
        lower_performers = sorted([x[0] for x in sorted_by_grades if x[1] == second_lowest_score])

        # print(sorted_by_grades)
        print('\n'.join(lower_performers))