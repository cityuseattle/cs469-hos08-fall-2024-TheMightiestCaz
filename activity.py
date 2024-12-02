def activitySelection(start, finish):
    n = len(start)
    if n == 0: return []
    #sort in ascending order according to finish time,
    #no need to understand, Activity index store in 'actID'
    #so that you can get the correct index even after the sorting.
    start, finishe, actID = zip(*sorted(
        zip(start, finish, range(n)),
        key = lambda x: x[1]
    ))

    #`i` keeps track of the index of the last selected activity
    #`answer` to stor ethe selected activities index
    i, answer = 0, [actID[0]]

    for j in range(n):
        if start[j] >= finish[i]:
            answer.append(actID[j])
            i = j
        
    return answer

#test case #1: output = [0, 1, 2, 6]
print(activitySelection(
    [0, 3, 4, 2, 5, 3, 9, 11, 10],
    [3, 4, 5, 8, 9, 12, 13, 14, 15]

))

#test case #2:
print(activitySelection(
    [1, 3, 0, 5, 8, 5],
    [2, 4, 6, 7, 9, 9]

))

#Test case #3:
print(activitySelection(
    [4, 0, 1, 1, 3],
    [6, 2, 3, 6, 4]

))