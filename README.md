# Telepathy_Labs
Technical Test - Telepathy Labs

This repo explains the code done as well as carries out the relevant unit tests to ensure the code is running as intended.

## Usage
```python
# check whether unit tests are running as intended
python -m  unittest finalcode.py
```

## Explanation of Algorithm
Efficient Solution 

Approach: The idea is to use Breadth First Search. The condition of patients getting infected is when they come in contact with other infected patients. This is similar to breadth-first search where the graph is divided into layers or circles and the search is done from lower or closer layers to deeper or higher layers.  To find the elements whose values are no the whole matrix had to be traversed.
 
Algorithm: 
Create an empty queue q. 
Find all infected victims and enqueue them to q. Also, enqueue a delimiter to indicate the beginning of the next time frame.
Run a loop while q is not empty
Do following while delimiter in q is not reached
Dequeue a patient from the queue, infect all adjacent patients. While infecting the adjacent, make sure that the time frame is incremented only once. And the time frame is not incremented if there are no adjacent patients.
Dequeue the old delimiter and enqueue a new delimiter. The victims infected in the previous time frame lie between the two delimiters.

## Contributers
#### Bhavesh Chainani
#### Data Scientist
#### July 2022

