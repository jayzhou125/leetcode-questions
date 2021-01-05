class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sort boxType based on number of units per box
        boxTypes.sort(key=lambda x:x[1],reverse=1)
        maxUnits=0
        for i,j in boxTypes:
            i = min(i,truckSize)
            maxUnits += i * j
            truckSize -= i
            if truckSize == 0:
                break
        return maxUnits
