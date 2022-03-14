from typing import List

def leastInterval(tasks: List[str], n: int) -> int:
        import heapq
        queue = []
        w = 0 # waiting time
        l = 0 # how many task are left
        for elt in set(tasks):
            heapq.heappush(queue, (0, -tasks.count(elt)))
        ans = 0
        while len(queue)>0:
            heapq.heapify(queue)
            (w, l)= heapq.heappop(queue)
            # if w==0:
            #     print(t)
            # else:
            #     print("idle"*w)
            #     print(t)
            ans += w+1
            for i in range(len(queue)):
                a, b = queue[i]
                queue[i] = (max(0, a-1-w), b) 
            w=n
            l+=1
            if l<0:
                heapq.heappush(queue, (w, l))
            
        return ans            

print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))