'''
Explanation of Algorithm

Approach: The idea is to use Breadth First Search. The condition of patients getting infected is when they come in contact with other infected patients. This is similar to breadth-first search where the graph is divided into layers or circles and the search is done from lower or closer layers to deeper or higher layers.  To find the elements whose values are no the whole matrix had to be traversed.

'''

# Algorithm: 
# 1. Create an empty queue q. 
# 2. Find all infected victims and enqueue them to q. Also, keep a time variable to keep track of time passed.
# 3. Run a loop while q is not empty and number of uninfected patients is more than 0.
# 4. Dequeue a patient from the queue (popleft), infect all adjacent patients. While infecting the adjacent, make sure that the time frame is incremented only once, and the time frame is not incremented if there are no adjacent patients.
# 5. Append newly infected patients to queue and continue till while loop breaks
# 6. Return time if every single patient becomes infected, else return -1


from collections import deque

def infecting_patients(M,N,grid: list[list[int]]) -> int:
    q = deque()
    #time to keep track of time which has passed
    #uninfected to keep track of how many uninfected patients at any given point in time
    time, uninfected = 0,0

    if M > 1000 or N > 1000:
        return -1

    for r in range(M):
        for c in range(N):
            #if any cell in the grid is uninfected, increment the number of uninfected
            if grid[r][c] == 1:
                uninfected += 1
            #if any cell is infected, add coordinates to queue to run multi BFS
            if grid[r][c] == 2:
                q.append([r,c])

    #4 directions to move in
    directions = [[0,1],[0,-1],[1,0],[-1,0]]

    #if queue is empty and uninfected=0, then the loop will stop
    while q and uninfected>0:
        for i in range(len(q)):
            #popleft to pop the equivalent of the length of q,
            #while appending the adjacent patients which will
            #become infected
            r,c = q.popleft()
            #go through the 4 adjacent positions of the infected victim
            for dr,dc in directions:
                #getting coordinate of adjacent spots
                row, col = dr + r, dc + c
                # if in bounds and uninfected patient, make the patient infected
                # if out of bounds or is not a uninfected patient, continue the loop
                if (row < 0 or row == len(grid) or
                    col < 0 or col == len(grid[0]) or
                    grid[row][col] != 1):
                    continue
                grid[row][col] = 2
                q.append([row,col])
                #decrement the number of uninfected patients
                uninfected -= 1
        #loop is executed, increment time by 1
        time += 1
    #return time if every single patient becomes infected
    return time if uninfected == 0 else -1

#running unit tests
import unittest

class TestInfectingPatients(unittest.TestCase):
    def test_infecting_patients(self):
        actual1 = infecting_patients(3,5,
                                    [[2, 1, 0, 2, 1],
                                    [1, 0, 1, 2, 1],
                                    [1, 0, 0, 2, 1]])
        expected1 = 2
        self.assertEqual(actual1,expected1)

        actual2 = infecting_patients(1,1,[[2]])
        expected2 = 0
        self.assertEqual(actual2,expected2)

        actual3 = infecting_patients(1,1,[[1]])
        expected3 = -1
        self.assertEqual(actual3,expected3)

        actual4 = infecting_patients(1001,1001,[[1]])
        expected4 = -1
        self.assertEqual(actual4,expected4)        

