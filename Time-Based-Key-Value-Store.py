1class TimeMap:
2
3    def __init__(self):
4        self.store = {}
5        # perform binary search on a set with tuples appended to it 
6        # store mood with time 
7        # schema -> key: [[value, timestamp], [value, timestamp]]
8        
9    def set(self, key: str, value: str, timestamp: int) -> None:
10        if key not in self.store:
11            self.store[key] = []
12        self.store[key].append([value, timestamp])
13        
14    def get(self, key: str, timestamp: int) -> str:
15        # perform a binary search and add a fallback to previous
16        result = ""
17        values = self.store.get(key, [])
18        start = 0
19        end = len(values) - 1
20
21        while start <= end:
22            mid = (start + end) // 2
23            
24            # increasing order 
25            if values[mid][1] == timestamp:
26                return values[mid][0]
27            elif timestamp > values[mid][1]:
28                result = values[mid][0]
29                start = mid + 1
30            elif timestamp < values[mid][1]:
31                end = mid - 1
32
33        return result
34            
35
36
37# Your TimeMap object will be instantiated and called as such:
38# obj = TimeMap()
39# obj.set(key,value,timestamp)
40# param_2 = obj.get(key,timestamp)