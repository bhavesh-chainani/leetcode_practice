from collections import deque

def infecting_patients(M,N,grid: list[list[int]]) -> int:
    q = deque()
    time, fresh = 0,0

    #ROWS, COLS = len(grid), len(grid[0])

    if M > 1000 or N > 1000:
        return -1

    for r in range(M):
        for c in range(N):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append([r,c])

    directions = [[0,1],[0,-1],[1,0],[-1,0]]

    while q and fresh>0:
        for i in range(len(q)):
            r,c = q.popleft()
            for dr,dc in directions:
                row, col = dr + r, dc + c
                # if in bounds and fresh, make rotten
                if (row < 0 or row == len(grid) or
                    col < 0 or col == len(grid[0]) or
                    grid[row][col] != 1):
                    continue
                grid[row][col] = 2
                q.append([row,col])
                fresh -= 1
        time += 1
    return time if fresh == 0 else -1


if __name__ == "__main__":

    # M = 3
    # N = 5
    # grid = [[2, 1, 0, 2, 1],
    #     [1, 0, 1, 2, 1]
    #     [1, 0, 0, 2, 1]]

    M = 1
    N = 1
    grid = [[1]]

    print("Max time incurred: ", infecting_patients(M,N,grid))

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

