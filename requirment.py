from collections import defaultdict

def canFinish(numCourses, prerequisites):
    counter = []
    from queue import Queue
    for i in range(numCourses):
        counter.append(0)
    for a, b in prerequisites:
        counter[a] = counter[a]+1
    numWoutPrereq = 0
    withPrereq = Queue()
    for i in range(numCourses):
        if counter[i]==0:
            numWoutPrereq +=1
        else:
            withPrereq.put(i)
    while not withPrereq.empty():
        course = withPrereq.get()
        for a, b in prerequisites:
            if a==course:
                if counter[b]==0:
                    counter[a] = counter[a]-1
            if counter[a]==0:
                numWoutPrereq+=1
            else:
                withPrereq.put(a)
                
    return numWoutPrereq == numCourses

print(canFinish(3, [[0,1],[0,2],[1,2]]))