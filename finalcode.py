from collections import deque

def infecting_patients(grid: list[list[int]]) -> int:
    q = deque()
    time, uninfected = 0,0

    ROWS, COLS = len(grid), len(grid[0])

    if ROWS > 1000 or COLS > 1000:
        print("Input matrix too large")
        return -1

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                uninfected += 1
            if grid[r][c] == 2:
                q.append([r,c])

    directions = [[0,1],[0,-1],[1,0],[-1,0]]

    while q and uninfected>0:
        for i in range(len(q)):
            r,c = q.popleft()
            for dr,dc in directions:
                row, col = dr + r, dc + c
                # if in bounds and uninfected, patient becomes infected
                if (row < 0 or row == len(grid) or
                    col < 0 or col == len(grid[0]) or
                    grid[row][col] != 1):
                    continue
                grid[row][col] = 2
                q.append([row,col])
                uninfected -= 1
        time += 1
    return time if uninfected == 0 else -1


# if __name__ == "__main__":

#     M = 3
#     N = 5
#     grid = [[2, 1, 0, 2, 1],
#         [1, 0, 1, 2, 1],
#         [1, 0, 0, 2, 1]]

#     print("Max time incurred: ", infecting_patients(grid))

import unittest

class TestInfectingPatients(unittest.TestCase):
    def test_infecting_patients(self):
        actual = infecting_patients([[2, 1, 0, 2, 1],
                                    [1, 0, 1, 2, 1],
                                    [1, 0, 0, 2, 1]])
        expected = 2
        self.assertEqual(actual,expected)