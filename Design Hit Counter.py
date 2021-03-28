"""
This a solution for the problem from
https://leetcode.com/problems/design-hit-counter/

Here is the copy of the problem from leetcode:

Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:

HitCounter() Initializes the object of the hit counter system.
void hit(int timestamp) Records a hit that happened at timestamp (in seconds). Several hits may happen at the same timestamp.
int getHits(int timestamp) Returns the number of hits in the past 5 minutes from timestamp (i.e., the past 300 seconds).

"""
from collections import defaultdict
class HitCounter:

    def __init__(self):
        self.count_last_5=0
        self.map_sec_to_count=defaultdict(int)
        self.last_update=0
        """
        Initialize your data structure here.
        """
        

    def hit(self, timestamp: int) -> None:
        self.count_last_5+=1
        self.map_sec_to_count[timestamp]+=1
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        

    def getHits(self, timestamp: int) -> int:
        if self.last_update!=timestamp:
            to_pop=[]
            for key in self.map_sec_to_count.keys():
                if key<=timestamp-300:
                    self.count_last_5-=self.map_sec_to_count[key]
                    to_pop.append(key)
            for key in to_pop:
                self.map_sec_to_count.pop(key)
        return self.count_last_5
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
