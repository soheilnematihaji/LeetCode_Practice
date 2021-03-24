"""
This a solution for the problem from
https://leetcode.com/problems/time-based-key-value-store/

Here is the copy of the problem from leetcode:

Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.
2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").

"""

from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.keytime_value={}
        self.key_time=defaultdict(list)
        """
        Initialize your data structure here.
        """
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keytime_value[(key,timestamp)]=value
        self.key_time[key].append(timestamp)
        self.key_time[key].sort()

    def get(self, key: str, timestamp: int) -> str:
        list_times=self.key_time[key]
        if list_times:
            for i in range(len(list_times)-1,-1,-1):
                if timestamp>=list_times[i]:
                    return self.keytime_value[(key,list_times[i])]
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
