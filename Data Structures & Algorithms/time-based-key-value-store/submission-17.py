class TimeMap:

    def __init__(self):
        # Store it in groups with multiple version
        self.datastore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.datastore.get(key):
            self.datastore[key] = []
        
        # v1=hash, now=tuple
        self.datastore[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not self.datastore.get(key):
            return ""
        
        # if available check against the previous
        prev = self.datastore[key][-1]

        if prev[1] <= timestamp:
            return prev[0]

        # search version (less than prev, equal to timestamp)
        versions = self.datastore[key]

        left = 0
        right = len(versions) - 1

        # Invariant: Result always stores in <= timestamp
        
        res = ""
        while left <= right:
            mid = (left + (right))//2
            mid_ts = versions[mid][1]

            if mid_ts == timestamp:
                return versions[mid][0]
            elif mid_ts > timestamp:
                right = mid - 1
            else:
                res = versions[mid][0]
                left = mid + 1
        
        print(res)
        return res

        
