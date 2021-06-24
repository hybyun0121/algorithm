from types import *
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = curr = 0
        tank = 0
        for i,j in zip(gas,cost):
            start = i if i > j

        curr = start
        while curr != start:
            for _ in range(len(gas)):
                tank += start+1 - cost[curr]
                if tank < 0:
                    return -1
                else:
                    curr = (curr+1) % len(gas)
                    tank += gas[curr]
    
