# LeetCode Question
Technical Test - Rotting Orange

This repo explains the code done for the Algorithm Test (Rotting Orange) as well as carries out the relevant unit tests to ensure the code is running as intended.

# File Information
1. README.md - contains information about the project
2. telepathylabs_bhavesh.py - code in py format, with unit tests

## Usage
```python
# check whether unit tests are running as intended in telepathylabs_bhavesh.py file
python -m unittest telepathylabs_bhavesh.py
```

## Explanation of Algorithm
Efficient Solution 

Approach: The idea is to use Breadth First Search. The condition of patients getting infected is when they come in contact with other infected patients. This is similar to breadth-first search where the graph is divided into layers or circles and the search is done from lower or closer layers to deeper or higher layers.  To find the elements whose values are 2 the whole matrix had to be traversed.
 
Algorithm: 
Create an empty queue q. 
Find all infected victims and enqueue them to q. Also, keep a time variable to keep track of time passed
Run a loop while q is not empty and number of uninfected patients is more than 0
Dequeue a patient from the queue (popleft), infect all adjacent patients. While infecting the adjacent, make sure that the time frame is incremented only once. And the time frame is not incremented if there are no adjacent patients.
Append newly infected patients to queue and continue till while loop breaks
Return time if every single patient becomes infected, else return -1

## Contributers
#### Bhavesh Chainani
#### Data Scientist
#### July 2022

